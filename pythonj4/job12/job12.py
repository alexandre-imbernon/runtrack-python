val=[5,2,4,3]
u=1
i=0
min=val[0]
minpos=0
if val[i]<min:
        min=val[i]
        minpos=i
        tamp=val[0]
        val[0]=val[i]
        val[i]=tamp
while i<len(val):
    while u<(3):
        if val[i]>val[u]:
            tamp2=val[u]
            val[u]=val[i]
            val[i]=tamp2
            print(val)
        u=u+1
    i=i+1

print(val)