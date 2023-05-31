FROM python:3.8-slim-buster

WORKDIR /flask-loan-app

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]