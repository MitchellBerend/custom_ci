import socket
import lib
from os import environ
import subprocess
import smtplib
from datetime import datetime

database_login_info = {
    "user":environ["db_user"],
    "password":environ["db_password"],
    "database":"ci",
    "host":socket.gethostbyname("ci_db")
}

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((socket.gethostname(),5000))
sock.listen(10)
while True:
    client, address = sock.accept()
    data = client.recv(10000).decode("utf-8")
    data = eval(data)
    command = ["python", "test/"+data["file_name"]]
    cwd="../home" + data["path"]
    shell = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    print("shell")
    with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(environ["email"],environ["password"])
        subject = f"""{data["project_name"]} commit hash {data["last_commit"]} test ran at {str(datetime.now())[:19]}"""
        body = str(shell.stdout) + str(shell.stderr)
        print(body)
        msg = f"""Subject: {subject}\n\n{body}"""
        print(msg)
        smtp.sendmail(environ["email"], environ["target_email"],msg)
    new_hash = lib.get_new_hash(data["path"],data["branch"])
    lib.update_commit(data["project_name"],data["path"],data["timestamp"],data["file_name"],new_hash,data["branch"],**database_login_info)
    client.send(bytes(f"""{data["project_name"]}""","utf-8"))
    break