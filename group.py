import statistics
import compare

def match(new, groups):
    potential=[]
    for i in groups:
        now=[]
        for a in groups[i]:
            now.append(compare.compare(new, a))
        now=(statistics.mean(now)
             +statistics.median(now))
        potential.append([now/2, i])
    return potential

def creategroups(data, threshold=0.8):
    groups={}
    for a in range(len(data)):
        print(a, len(groups))
        i=data[a]
        result=match(i, groups)
        if result:
            result=max(result)
        else:
            result=[0]
        if result[0]>threshold:
            groups[result[1]].append(i)
        else:
            groups[hash(repr(i))]=[i]
    return groups
