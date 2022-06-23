
def mean(*args):
    if type(args[0])==type([]):
        n = args[0]
        return sum(n)/len(n)
    return sum(args)/len(args)

def median(*args):
    if type(args[0])==type([]):
        n = args[0]
    else:
        n =list(args)
    
    n = sorted(n)
    length =len(n)

    if length%2==0:
            return (n[length//2-1] + n[length//2])/2    
    return n[length//2]

def mode(*args):
    if type(args[0])==type([]):
        n = args[0]
    else:
        n =list(args)
    

    frequency ={}
    for i in n:
        if i in frequency.keys() :pass
        else : frequency[i] =0

    for i in n:
        if i in frequency.keys():
            frequency[i] += 1
    
    freq=max(frequency.values())
    for k , v in frequency.items():
        if v ==freq: return k

     

    




