FROM python:3


RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*




WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app
#EXPOSE 8000

ENTRYPOINT ["python", "helloworld/manage.py"]
CMD ["makemigrations"]
CMD ["migrate"]
CMD ["runserver", "0.0.0.0:8800"]