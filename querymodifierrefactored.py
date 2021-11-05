def setOffAlarms(p):
    print('Watch out for.....' + p + '!')

def findCriminal (people):
    for p in people:
        if (p == 'Don'):
            return 'Don'
        if (p == 'John'):
            return 'John'
    return ''

p = findCriminal(['Dan','Don'])
setOffAlarms(p)