file=open("liczby.txt","r")
numbers=[]
for line in file:
    numbers.append(int(line,2))
file.close()
divisionbytwo=0
divisionbyeight=0
for x in numbers:
    if x%2==0:
        divisionbytwo+=1
    if x%8==0:
        divisionbyeight+=1

print(divisionbytwo,divisionbyeight)