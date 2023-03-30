import csv

h = 0
file = open("data.csv")
reader = csv.reader(file)
lines= len(list(reader))
print(lines)

with open('data.csv') as f:
    reader = csv.reader(f,delimiter='|')
    l = [row for row in reader]
    with open("data.csv") as f:
        reader = csv.reader(f)
        for i in reader:
            print(l[h][1])
            h += 1

        # //*[@id="airdrop-block"]/div/div[1]/span[2]