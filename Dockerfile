FROM python:3.7
WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile
RUN pipenv install
COPY . .
EXPOSE 8000
ENTRYPOINT ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000"]
