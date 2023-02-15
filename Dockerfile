FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip3 install pip --upgrade pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
# Define environment variable
ENV NAME VENV
# Run app.py when the container launches
CMD ["python", "main.py"]

