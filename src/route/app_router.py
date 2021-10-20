from flask import Blueprint, render_template
import db.mysql
app_route = Blueprint('app_route',__name__)

@app_route.route("/")
def index():
    # Flask 렌더러
    db.mysql.Connect()
    return render_template("index.html")

@app_route.route('/healthz')
def healthEcho():
    # K8S Health check 
    return 'Hello flask, i\'m alive!'

@app_route.route('/headers')
def headers():
    # HTTP 상세히 찍어보기 (개발 테스트)
    return print_header()
