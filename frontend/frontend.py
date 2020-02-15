from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import socket
import mysql.connector as sql
from os import environ
from datetime import datetime

"""
"""
app = Flask(__name__)

api = Api(app)

@app.route('/')
def index():
    database_login = {
        "user": environ["db_user"],
        "host": socket.gethostbyname("ci_db"),
        "database":"ci",
        "password":environ["db_password"]
    }
    assert database_login["host"] != "placeholder", "fill in db host"
    con = sql.connect(**database_login)
    try:
        cur = con.cursor()
        cur.execute("""SELECT project_name FROM ci;""")
        tup = cur.fetchall()
        data = [item[0] for item in tup]
    finally:
        con.close()
    return jsonify(data)


class tracker(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("path", required=True)
        parser.add_argument("project_name", required=True)
        parser.add_argument("file_name", required=True)
        parser.add_argument("branch", required=True)
        parser.add_argument("commit", required=True)
        args = parser.parse_args()
        print(args)
        project_name, path, file_name, commit, branch = args["project_name"], args["path"], args["file_name"], args["commit"], args["branch"]
        if ";" in path or ";" in project_name or ";" in file_name:
            return "Arguments can not contain ;"
        database_login = {
        "user": environ["db_user"],
        "host": socket.gethostbyname("ci_db"),
        "database":"ci",
        "password":environ["db_password"]
        }
        date = str(datetime.now())[:19]
        con = sql.connect(**database_login)
        try:
            cur = con.cursor()
            cur.execute(f"""INSERT INTO ci values ('{project_name}','{path}','{date}','{file_name}','{commit}','{branch}');""")
        finally:
            con.commit()
            con.close()
        return f"""Added {project_name} to ci tracker."""

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("project_name", required=True)
        parser.add_argument("file_name", required=True)
        args = parser.parse_args()
        print(args)
        project_name, file_name = args["project_name"], args["file_name"]
        database_login = {
        "user": environ["db_user"],
        "host": socket.gethostbyname("ci_db"),
        "database":"ci",
        "password":environ["db_password"]
        }
        try:
            con = sql.connect(**database_login)
            cur = con.cursor()
            cur.execute(f"""DELETE FROM ci WHERE project_name='{project_name}' and file_name='{file_name}';""")
        except:
            return f"""{project_name} not deleted from automated testing list."""
        finally:
            con.commit()
            con.close()
        return f"""{project_name} deleted from automated testing list."""


api.add_resource(tracker, '/tracker')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8081")