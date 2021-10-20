from flask import Blueprint, render_template
import db.mysql
import socket

crawler_route = Blueprint('crawler_route',__name__)

@crawler_route.route("/crawler")
def index():
    # conn = db.mysql.Connect()
    # cursor = conn.cursor()
    # sql = "SELECT * FROM ORDER_WORK_ANY LIMIT 10"
    # cursor.execute(sql)
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    print(socket.gethostbyname(socket.gethostname()))
    return render_template("index.html")
