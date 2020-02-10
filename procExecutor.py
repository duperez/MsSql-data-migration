import pymssql
import sys
from os import listdir
from os.path import isfile, join

#           _      _      _        
#  ___ __ _| |  __| |__ _| |_ __ _ 
# (_-</ _` | | / _` / _` |  _/ _` |
# /__/\__, |_| \__,_\__,_|\__\__,_|
#        |_|                       

server   = "localhost"
user     = "SA"
password = "your@pass123"
file     = "scripts/"


class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


#  _ __ _ _ ___  __ ___ ______
# | '_ \ '_/ _ \/ _/ -_|    print(bcolors.HEADER + "process with file " + bcolors.WARNING + sys.argv[
        2] + bcolors.HEADER + " has been initializated")
    exec(conn, read_proc_file(sys.argv[2]))

def get_database_info():
    lst = list()
    info = open('data.txt', 'r')
    for line in info:
        lst.append(line)
    return lst


def read_proc_file(name):
    file = open(name, 'r')
    proc = ''
    for line in file:
        proc = proc + line
    return proc


def exec(conn, proc):
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute(proc)


def set_environment(dir, conn):
    print(bcolors.HEADER + "setting environment up" + bcolors.HEADER)
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    onlyfiles.sort()
    for proc in onlyfiles:
        exec(conn, read_proc_file(file + proc))
        print(bcolors.WARNING + proc + bcolors.OKBLUE + " is now up to date")
    print(bcolors.OKGREEN + "environment configured" + bcolors.OKGREEN)


try:
    conn = pymssql.connect(server, user, password)
    set_environment(sys.argv[1], conn)
    conn.close()

    print(bcolors.OKGREEN + bcolors.UNDERLINE + "process finished \\o/ - the end\n" + bcolors.ENDC)
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(bcolors.FAIL + message)
