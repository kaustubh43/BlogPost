# FROM ubuntu 
# WORKDIR /kaustubh_app
# COPY . /kaustubh_app/

FROM python:3.11
COPY . /kaustubh_app
RUN pip install -r /kaustubh_app/requirements.txt
ENTRYPOINT [ "python", "/kaustubh_app/manage.py", "runserver" ]