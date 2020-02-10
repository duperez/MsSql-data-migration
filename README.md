
This is a simple python scritp that I created to migrate data to a docker with sql server.


how to execute:
> python3 procExecutor.py your_migration_dir


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

To run this application install pyodbc (sql server dependency)

_how to install_:

```
sudo apt install python3-pip
sudo apt install unixodbc-dev
pip3 install --user pyodbc

```

If you are using my docker-compose file, you should access the sql bash using this guide:

```
#   --    To open shell    --
docker exec -it <docker_id> "bash"

#   --  To open sql shell  --
/opt/mssql-tools/bin/sqlcmd -S localhost -U <"user_name"> -P <"pass">
```
