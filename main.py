# system import
import json
import jsonschema
from flask import Flask, send_file
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from GCSBucket import storage_client, BUCKET_NAME

# Google Cloud storage App
app = Flask("GCStorage")
api = Api(app)


class GCStorageApiVew(Resource):
    # get method
    def get(self):
        blob_name = 'configuration-file.json'
        bucket_in_gcp = storage_client.bucket(BUCKET_NAME)
        file = bucket_in_gcp.blob(blob_name)
        if file.exists():
            file.download_to_filename(blob_name)
            return send_file(blob_name, as_attachment=True)
        else:
            return {"message": "file not found"}, 404

    def post(self):
        # GivenSample Data
        provided_schema = {
            "firstName": str,
            "secondName": str,
            "ageInYears": int,
            "address": str,
            "creditScore": float
        }
        # Taking file from the API
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=FileStorage, location='files')
        args = parser.parse_args()
        file = args['file']

        filename_check = file.filename
        if filename_check == "configuration-file.json":
            file_contents = file.read()
            file.seek(0)
            data = json.loads(file_contents)
            try:
                # verified to ensure the file match[JSON schema]
                jsonschema.validate(data, provided_schema)
                # Get the filename and extension for upload
                filename = secure_filename(file.filename)
                bucket = storage_client.get_bucket(BUCKET_NAME)
                blob = bucket.blob(filename)
                blob.upload_from_file(file.stream)
                return {"message": "File uploaded successfully"}, 200

            except jsonschema.exceptions.ValidationError as e:
                return {"message": e.message}, 400
        else:
            return {
                "message": "the file format is invalid. It should be 'configuration-file.json'" # noqa
            }, 400


api.add_resource(GCStorageApiVew, "/config")

if __name__ == "__main__":
    app.run()
