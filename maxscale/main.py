# Joshua Brown, jbrown02@student.rtc.edu
# 6/12/2023, Spring Quarter
# CNE 370 - Christine Sutton
# Sharded Database Query Engine (This code utilizes database sharding to organize a collection of zip codes)

import mysql.connector

db = mysql.connector.connect(host="172.18.0.4", port="4000", user="maxuser", password="maxpwd")
cursor = db.cursor()

# Largest zipcode in zipcodes_one
print('The largest zipcode in zipcodes_one:')
cursor = db.cursor()
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
results = cursor.fetchall()
for result in results:
    print(result)

# All zipcodes where state = KY
print('All zipcodes where state = KY:')
cursor = db.cursor()
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE State = 'KY' ORDER BY Zipcode ASC;")
results_zipcodes_one = cursor.fetchall()
cursor.execute("SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE State = 'KY' ORDER BY Zipcode ASC;")
results_zipcodes_two = cursor.fetchall()
for zipcodes_one, zipcodes_two in zip(results_zipcodes_one, results_zipcodes_two):
    print(zipcodes_one[0], zipcodes_two[0])

# All zipcodes between 40000 and 41000
print('All zipcodes between 40000 and 41000:')
cursor = db.cursor()
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000 ORDER BY Zipcode ASC;")
results_zipcodes_three = cursor.fetchall()
cursor.execute("SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE zipcode BETWEEN 40000 AND 41000 ORDER BY Zipcode ASC;")
results_zipcodes_four = cursor.fetchall()
for zipcodes_three, zipcodes_four in zip(results_zipcodes_three, results_zipcodes_four):
    print(zipcodes_three[0], zipcodes_four[0])

# The TotalWages column where state = PA
print('The TotalWages column where state = PA:')
cursor = db.cursor()
cursor.execute("SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE state = 'PA' ORDER BY TotalWages ASC;")
results_zipcodes_five = cursor.fetchall()
cursor.execute("SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE state = 'PA' ORDER BY TotalWages ASC;")
results_zipcodes_six = cursor.fetchall()
for zipcodes_five, zipcodes_six in zip(results_zipcodes_five, results_zipcodes_six):
    print(zipcodes_five[0], zipcodes_six[0])
