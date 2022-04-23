from loguru import *
import pypyodbc


def unitExportEXCELDBCompare(exceldata):
    credential = "Driver={SQL Server};Server=AGL78\SQLEXPRESS;Database=CT-LIMS-FLUSHDB; UID=sa; PWD=ATE186@agaramtech"
    dbconnect = pypyodbc.connect(credential)

    cursor = dbconnect.cursor()

    query2 = "select sunitname,sdescription,ndefaultstatus from unit where nunitcode<>-1 order by 1 desc"

    cursor.execute(query2)

    row2 = cursor.fetchone()

    total=[]

    while row2:

        data=""
        for i in  row2:

            data=data+str(i)

        total.append(data)

        row2 = cursor.fetchone()

    finalValue=""
    for i in total:
        finalValue=finalValue=i

    finalResult="FAIL"

    for i in exceldata:
        if finalValue.__contains__(i):
            finalResult="PASS"
        else:
            finalValue="FAIL"

    if finalResult=="PASS":
        logger.info("The exported record is matching with database")
    else:
        logger.error("The exported record is not matching with database")


unitExportEXCELDBCompare("D")