file=open("liczby.txt","r")
binnumbers=[]
for line in file:
    line=line.rstrip()
    binnumbers.append(line)
file.close()
result=0
for i in binnumbers:
    zerocount=0
    onecount=0
    for j in range(0,len(i)):
        if i[j]=="0":
            zerocount+=1
        elif i[j]=="1":
            onecount+=1
    if zerocount>onecount:
        result+=1
print(result)