FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /vehicles_code
WORKDIR /vehicles_code
COPY . /vehicles_code/
RUN chmod +x entry-point.sh
#COPY requirements.txt /vehicles_code/
RUN pip install -r requirements.txt

