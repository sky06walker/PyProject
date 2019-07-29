import mysql.connector
from xlwt import Workbook

con = mysql.connector.connect(host='localhost',database='mysql',user='root',password='Pigbbong04!@')
cur = con.cursor()
wb = Workbook()
ws = wb.add_sheet("TestSheet")

cSql = 'SHOW DATABASES'
cur.execute(cSql)
bCreateDB = True

for x in cur:
    cDBName = ''.join(x)
    #print(cDBName)
    if cDBName == "students":
        cMsg = 'Database exists'
        bCreateDB = False
        break

if bCreateDB:
    cSql = 'Create Database students'
    cur.execute(cSql)
    cMsg = 'Database created'

con.close()

ws.write(0,0,"Test 1")
ws.write(0,1,"Test 2")
wb.save(r"C:\Users\WH\Downloads\Test.xlsx")

print(cMsg)
#Query to check is MySQL DB exists = 'CREATE DATABASE IF NOT EXISTS Students;'
#Query to show all MySQL DB = 'SHOW DATABASES'
