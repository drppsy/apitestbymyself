import xlrd
from xlutils.copy import copy

class OperaExcel():

    def __init__(self,file_name=None,sheet_id = None):
        if file_name is not None:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = "../data/apitestcase.xlsx"
            self.sheet_id = 0
        self.table = self.get_table_data()

    # 基于文件名和表单号，获取对应的表单数据
    def get_table_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheets()[self.sheet_id]
        return table

    # 基于表单，获取对应表单的行数
    def get_table_lines(self):
        table = self.table
        return table.nrows

    # 基于行号和列号，获取对应单元格的内容
    def get_cell_value(self,colid,rowid):
        table = self.table
        cell_value = table.cell_value(colid,rowid)
        return cell_value

    # 根据列号，获取该列的内容
    def get_clodata_by_cloid(self,cloid=None):
        if cloid is not None:
            clodata = self.table.col_values(cloid)
        else:
            clodata = self.table.col_values(0)
        return clodata

    # 根据行号，获取该行的内容
    def get_rowdata_by_rowid(self,rowid):
        rowdata = self.table.row_values(rowid)
        return rowdata

    # 根据单元格内容，获取单元格所在的行号
    def get_rowid_by_cell_value(self,cell_value):
        rowid = 0
        clodata = self.get_clodata_by_cloid()
        for clo in clodata:
            if cell_value == clo:
                return rowid
            rowid += 1

    # 根据单元格内容，获取该行的数据
    def get_rowdata_by_cell_value(self,cell_value):
        rowid = self.get_rowid_by_cell_value(cell_value)
        rowdata = self.get_rowdata_by_rowid(rowid)
        return rowdata

    # 基于行号、列号和值，在excel行列中写入数据
    def write_value(self,row,col,value):
        data = xlrd.open_workbook(self.file_name)
        excel = copy(data)
        sheet = excel.get_sheet(0)
        sheet.write(row,col,value)
        excel.save(self.file_name)

# 单元测试
def test_opera_excel():
    excel = OperaExcel()
    lines = excel.get_table_lines()
    assert lines == 3

    cell_value = excel.get_cell_value(1,2)
    assert "apitest.xiniujiao.net" in cell_value

    col_values = excel.get_clodata_by_cloid()
    print(col_values)

    row_data = excel.get_rowdata_by_rowid(1)
    print(row_data)

    rowid = excel.get_rowid_by_cell_value("yxsq002")
    print(rowid)

    rowdata = excel.get_rowdata_by_cell_value("yxsq002")
    print(rowdata)

    write_data = excel.write_value(2,9,'pass')
    cell_value = excel.get_cell_value(2,9)

test_opera_excel()




