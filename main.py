# system import
import pathlib
from flask import Flask
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from read_json_file import validate_file


# Google Cloud storage App
app = Flask("GCStorage")
api = Api(app)

# making fonder for file
working_dir = pathlib.Path.cwd()
files_folder = working_dir.joinpath('my_files')
downloads_folder = working_dir.joinpath('downloaded')


class GCStorageApiVew(Resource):

    # get method
    def get(self):
        return "hello world"

    def post(self):
        # read file from the request
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=FileStorage, location='files')
        args = parser.parse_args()
        file = args['file']
        # get file name
        filename = file.filename
        if filename == "configuration-file.json":
            # check provided_schema valid or not
            status, messages = validate_file(file)
            if not status:
                return {"message": messages}, 400
            return {"message": "Successfully Saved"}, 200
        else:
            return {
                "message": "the file format is invalid. It should be 'configuration-file.json'" # noqa
            }, 400


api.add_resource(GCStorageApiVew, "/config")

if __name__ == "__main__":
    app.run()
