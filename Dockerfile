FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements requirements

RUN pip install -r requirements/local.txt

COPY . .

EXPOSE 8000

CMD [ "python", "manage.py", "runserver"]
