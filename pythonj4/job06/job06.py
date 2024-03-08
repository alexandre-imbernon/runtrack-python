def switchlist():
    L = [1,2,3,4,5]
    print(L)
    for i,m in [(0,4)]:
        L[i], L[m] = L[m], L[i]
    return L

print(switchlist())