FROM python:3.12 AS builder

WORKDIR /app 

COPY requirements.txt /app

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app 

CMD ["./wait-for-it.sh", "postgres:5432", "--", "sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]



FROM builder as dev-envs

RUN apk update && \
	apk add git

RUN addgroup -S docker && \
	adduser -S --shell /bin/bash --ingroup docker vscode

# Install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /

CMD ["./wait-for-it.sh", "postgres:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]