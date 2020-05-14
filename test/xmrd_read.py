import xlrd

wb = xlrd.open_workbook("C:\\Users\\Admin\\Desktop\\data1.xlsx")
sh = wb.sheet_by_index(0)  # 第一个表
rowName = sh.row_values(0)#读取一行的数据
colName = sh.col_values(0)#读取一列的数据
row = len(colName)#读取行数
col = len(rowName)#读取列数
value = sh.cell(1,0).value#获取某个单元格的值
print(row)
print(col)
print(value)
for name in colName:
    print(name)
