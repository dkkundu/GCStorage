# __File Management System__

1. ### Run the project
    - Run `Venv` and `and set the interpater`.
   ```
    python3.9 -m venv venv
    source venv/bin/activate
   
    pip install pip --upgrade pip
    pip install -r requirements.txt
    python main.py
    ```

     
2. ### ADD CREDENTIALS
    - OPEN the GCSBucket.py File.
   ```
   # ADD YOUR BUCKET NAME
   # ADD YOUR GOOGLE APPLICATION CREDENTIALS FILE
   # AND PUT IT INTO THIS APPLICATION ROOT PATH
   
   BUCKET_NAME = "stored-configuration-files"
   GOOGLE_APPLICATION_CREDENTIALS = "add-your-file.json"
   
   ```
   > _NOTE: Browse to [http://127.0.0.1:5000/config](http://127.0.0.1:5000/config) to view the api. (GET and POST Request Allow)_

