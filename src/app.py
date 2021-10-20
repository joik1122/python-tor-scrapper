from flask import Flask, render_template, request
from route.app_router import app_route
from route.crawler_router import crawler_route
import os
import time
import logging
import socket

# 리퀘스트 디버깅 테스트용 
def print_header():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    data = f''' 
------------------------------
You accessed to path    {request.path}
Access Server URL       {request.base_url}
Container Hostname      {host_name}
Container IP            {host_ip}
Original IP with Proxy  {request.environ.get('HTTP_X_REAL_IP', request.remote_addr)}
Static string           {''}
------------------------------
Flask received HTTP header
{request.headers}
'''
    logging.info(data)
    return data

app = Flask(__name__)

app.register_blueprint(app_route)
app.register_blueprint(crawler_route)

if __name__ == "__main__":
    # 로거 세팅 파이썬 로깅 아키텍처 -> logging.info('안녕') 요런식으로 사용합니다. 단순 print 지양
    log_level = logging.INFO
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

    # waitress flask run
    from waitress import serve
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 80)))