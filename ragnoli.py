def print_rangoli(size):
    tire = (size + size -2)*2
    alsize = [chr(i) for i in range(97,97+size)]
    cord = [(tire+1)//2]

    response = []
    for i in range(size):
        trace = list("-"*(tire+1))
        for j in range(len(cord)):
            if j==0:
                trace[cord[j]]=alsize[-(i+1)]
            
            else:
                trace[cord[j]] = alsize[-(i+1-j)]
                trace[cord[j]+4*j] = alsize[-(i+1-j)]
        cord.append(cord[-1]-2)
        response.append("".join(trace))

    inserse = response[::-1][1:len(response)+1]
    print("\n".join(response),"\n".join(inserse),sep="\n")

print_rangoli(5)