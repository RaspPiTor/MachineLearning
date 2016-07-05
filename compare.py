__cache__=dict()
def CompareDict(one, two):
    allowed=[dict, int, float]
    onev=[a for a in one.values() if type(a) in allowed]
    twov=[a for a in two.values() if type(a) in allowed]
    if onev==twov:
        return 1
    try:
        key='%s%s' % (str(onev), str(twov))
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
        result=sum(result)/len(result)
    except ZeroDivisionError:
        result=0
    __cache__[key]=result
    return result
