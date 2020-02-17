import mysql.connector as sql
import subprocess

def get_new_hash(path,branch):
    """
    path
    branch
    """
    cwd = "../home/mitchell" + path + "/.git/refs/heads"
    command = ["cat", branch]
    text = subprocess.run(command,cwd=cwd, text=True, capture_output=True)
    return text.stdout[:7]


def update_commit(project_name, path, timestamp, file_name, new_hash, branch,**login_info):
    """
    project_name
    path
    timestamp
    file_name
    new_hash
    branch
    """
    assert login_info != {}, "Login info not passed as an argument."
    con = sql.connect(**login_info)
    try:
        cur = con.cursor()
        cur.execute(f"""DELETE FROM ci WHERE project_name='{project_name}';""")
        cur.execute(f"""INSERT INTO ci values('{project_name}','{path}','{timestamp}','{file_name}','{new_hash}','{branch}');""")
    finally:
        con.commit()
        con.close()