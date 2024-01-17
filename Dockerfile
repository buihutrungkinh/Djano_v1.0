# Use an official Python runtime as a parent image
FROM python:alpine3.19
WORKDIR /usr/src/app
COPY . .
RUN pip install --upgrade pip
#COPY /root/home/tamnq3/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "./Task/manage.py", "runserver", "0.0.0.0:8000"]
