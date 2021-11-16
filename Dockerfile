FROM python:3.10.0rc2-slim-buster
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt requirements.txt
COPY .env .env
RUN apt-get update \
    && apt-get -y install libpq-dev gcc python-dev libldap2-dev libsasl2-dev libssl-dev
RUN pip3 install -r requirements.txt

# #entrypoint stuff...
# COPY ./entrypoint.sh .
# RUN sed -i 's/\r$//g' /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh

# # copy project

# COPY . .
# # run entrypoint.sh
# ENTRYPOINT ["/app/entrypoint.sh"]