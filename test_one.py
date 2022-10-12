def dont_give_me_five(start,end):
    x=[]
    for i in range(start, end+1):
        z=str(i)
        if '5' in z:
            continue
        else:
            x.append(i)
    return len(x)

print(dont_give_me_five(4,17))












































