



def tri(L) :
    Lt=[]
    for i in range(len(L)):
        if Lt==[]:
            Lt=[L[i]]
        else :

            if Lt[0]>= L[i]:
                Lt = [L[i]] + Lt
            else:
                if i == 1:
                    Lt=Lt + [L[i]]
                else:
                    for j in range(i-1) :
                        #print(j)
                        #print(len(Lt), i)
                        if Lt[j+1]>=L[i] and Lt[j]<L[i]:
                            Lt.insert(j+1,L[i])
                    #print(len(Lt),i)
                    if Lt[i-1] < L[i] :
                        Lt.append(L[i])
                    if len(Lt)!=(i+1) :
                        print("erreur" , Lt[i-2] , L[i])
                        print("erreur", Lt[i - 3], L[i-1])
                        print(len(Lt), i)
                        print(Lt)
                        break
    return (Lt)

def tribulle(L) :
    #global(L)
    for i in range(len(L)) :
        min=i
        for j in range(len(L)-i) :
            if L[min]>L[j+i] :
                min=j+i
        a,b=L[i], L[min]
        L[i] , L[min] = a , b
    return(L)

def heron (N,e=1) :
    a=1
    b=N
    while b-a> e :
        b=(a+b)/2
        a=N/b
    return((b+a)/2)