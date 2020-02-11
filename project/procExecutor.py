import re
import sys
from os import listdir
import pymssql
from project import sql_file, paint
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

#           _      _      _
#  ___ __ _| |  __| |__ _| |_ __ _
# (_-</ _` | | / _` / _` |  _/ _` |
# /__/\__, |_| \__,_\__,_|\__\__,_|
#        |_|

server = "localhost"
user = "SA"
password = "your@pass123"


#  _ __ _ _ ___  __ ___ ______
# | '_ \ '_/ _ \/ _/ -_|_-<_-<
# | .__/_| \___/\__\___/__/__/
# |_|

def print_logo():
    f = open('logo.txt', 'r')
    logo = ''
    for line in f:
        logo = logo + line
    print(f'{paint.color.OKBLUE}{logo}{paint.color.HEADER}Migration\n')


def execute(connection, proc):
    connection.autocommit(True)
    cursor = connection.cursor()
    cursor.execute(proc.data)


def get_files_and_folders(dir):
    all_files = list()
    all_folders = list()
    folder = [f for f in listdir(dir)]
    for file in folder:
        if re.match('.*sql', file):
            all_files.append(sql_file.sql_file(dir, file))
        else:
            if file != dir:
                all_folders.append(dir + file + '/')

    return all_files, all_folders


def proccess_folder(folder, connection):
    print(f'{paint.color.OKBLUE}entering in: {paint.color.WARNING}{folder}{paint.color.ENDC}')
    files, folders = get_files_and_folders(folder)
    folders.sort()
    setSortAndRun(files, connection)
    if len(folders) > 0:
        for dir in folders:
            proccess_folder(dir, connection)
    print(f"{paint.color.OKBLUE}All files in {paint.color.WARNING}{folder}{paint.color.OKBLUE}"
          f"have been processed (•̀ᴗ•́)و̑̑ - going back to the top folder {paint.color.ENDC}")


def setSortAndRun(files, connection):
    files.sort(key=lambda x: x.name, reverse=False)
    for proc in files:
        proc.set_data()
        print(f'{paint.color.WARNING}\'{proc.name}\' {paint.color.OKBLUE}process is starting{paint.color.ENDC}')
        execute(connection, proc)
        print(f'{paint.color.WARNING}\'{proc.name}\' {paint.color.OKBLUE}process is finished{paint.color.ENDC}')


try:
    print_logo()
    print(f"{paint.color.HEADER}starting environment migration{paint.color.ENDC}")

    conn = pymssql.connect(server, user, password)
    proccess_folder(sys.argv[1], conn)
    conn.close()

    print(f"{paint.color.HEADER}process finished ٩(ᐛ)و - the end\n")
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(paint.color.FAIL + message)
