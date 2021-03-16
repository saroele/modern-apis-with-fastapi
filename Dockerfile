FROM python:3.9

WORKDIR /usr/src

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["bash"]