# __File Management System__

1. ### ADD CREDENTIALS
    - OPEN the GCSBucket.py File.
   ```
   # ADD YOUR BUCKET NAME
   # ADD YOUR GOOGLE APPLICATION CREDENTIALS FILE
   # AND PUT IT INTO THIS APPLICATION ROOT PATH
   
   BUCKET_NAME = "stored-configuration-files"
   GOOGLE_APPLICATION_CREDENTIALS = "add-your-file.json"
   
2. ### RUN WITH VIRTUAL ENVIRONMENT
    - Run `Venv` and `and set the interpreter`.
   ```
    python3.9 -m venv venv
    source venv/bin/activate
    # Windows: source venv/Scripts/activate

    pip install pip --upgrade pip
    pip install -r requirements.txt
    python main.py
    ```
3. ### RUN WITH DOCKER
    - Install Docker in our System.
   ```
   # docker build -t gcstorage . 
   # docker run -p 5000:5000 gcstorage:latest

   ```
   > _NOTE: Browse to [http://127.0.0.1:5000/config](http://127.0.0.1:5000/config) to view the api. (GET and POST Request Allow)_

