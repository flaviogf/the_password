FROM python:3.7
WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile
RUN pipenv install
COPY . .
EXPOSE 8000
ENV SCRIPT_NAME=/thepassword
ENTRYPOINT [ "pipenv", "run", "gunicorn", "--bind", "0.0.0.0"]
