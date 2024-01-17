FROM python:alpine3.19
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "./Task/manage.py", "runserver", "0.0.0.0:8000"]
