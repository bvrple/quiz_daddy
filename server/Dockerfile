FROM python:3.10-alpine3.19

WORKDIR /quiz-daddy-server

COPY . .

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

EXPOSE 4000

CMD ["pipenv", "run", "python", "main.py"]