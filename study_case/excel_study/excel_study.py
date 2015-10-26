# coding=UTF-8

from util.base.excel.xl_util import open_excel
from util.base.excel.xl_util import read
from util.base.excel.xl_util import create_workbook
from util.base.excel.xl_util import create_writer
from util.base.excel.xl_util import create_sheet
from util.base.excel.xl_util import write
from util.base.excel.xl_util import save_workbook

__author__ = 'jubileus'


# 测试方法
def test():
    src = open_excel('/home/jubileus/office file/投资事件分析表格.xls')
    data = read(src.sheet_by_index(0))

    wb = create_workbook()
    ew = create_writer(wb)

    ws = create_sheet(wb, 'finance', 0)

    write(data, ws)

    save_workbook(ew, '/home/jubileus/office file/rs.xlsx')

