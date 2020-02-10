import re
import sys
from os import listdir
import pymssql
import operator

#           _      _      _
#  ___ __ _| |  __| |__ _| |_ __ _
# (_-</ _` | | / _` / _` |  _/ _` |
# /__/\__, |_| \__,_\__,_|\__\__,_|
#        |_|

server   = "localhost"
user     = "SA"
password = "your@pass123"


class sql_file:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.data = ''

    def set_data(self):
        sql = open(self.path + self.name, 'r')
        proc = ''
        for line in sql:
            proc = proc + line
            self.data = proc


class color:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    UNDERLINE = '\033[4m'


def execute(connection, proc):
    connection.autocommit(True)
    cursor = connection.cursor()
    cursor.execute(proc.data)


def get_all_files(dir):
    all_file = list()
    folder = [f for f in listdir(dir)]
    for file in folder:
        if re.match('.*sql', file):
            all_file.append(sql_file(dir, file))
        else:
            if file != dir:
                all_file = all_file + get_all_files(dir + file + '/')
    return all_file


def set_environment(folder, connection):
    print(color.HEADER + "setting environment up" + color.HEADER)
    files = get_all_files(folder)
    files.sort(key=lambda x: x.name, reverse=False)
    for proc in files:
        proc.set_data()
        execute(connection, proc)
        print(color.WARNING + proc.name + color.OKBLUE + " is now up to date")
    print(color.OKGREEN + "environment configured" + color.OKGREEN)


try:
    conn = pymssql.connect(server, user, password)
    set_environment(sys.argv[1], conn)
    conn.close()

    print(color.OKGREEN + color.UNDERLINE + "process finished \\o/ - the end\n" + color.ENDC)
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(color.FAIL + message)
