__cache__=dict()
def CompareDict(one, two):
    allowed={dict, int, float}
    diff=set(one)^set(two)
    onev=[one[a] for a in one if type(one[a]) in allowed and a not in diff]
    twov=[two[a] for a in two if type(two[a]) in allowed and a not in diff]
    if onev==twov:
        return 1
    key='%s%s' % (onev, twov)
    try:
        return __cache__[key]
    except KeyError:
        pass
    result=list()
    add=result.append
    for first, second in zip(onev, twov):
        try:
            if first==second:
                add(1)
            elif type(first)==dict and type(second)==dict:
                add(CompareDict(first, second))
            else:
                if first<second:
                    add(first/second)
                else:
                    add(second/first)
        except Exception as error:
            print(error, type(error))
    try:
        result=sum(result)/(len(result)+len(diff))
    except ZeroDivisionError:
        result=0
    __cache__[key]=result
    return result
