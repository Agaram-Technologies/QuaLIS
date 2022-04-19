import pypyodbc

def unitExcel():
    credential = "Driver={SQL Server};Server=AGL78\SQLEXPRESS;Database=CT-LIMS-FLUSHDB; UID=sa; PWD=ATE186@agaramtech"
    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    query = "update users set "

    cursor.execute(query)

    row = cursor.fetchone()

    value = row[0]

    print(value)

    while row:
        print(row)
        row = cursor.fetchone()

