#refactor: separate query from modifier
#Martin Fowler

# Create a new query method to return what the original method did.
# Change the original method so that it returns only the result of calling the new query method.
# Combine steps: query and call command/modifier

#Every method should either be a command that performs an action, or a query that returns data to the caller, but never both.


def setOffAlarms(p):
    print('Watch out for.....' + p + '!')

def alertForCriminals (people):
    for p in people:
        if (p == 'Don'):
            #setOffAlarms(p)
            return 'Don'
        if (p == 'John'):
            #setOffAlarms(p)
            return 'John'
    return ''

setOffAlarms(alertForCriminals(['Dan','Don']))