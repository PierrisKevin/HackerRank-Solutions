w, h = map(int,input().split(" "))
cord =[h//2]
res = []
for i in range(w//2):
    tire = list("-"*h)
    for j in range(len(cord)):
        tire[cord[j]]="|"
        tire[cord[j]+1]=tire[cord[j]-1] ="."
        # Le symetrie 
        if i>0:
            symCord = cord[0]+3*j
            tire[symCord]="|"
            tire[symCord+1] =tire[symCord-1] ="."
    res.append("".join(tire))
    cord.append(cord[-1]-3)
invers = res[::-1]
cote = (h-7)//2
print("\n".join(res), "-"*cote+"WELCOME"+"-"*cote, "\n".join(invers) , sep="\n")