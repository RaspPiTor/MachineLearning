def CompareDict(one, two):
    if one==two:
        return 1
    result=[]
    add=result.append
    for i in set(list(one)+list(two)):         
        try:
            if one[i]==two[i]:
                add(1)
            else:
                now=[one[i]/two[i], two[i]/one[i]]
                if now[0]<now[1]:
                    add(now[0])
                else:
                    add(now[1])
        except TypeError:
            if type(one[i])==dict and type(two[i])==dict:
                add(CompareDict(one[i], two[i]))
        except IndexError:
            add(0)
        except Exception:
            pass
    try:
        return sum(result)/len(result)
    except ZeroDivisionError:
        return 0
