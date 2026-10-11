FROM python:3.9-slim

WORKDIR /app

# COPY . .

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app.py app.py

#Create a label on the image with the port number
EXPOSE 5000  


CMD [ "python3" ,"app.py" ]