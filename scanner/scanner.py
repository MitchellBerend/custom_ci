import socket
import lib
from os import environ
from time import sleep

database_login_info = {
    "user":environ["db_user"],
    "password":environ["db_password"],
    "database":"ci",
    "host":socket.gethostbyname("ci_db")
}

targets = lib.get_targets(**database_login_info)

for item in targets:
    last_com = item["last_commit"]
    print(f"""Checking {item["project_name"]}""")
    print(last_com)
    current_com = lib.scan(item["path"],item["branch"])
    item["current_commit"] = current_com
    if last_com != current_com:
        print(f"""sending test signal for {item["project_name"]}""")
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((socket.gethostbyname("tester_ci"),5000))
        sock.send(bytes(str(item), "utf-8"))
        data = ""
        while True:
            msg = sock.recv(1024)
            if len(msg) <= 0:
                break
            data += msg.decode("utf-8")
        print(data)
        sock.close()