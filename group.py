from compare import CompareDict

def match(new, groups):
    potential=[]
    add=potential.append
    for i in groups:
        now=[]
        nowadd=now.append
        for a in groups[i]:
            nowadd(CompareDict(new, a))
        add([sum(now)/len(now), i])
    return potential

def creategroups(data, threshold=0.8):
    groups={}
    groups[hash(str(data[0]))]=[data[0]]
    for i in data:
        result=match(i, groups)
        result=max(result)
        if result[0]>threshold:
            groups[result[1]].append(i)
        else:
            groups[hash(str(i))]=[i]
    return groups
