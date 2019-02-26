a = [23,34,56,5,2,1,93]
b=[]
#result = [x for x in a if x < a[[a.index(x)]+1] else a[[a.index(x)]+1]]


'''for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]

print (a)'''

for x in a:
    try:
        c = a.index(x)
        if x > a[c]:
            a[c],a[c+1] = a[c+1],a[c]
        else:
            b.append(a[c-1])
    except Exception:
        print(b)
        print(Exception)

print(a)