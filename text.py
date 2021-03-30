def revword(word):
    return word[::-1].lower()


def countword():
    count=1
    tx= open('text.txt','r')
    tx=tx.read()
    tx=tx.replace('\n',' ') 
    tx=(tx.lower())
    w=tx.split()
    for i in range(1,len(w)):
        if w[0]==revword(w[i]):
           count = count + 1 
    return count
countword()
