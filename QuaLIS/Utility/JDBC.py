import pypyodbc


def unitExcel():
    credential = "Driver={SQL Server};Server=AGL78\SQLEXPRESS;Database=CT-LIMS-FLUSHDB; UID=sa; PWD=ATE186@agaramtech"
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


def userName():
    credential = "Driver={SQL Server};Server=AGL78\SQLEXPRESS;Database=CT-LIMS-FLUSHDB; UID=sa; PWD=ATE186@agaramtech"
    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    query = "select sfirstname from users where sloginid='admin'"

    cursor.execute(query)

    row = cursor.fetchone()

    value = row[0]

    print(value)

    while row:
        print(row)
        row = cursor.fetchone()

    query2 = "select sfirstname from users where sloginid='admin'"

    cursor.execute(query2)

    row2 = cursor.fetchone()

    value2 = row2[0]

    print(value2)

    while row2:
        print(row2)
        row2 = cursor.fetchone()


    username=value+" "+value2

    return value2

