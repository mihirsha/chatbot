FROM python:3.9.7

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt --timeout=100

COPY . .

COPY ./entrypoint.sh /

ENTRYPOINT [ "sh", "/entrypoint.sh" ]
