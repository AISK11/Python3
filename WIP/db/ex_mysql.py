#!/usr/bin/env python3

################################################################################
##                                   README                                   ##
################################################################################
## Demo example how to manage MySQL DB in Python3.


################################################################################
##                                  Theory                                    ##
################################################################################
'''
1. Install MariaDB (on Artix):
# pacman -S mariadb mariadb-dinit
# mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
2. Start MariaDB daemon:
# dinitctl start mysqld
3. Create user:
# mariadb
MariaDB> CREATE USER 'python'@'%' IDENTIFIED BY 'python3';
MariaDB> CREATE USER 'python'@'localhost' IDENTIFIED BY 'python3';
MariaDB> GRANT ALL PRIVILEGES ON *.* TO 'python'@'%';
MariaDB> GRANT ALL PRIVILEGES ON *.* TO 'python'@'localhost';


Additional resources:
- https://wiki.archlinux.org/title/MariaDB
- https://www.w3schools.com/python/python_mysql_getstarted.asp
'''


################################################################################
##                                  Modules                                   ##
################################################################################
## Installation (Arch): $(pacman -S python-mysql-connector)
import mysql.connector


################################################################################
##                             Public Variables                               ##
################################################################################
## DB variables.
db_config = {
    "user":     "python",
    "host":     "localhost",
    "password": "python3",
}

## Connect to database.
db_conn = mysql.connector.connect(**db_config)

## Create database cursor to execute commands.
db_cursor = db_conn.cursor()


################################################################################
##                                 Functions                                  ##
################################################################################
## Returns list of tuples in format [('HOST', 'USER', 'PASSWORD'), ...]
def db_show_users():
    db_cursor.execute("SELECT host, user, password FROM mysql.user;")
    return db_cursor.fetchall()


## Returns list of tuples in format [('DATABASE',), ...]
def db_show_databases():
    db_cursor.execute("SHOW DATABASES;")
    return db_cursor.fetchall()


## Returns database name in string.
def db_show_current_database():
    db_cursor.execute("SELECT DATABASE();")
    return db_cursor.fetchall()[0][0]



## Check if specified database exists.
## 0 = database does not exists
## 1 = database does exists
def db_is_valid(db):
    if (db,) in db_show_databases():
        return 1
    else:
        return 0


## Create specified database.
## 0 = success
## 1 = database already exists
## 2 = other error (permissions probably)
def db_create_database(db):
    try:
        db_cursor.execute(f"CREATE DATABASE {db};")
        return 0
    except Exception:
        ## Check if database already exists.
        if db_is_valid(db):
            return 1 ## Database exists.
        else:
            return 2 ## Database does not exists. Most likely caused by missing permissions.


## Delete specified database.
## 0 = success
## 1 = database does not exists
## 2 = other error (permissions probably)
def db_drop_database(db):
    try:
        db_cursor.execute(f"DROP DATABASE {db};")
        return 0;
    except Exception:
        ## Check if database does not exists.
        if not db_is_valid(db):
            return 1 ## Database does not exists.
        else:
            return 2 ## Database does exists. Most likely caused by missing permissions.


## Delete specified database.
## 0 = success
## 1 = database does not exists
## 2 = other error (permissions probably)
def db_select_database(db):
    try:
        db_cursor.execute(f"USE {db};")
        return 0;
    except Exception:
    ## Check if database does exists.
        if not db_is_valid(db):
            return 1 ## Database does not exists.
        else:
            return 2 ## Database does exists but still couldnt be selected. Most likely caused by missing permissions.


## Program starting function.
def main():
    print(f"Listing all users...\n{db_show_users()}\n")
    print(f"Listing all databases...\n{db_show_databases()}\n")
    print(f"Loading currently selected database...\n{db_show_current_database()}\n")


    database = "showcase_db"
    print(f"Deleting database '{database}'...")
    if db_drop_database(database) == 0:
        print(f"Database '{database}' deleted successfully.")
    elif db_drop_database(database) == 1:
        print(f"Error! Database '{database}' could not be deleted. Database does not exists!")
    else:
        print(f"Error! Database '{database}' could not be deleted. Maybe check if you have permissions?")
    print(f"\nListing all databases...\n{db_show_databases()}\n")

    print(f"Creating database '{database}'...")
    if db_create_database(database) == 0:
        print(f"Database '{database}' created successfully.")
    elif db_create_database(database) == 1:
        print(f"Error! Database '{database}' could not be created. Database already exists!")
    else:
        print(f"Error! Database '{database}' could not be created. Maybe check if you have permissions?")
    print(f"\nListing all databases...\n{db_show_databases()}\n")

    print(f"Selecting database '{database}'...")
    if db_select_database(database) == 0:
        print(f"Database '{database}' selected successfully.")
    elif db_select_database(database) == 1:
        print(f"Error! Database '{database}' could not be selected. Database does not exists!")
    else:
        print(f"Error! Database '{database}' could not be selected. Maybe check if you have permissions?")




## Python3 program start execution.
if __name__ == "__main__":
    main()
