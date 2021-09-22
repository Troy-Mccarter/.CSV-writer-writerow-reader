
import csv  # importing csv module

xf = open("students.csv", "r", newline="\r\n")  # During the execution, the extra empty list forms. To get rid of that empty list, we have to add 'newline="\r\n"'

sobj = csv.reader(xf)  # reading 'students.csv'

for rec in sobj:  # reading all records in 'sobj' or simply 'students.csv'
    print(rec)  # printing records
