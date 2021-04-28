f = open('C:\\Users\\ezulq\\Desktop\\data.txt','r')
Lines = f.readlines()
count = 0
total = 0
for line in Lines:
    try:
        print(float(line.strip()))
        total += float(line.strip())
        count+=1
    except:
        continue

print('Average KD : ', round(total/count,2))

