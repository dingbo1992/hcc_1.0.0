import pymysql
from xlwt import *
import xlrd


class ExcelAction:

    def mysql2excel(self, file_path):
        connect = pymysql.Connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="123456",
            db="bj03",
            charset='utf8'
        )
        print("写入中，请等待……")

        cursor = connect.cursor()
        sql = "select * from booktest_areainfo"
        cursor.execute(sql)
        number = cursor.fetchall()
        fp = open(file_path, "w")
        loan_count = 0
        for loanNumber in number:
            loan_count += 1
            fp.write(str(loanNumber) + "\n")
        fp.close()
        cursor.close()
        connect.close()
        print("写入完成,共写入%d条数据！" % loan_count)

    def data2excel(self, file_path, data):
        # 需要xlwt库的支持
        # import xlwt
        file = Workbook(encoding='utf-8')
        # 指定file以utf-8的格式打开
        table = file.add_sheet('data')
        # 指定打开的文件名

        # data = {
        #     # "1": ["张三", 150, 120, 100],
        #     # "2": ["李四", 90, 99, 95],
        #     # "3": ["王五", 60, 66, 68]
        # }
        # 字典数据

        ldata = []
        num = [a for a in data]
        # for循环指定取出key值存入num中
        num.sort()
        # 字典数据取出后无需，需要先排序

        for x in num:
            # for循环将data字典中的键和值分批的保存在ldata中
            t = [int(x)]
            for a in data[x]:
                t.append(a)
            ldata.append(t)

        for i, p in enumerate(ldata):
            # 将数据写入文件,i是enumerate()函数返回的序号数
            for j, q in enumerate(p):
                # print i,j,q
                table.write(i, j, q)
        file.save(file_path)
        # return self

    def excel_read(self, file_path):

        wb = xlrd.open_workbook(file_path)
        sh = wb.sheet_by_index(0)  # 第一个表
        rowName = sh.row_values(0)  # 读取一行的数据
        colName = sh.col_values(0)  # 读取一列的数据
        row = len(colName)  # 读取行数
        col = len(rowName)  # 读取列数
        value = sh.cell(1, 0).value  # 获取某个单元格的值
        print(row)
        print(col)
        print(value)
        for name in colName:
            print(name)


ExcelAction().mysql2excel('C:\\Users\\Admin\\Desktop\\data7.xlsx')