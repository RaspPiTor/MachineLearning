def CompareDict(one, two):
    result=[]
    for i in set(list(one)+list(two)):
        try:            
            try:
                if one[i]==two[i]:
                    result.append(1)
                else:
                    result.append(min(one[i]/two[i], two[i]/one[i]))
            except TypeError:
                if type(one[i])==dict and type(two[i])==dict:
                    result.append(CompareDict(one[i], two[i]))
        except Exception:
            pass
    try:
        return sum(result)/len(result)
    except ZeroDivisionError:
        return 0
