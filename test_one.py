def sort_by_length(arr):
    d={}
    l=[]
    for i in arr:
        d[len(i)]=i
    for v, k in sorted(d.items()):
        l.append(k)
    return l

print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))












































