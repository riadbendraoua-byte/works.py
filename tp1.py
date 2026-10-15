import math 
print ("exo1")
n = 0 
n = int(input())
somme=0
for i in range (0,n):
        if (i%2 == 0 ):
            somme+=i
           
print (somme)
print ("exo2")
x = int(input())
while x>9:
    s=0
    while x>0 : 
        s=s+x%10
        x=x/10
    x=s
print (x)
print ("exo3")
def estpri (n) : 
    if n < 2 :
        return False
    for i in (2,math.sqrt(n)):
        if n%i==0 :
            return False
    return True 
print(estpri (15))
print ("exo4")
t=[5,2,8,1]
for i in range (0,len(t)-1):
    for j in range (0,len(t)-i-1) :
        if t[j]>t[j+1] : 
            t[j],t[j+1]=t[j+1],t[j]
print (t)
print ("exo 5")
t=[]
for i in range (0,10):
    t.append(int(input("donne num ")))
s=0
for i in range (0,len(t)):
    if t[i]%2 == 0:
             s=s+t[i]
print (s)
t=[2,5,7,5,44,85,445,87]
t2=[]
for i in range (len(t)) :
    t2.append(pow(t[i],2))
print (t)
print (t2)
t3=[i*i for i in t]
print (t3)
c = int ( input ())
while c !=0 :
    c--
    if c == 0 : 
        tx.append (15)
imp = [1,3,5,7,9,11,13,15]
pai = [0,2,4,6,8,10,12,14]
i,c = 0 
for j in range (min(len(imp,pai))):
    if imp[i]<pai[c] :
        tout.append(imp[i])
        i++
    else : 
        tout.append(pai[c])
        c++
if min(len(imp,pai))==len(imp):
    for k in range (len(imp),len(pai)):
        tout[k]=
