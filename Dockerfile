FROM python:3

ENV AWS_ACCESS_KEY_ID =AKIAWI6HBHC3AO255M4V
ENV AWS_SECRET_ACCESS_KEY=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
ENV AWS_DEFAULT_REGION=us-east-2

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app
#EXPOSE 8000

ENTRYPOINT ["python", "helloworld/manage.py"]
CMD ["runserver", "0.0.0.0:8800"]