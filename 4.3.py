file=open("liczby.txt","r")
numbers=[]
for line in file:
    line=line.rstrip()
    numbers.append(int(line,2))
file.close()
minindex=0
maxindex=0
minnumber=numbers[0]
maxnumber=numbers[0]
for i in range(0,len(numbers)):
    if numbers[i]<minnumber:
        minnumber=numbers[i]
        minindex=i+1
    if numbers[i]>maxnumber:
        maxnumber=numbers[i]
        maxindex=i+1

print(minindex,maxindex)