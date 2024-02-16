w, h = map(int,input().split())
cord = [h//2]
res = []

for i in range(w//2):
    tire = ['-']*h
    for j in cord:
        tire[j:j+2] = ['.','|','.']
        if i > 0:
            symCord = cord[0] + 3*j
            tire[symCord:symCord+2] = ['.','|','.']
    res.append(''.join(tire))
    cord.append(cord[-1]-3)

invers = res[::-1]
cote = (h-7)//2
print("\n".join(res + ['-'*cote + "WELCOME" + '-'*cote] + invers))