[![#](https://img.shields.io/badge/licence-MIT-blue.svg)](#) [![#](https://img.shields.io/badge/python-3-yellow.svg)](#)

This is a simple python scritp that I created to migrate data to a docker with sql server.

how to execute:
> python3 procExecutor.py your_migration_folder

or, if you are just testing, just execute the run.sql to put docker up and run the python
> ./run.sh your_migration_folder

changing sql connection:

* in the script, the first variable has the data to connect with sql server, just change it as you want.

* These data are the same in the docker-compose file in this repo

```
# --------------------------------
# sql data
# --------------------------------
#   host="localhost",
#   user="SA",
#   passwd="your@pass123"
```

dependencies:

To run this application, install pyodbc (python dependency for sql server)

_how to install dependencies_:

```
sudo apt install python3-pip
sudo apt install unixodbc-dev
pip3 install --user pyodbc
```

If you are using my docker-compose file, you can access the sql bash using this guide:

```
#   -- To open docker shell --
docker exec -it <docker_id> bash

#   -- To open sql shell (execute on docker shell) --
/opt/mssql-tools/bin/sqlcmd -S localhost -U <user_name> -P <pass>
```
in your environment folder:

If you want an specific execution order of your files, just enumerate your files as the example bellow.

```
00_database_creation.sql
01_table_creation.sql
.
.
.
```
