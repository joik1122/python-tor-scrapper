# 기본 설정
FROM python:3.9.2-alpine3.12
RUN apk add --no-cache --update tzdata && \
        cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
        echo "Asia/Seoul" > /etc/timezone

# COPY ./python /python
WORKDIR /src/

# 의존성 설치
COPY ./requirements.txt /pydata/requirements.txt
RUN pip install --no-cache-dir -r /pydata/requirements.txt
RUN apk add sudo
# RUN sudo sh /src/tor.sh

# Codebase
COPY ./src /src/
ENTRYPOINT ["python", "/src/app.py"]