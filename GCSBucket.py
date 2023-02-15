from google.cloud import storage
import os

# ADD YOUR BUCKET NAME
BUCKET_NAME = "stored-configuration-files"
# ADD YOUR GOOGLE APPLICATION CREDENTIALS FILE 
# AND PUT IT INTO THIS APPLICATION ROOT PATH
GOOGLE_APPLICATION_CREDENTIALS = "evident-scion-377815-dedcf4b27bf4.json"

PATH = os.path.join(os.getcwd(), GOOGLE_APPLICATION_CREDENTIALS)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = PATH
storage_client = storage.Client(PATH)
