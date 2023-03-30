import csv
h = 0


with open('data.csv','rt') as f:
    reader = csv.reader(f,delimiter='|')
    print(reader[h],[1])
    h += 1
    
        