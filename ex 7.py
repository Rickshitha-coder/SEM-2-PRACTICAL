sentence=input()
upper=[]
lower=[]
u_count=0
l_count=0
def split():
    for i in sentence:
        if i.isupper()==True:
            upper.append(i)
        if i.islower()==True:
            lower.append(i)
            
split()
for i in upper:
    u_count+=1
print(u_count)
for i in lower:
    l_count+=1
print(l_count)
        
