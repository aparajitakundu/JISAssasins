#question 17 done by aparajita kundu
x= input('enter the set of numbers :(enter space seperatedvalue):')
list1= x.split(" ")
res=[]
for i in list1:
    n = int(i)
    for j in range(2,int(n/2)):
        if(n%j == 0):
            break
    else:
        res.append(n)
print(res)
