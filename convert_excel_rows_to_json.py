import xlrd
import json

def row_to_json(column_names, row_data):
    row_list = []
    for item in row_data:
        row_val = {}
        for i in range(0, column_names.__len__()):
            row_val[column_names[i]] = item[i]
        row_list.append(json.dumps(row_val))
    return row_list

def xls_to_dict(workbook_url):
    workbook_dict = {}
    book = xlrd.open_workbook(workbook_url)
    sheets = book.sheets()
    for sheet in sheets:    
        workbook_dict[sheet.name] = {}
        columns = sheet.row_values(0)
        rows = []
        for row_index in range(1, sheet.nrows):
            row = sheet.row_values(row_index)
            rows.append(row)
        sheet_data = row_to_json(columns, rows)
        workbook_dict[sheet.name] = sheet_data
    return workbook_dict
    

sample = xls_to_dict('data.xlsx')
print(sample)
