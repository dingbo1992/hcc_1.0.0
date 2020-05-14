import pymysql


def get_loan_number(file_txt):
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
    fp = open(file_txt, "w")
    loan_count = 0
    for loanNumber in number:
        loan_count += 1
        fp.write(str(loanNumber) + "\n")
    fp.close()
    cursor.close()
    connect.close()
    print("写入完成,共写入%d条数据！" % loan_count)


if __name__ == "__main__":
    file_txt = 'C:\\Users\\Admin\\Desktop\\data2.xlsx'
    get_loan_number(file_txt)