import sqlite3, csv

connection = sqlite3.connect('reports.db')
cursor = connection.cursor()

with open('TeamMap.csv','r', newline='') as file:
    reader = csv.reader(file)
    next(reader, None) #Skip the headers
    cursor.execute("DROP TABLE IF EXISTS TeamMap")
    cursor.execute("CREATE TABLE IF NOT EXISTS TeamMap(TeamId INTEGER PRIMARY KEY, Name VARCHAR)")
    table = "TeamMap"
    no_records = 0
    for row in file:
        cursor.execute("INSERT OR IGNORE INTO TeamMap VALUES (?,?)",row.split(","))#Ignore makes sure it doesnt insert duplicates
        cursor.execute("UPDATE TeamMap set Name = REPLACE(REPLACE(Name,'\r',''),'\n','')") #gets rid of '\n' which were unintentionally getting inserted with the strings 
        connection.commit()
        no_records += 1
print("{} Records Inserted Into {} table".format(no_records,table))

with open('ProductMaster.csv','r') as file:
    reader = csv.reader(file)
    next(reader, None) #Skip the headers
    cursor.execute("DROP TABLE IF EXISTS ProductMaster")
    cursor.execute("CREATE TABLE IF NOT EXISTS ProductMaster(ProductId INTEGER PRIMARY KEY, Name VARHCAR, Price FLOAT, Lotsize INTEGER)")
    table = "ProductMaster"
    no_records = 0
    for row in file:
        cursor.execute("INSERT OR IGNORE INTO ProductMaster VALUES (?,?,?,?)",row.split(","))
        connection.commit()
        no_records += 1
print("{} Records Inserted Into {} table".format(no_records,table))

with open('Sales.csv','r') as file:
    reader = csv.reader(file)
    cursor.execute("DROP TABLE IF EXISTS Sales")
    cursor.execute("CREATE TABLE Sales(SaleId INTEGER PRIMARY KEY, ProductId INTEGER, TeamId INTEGER, Quantity INTEGER, Discount FLOAT)")
    table = "Sales"
    no_records = 0
    for row in file:
        cursor.execute("INSERT OR IGNORE INTO Sales VALUES (?,?,?,?,?)",row.split(","))
        connection.commit()
        no_records += 1
print("{} Records Inserted Into {} table".format(no_records, table))


cursor.execute("DROP TABLE IF EXISTS TeamGrossRevenue")
cursor.execute("CREATE TABLE TeamGrossRevenue(TeamId INTEGER, TeamName VARCHAR, GrossRevenue FLOAT)")

cursor.execute("""INSERT INTO TeamGrossRevenue
                  SELECT DISTINCT tm.TeamId, tm.name"TeamName", SUM(pm.price * pm.lotsize * s.Quantity) "GrossRevenue"
                  FROM Sales s
                  JOIN TeamMap tm on tm.TeamId = s.TeamId
                  JOIN ProductMaster pm on pm.ProductId = s.ProductId
                  group by tm.TeamId, tm.name
                  """)

TeamReport = cursor.execute("SELECT RTRIM(TeamName)TeamName, GrossRevenue FROM TeamGrossRevenue ORDER BY GrossRevenue DESC")

with open('TeamReport.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['TeamName','GrossRevenue'])
    writer.writerows(TeamReport)
    print("TeamReport.csv generated and exported")

ProductReport = cursor.execute("""SELECT DISTINCT LTRIM(pm.name)Name, SUM(pm.price * pm.lotsize * s.Quantity)"GrossRevenue" , SUM(pm.Lotsize*s.Quantity)"TotalUnits", (SUM(pm.price * pm.lotsize * s.Quantity) * (s.Discount / 100))"Total Discount"
                  FROM Sales s
                  JOIN TeamMap tm on tm.TeamId = s.TeamId
                  JOIN ProductMaster pm on pm.ProductId = s.ProductId
                  GROUP BY pm.name
                  ORDER BY SUM(pm.price * pm.lotsize * s.Quantity) DESC
                  """)


with open('ProductReport.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['Name','GrossRevenue', 'TotalUnits', 'DiscountCost'])
    writer.writerows(ProductReport)
    print("ProductReport.csv generated and exported")
connection.close()

