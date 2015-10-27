# coding=UTF-8

# from util.base.excel.xls_reader import open_excel, get_sheet_by_index
# from util.base.excel.xls_reader import read
#
# from util.base.excel.xlsx_writer import create_workbook
# from util.base.excel.xlsx_writer import create_writer
# from util.base.excel.xlsx_writer import create_sheet
# from util.base.excel.xlsx_writer import write
# from util.base.excel.xlsx_writer import save_workbook

from util.base.excel.xlsx_reader import get_workbook
from util.base.excel.xlsx_reader import get_sheet_names
from util.base.excel.xlsx_reader import get_sheet_by_name
from util.base.excel.xlsx_reader import read


__author__ = 'jubileus'


# 测试方法1
# def test_1():
#     src = open_excel('/home/jubileus/office file/投资事件分析表格.xls')
#     data = read(get_sheet_by_index(src, 0))
#
#     wb = create_workbook()
#     ew = create_writer(wb)
#     ws = create_sheet(wb, 'finance', 0)
#
#     write(data, ws)
#     save_workbook(ew, '/home/jubileus/office file/rs.xlsx')


# 测试方法2
def test_2():
    src = get_workbook('/home/jubileus/office file/投资事件分析表格.xlsx')
    if src:
        names = get_sheet_names(src)
        ws = get_sheet_by_name(src, names[0])
        data = read(ws, row_e=30)
        for r in range(len(data)):
            line = ''
            for c in range(len(data[r])):
                line += str(data[r][c]) + ";  "
            print(line)


# test_1()
test_2()
