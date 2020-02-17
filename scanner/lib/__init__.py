import mysql.connector as sql
import subprocess


def get_targets(**login_info):
    """
    returns a list with dictionaries.
    keys:
        - path
        - file_name
    """
    assert login_info != {}, "login_info not passed correctly"
    con = sql.connect(**login_info)
    try:
        cur = con.cursor()
        cur.execute(f"""SELECT * FROM ci;""")
        tup = cur.fetchall()
    finally:
        con.close()
    return [{"project_name":item[0],"path":item[1],"timestamp":item[2],"file_name":item[3],"last_commit":item[4],"branch":item[5]} for item in tup]


def scan(path,head):
    cwd = "../home/mitchell" + path + "/.git/refs/heads"
    command = ["cat", head]
    text = subprocess.run(command,cwd=cwd, text=True, capture_output=True)
    return text.stdout[:7]
