FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get -y update
RUN apt-get -y install vim
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    pip install pymysql &&\
    pip install numpy &&\
    pip install pandas &&\ 
    pip install beautifulsoup4 &&\
    apt-get -y install sqlitebrowser &&|
    pip install pymysql &&|
    pip install requests