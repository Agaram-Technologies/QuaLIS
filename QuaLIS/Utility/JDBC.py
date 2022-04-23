from configparser import ConfigParser

import pypyodbc
from loguru import logger

from Utility import BasicOperation

configDriver=ConfigParser()
configDriver.read(BasicOperation.projectDirectory()+"\\config.ini")

sqlserver=configDriver.get("Database","server")
userName=configDriver.get("Database","userName")
password=configDriver.get("Database","password")
database=configDriver.get("Database","database")

print(database)

print(sqlserver)

credential = "Driver={SQL Server};"+"Server={};Database={}; UID={}; PWD={}".format(sqlserver,database,userName,password)


def unitExcel():


    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    query = "select count(*) from unit where nstatus=1 and nunitcode<>-1 order by 1 desc"

    cursor.execute(query)

    row = cursor.fetchone()

    value = row[0]

    print(value)

    while row:
        print(row)
        row = cursor.fetchone()

    return  value


def retunOneValue(query):
    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    cursor.execute(query)

    row = cursor.fetchone()

    value = row[0]

    print(value)

    return value

retunOneValue("select nunitcode from unit where nunitcode=1")




def unitCount():
    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    query2 = "select COUNT(*) from unit where nstatus=1 and nunitcode<>-1"

    cursor.execute(query2)

    row2 = cursor.fetchone()

    value2 = row2[0]

    print(value2)

    while row2:
        print(row2)
        row2 = cursor.fetchone()



    return value2




def dbunit():
    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    query2 = "select sunitname,sdescription,ndefaultstatus from unit where nstatus=1 and nunitcode<>-1"

    cursor.execute(query2)

    row2 = cursor.fetchone()

    value2 = row2[0]

    print(value2)

    while row2:
        print(row2)
        row2 = cursor.fetchone()


def name(name):
    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    query2 = "select sunitname from unit where sunitname='2000'"

    cursor.execute(query2)

    row = cursor.fetchone()

    i=1

    while row:
        a=row[0]
        row = cursor.fetchone()
        if a=="2000":
            print(a)
            i=i+1

    print(i)
    if 2 > 1:
        logger.info("It accept the duplicate entry in db")

    else:
        logger.error("It not accept the duplicate entry in DB")






def unitExcel():
    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    query2 = "select sunitname,sdescription,ndefaultstatus from unit where nunitcode<>-1"

    cursor.execute(query2)

    row2 = cursor.fetchone()

    while row2:
        print(row2)
        row2 = cursor.fetchone()

    return  row2

retunOneValue("select nunitcode from unit where nunitcode=1")