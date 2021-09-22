import csv  # importing csv module

xf = open("students.csv", "w")  # opening 'students.csv' as write mode 'w'

sobj = csv.writer(xf)  # writing into file named 'xf'

Range = int(input("Range: "))  # how many times we have to recall 'for loop'

for i in range(Range):
  
    # taking inputs from user
    A = int(input("Adm. no:"))  
    N = input("Nme: ")
    P = float(input("Percentage:"))
    
    L = [A, N, P]  
    
    sobj.writerow(L)  # writing L as a row inside 'students.csv' with the help of sobj
    
xf.close()
