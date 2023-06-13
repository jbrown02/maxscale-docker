# Joshua Brown, jbrown02@student.rtc.edu
# 6/12/2023, Spring Quarter
# CNE 370 - Christine Sutton
# Sharded Database Query Engine (This code utilizes database sharding to organize a collection of zip codes)

import mysql.connector

db = mysql.connector.connect(host="172.21.0.4", port="4000", user="maxuser", password="maxpwd")
cursor = db.cursor()

print('The largest zipcode in zipcodes_one:')
cursor.execute("SELECT Zipcode FROM zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
results = cursor.fetchall()
for result in results:
    print(result)

print('All zipcodes where state = KY:')
cursor.execute("SELECT Zipcode FROM zipcodes_one WHERE State = 'KY' UNION SELECT Zipcode FROM zipcodes_two WHERE State = 'KY';")
results = cursor.fetchall()
for result in results:
    print(result)

print('All zipcodes between 40000 and 41000:')
cursor = db.cursor()
cursor.execute("SELECT Zipcode FROM zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000 UNION SELECT Zipcode FROM zipcodes_two WHERE zipcode BETWEEN 40000 AND 41000;")
results = cursor.fetchall()
for result in results:
    print(result)

print('The TotalWages column where state = PA:')
cursor = db.cursor()
cursor.execute("SELECT TotalWages FROM zipcodes_one WHERE state = 'PA' UNION ALL SELECT TotalWages FROM zipcodes_two WHERE state = 'PA';")
results = cursor.fetchall()
for result in results:
    print(result)
