from conf.setting import DATA_PATH
import os
import xlrd

# def txt_2list(file_name):
#     data_file_path = os.path.join(DATA_PATH,file_name)
#     with open(data_file_path,"r",encoding='utf-8')as fr:
#         #['username1,password1,1\n', 'username2,password1,success\n', 'username3,password1,1\n', 'username4,password1,success\n', 'username5,password1,1\n']
#         res = fr.readlines()
#         data_list =[]
#         for v in res:
#             new_v = v.strip('\n')
#             if new_v.strip():
#                 data_list.append(new_v.strip().split(','))
#     return data_list

#print(txt_2list())

def textFileToList(file_name,seq = ','):
    data_file_path = os.path.join(DATA_PATH,file_name)
    case_data = []
    with open(data_file_path,encoding='utf-8') as f:
        for line in f:
            new_line = line.strip()
            if new_line:
                case_data.append(new_line.split(seq))
    return case_data
# 返回的是二维列表




def excelToList(filename):
    data_file_path = os.path.join(DATA_PATH,filename)
    book = xlrd.open_workbook(data_file_path)
    sheet = book.sheet_by_index(0)
    row_count = sheet.nrows
    case_data = []
    for row in range(row_count):
        row_data = sheet.row_values(row)
        case_data.append(row_data)
    return case_data
# 返回的是二维列表

print(excelToList("excel_data.xls"))
























