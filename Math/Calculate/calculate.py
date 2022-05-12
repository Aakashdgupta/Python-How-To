
def mean(*args):
    if type(args[0])==type([]):
        n = args[0]
        return sum(n)/len(n)
    return sum(args)/len(args)
