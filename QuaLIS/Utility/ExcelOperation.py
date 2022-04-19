import openpyxl

def numberOfRows(excelSheet):

    # to open the workbook
    # workbook object is created
    wb = openpyxl.load_workbook(excelSheet)
    sheet_obj = wb.active

    # print the total number of rows
    print(sheet_obj.max_row-1)

numberOfRows("D")

"D:\\excel\\Export (13).xlsx"

