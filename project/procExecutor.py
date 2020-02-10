import re
import sys
from os import listdir
import pymssql
from project import sql_file, paint

#           _      _      _
#  ___ __ _| |  __| |__ _| |_ __ _
# (_-</ _` | | / _` / _` |  _/ _` |
# /__/\__, |_| \__,_\__,_|\__\__,_|
#        |_|

server   = "localhost"
user     = "SA"
password = "your@pass123"


def execute(connection, proc):
    connection.autocommit(True)
    cursor = connection.cursor()
    cursor.execute(proc.data)


def get_all_files(dir):
    all_file = list()
    folder = [f for f in listdir(dir)]
    for file in folder:
        if re.match('.*sql', file):
            all_file.append(sql_file.sql_file(dir, file))
        else:
            if file != dir:
                all_file = all_file + get_all_files(dir + file + '/')
    return all_file


def set_environment(folder, connection):
    print(paint.color.HEADER + "setting environment up" + paint.color.HEADER)
    files = get_all_files(folder)
    files.sort(key=lambda x: x.name, reverse=False)
    for proc in files:
        proc.set_data()
        execute(connection, proc)
        print(paint.color.WARNING + proc.name + paint.color.OKBLUE + " is now up to date")
    print(paint.color.OKGREEN + "environment configured" + paint.color.OKGREEN)


try:
    conn = pymssql.connect(server, user, password)
    set_environment(sys.argv[1], conn)
    conn.close()

    print(paint.color.OKGREEN + paint.color.UNDERLINE + "process finished \\o/ - the end\n" + paint.color.ENDC)
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(paint.color.FAIL + message)
