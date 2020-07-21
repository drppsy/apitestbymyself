import os
import xlrd
from xlutils.copy import copy
root_path = os.path.abspath("..")


class OperaExcel():

    def __init__(self,file_path=None,sheet_id=None):
        if file_path is not None:
            self.file_path = file_path
            self.sheet_id = sheet_id
        else:
            self.file_path = root_path + '/data/apitestcases.xlsx'
            self.sheet_id = 0
        self.table = self.get_table()

    def get_table(self):
        table = xlrd.open_workbook(filename=self.file_path).sheets()[self.sheet_id]
        return table

    def get_lines(self):
        lines = self.table.nrows
        return lines

    def get_cell_value(self,rowid,colid):
        cell_value = self.table.cell_value(rowid,colid)
        return cell_value

    def get_col_values_by_colid(self,colid):
        col_values = self.table.col_values(colid)
        return col_values

    def get_rowid_by_cell_value(self,cell_value):
        rowid = 0
        col_values = self.get_col_values_by_colid(0)
        for value in col_values:
            if cell_value == value:
                return rowid
            rowid += 1

    def get_row_values_by_rowid(self,rowid):
        row_values = self.table.row_values(rowid)
        return row_values

    def get_row_values_by_cell_value(self,cell_value):
        rowid = self.get_rowid_by_cell_value(cell_value)
        row_values = self.get_row_values_by_rowid(rowid)
        return row_values

    def write_data(self,row,col,value):
        excel = xlrd.open_workbook(self.file_path)
        excel = copy(excel)
        table = excel.get_sheet(0)
        table.write(row,col,value)
        excel.save(self.file_path)

if __name__ == '__main__':
    opra_excel = OperaExcel()

# def test_opera_excel():
#     excel = OperaExcel()
    # lines = excel.get_lines()
    # print(lines)

    # cell_value = excel.get_cell_value(1,2)
    # print(cell_value)

    # col_values = excel.get_col_values_by_colid(0)
    # print(col_values)

    # rowid = excel.get_rowid_by_cell_value('yxsq001')
    # print(rowid)

    # row_values = excel.get_row_values_by_rowid(1)
    # print(row_values)

    # row_values = excel.get_row_values_by_cell_value('yxsq002')
    # print(row_values)

#     excel.write_data(1,11,'pass')
#     row_values = excel.get_row_values_by_rowid(1)
#     print(row_values)
#
# test_opera_excel()
