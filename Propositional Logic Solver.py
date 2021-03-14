from sys import stdin

def resolve(a,b):
    negar= [element * -1 for element in b]
    literalsOverlap = set(a) & set(negar)
    if len(literalsOverlap)==1:
        r = (set(a)-literalsOverlap)|set(b)-set([element * -1 for element in list(literalsOverlap)])
        return list(r)
    return None



def prsolver(clauses):
    new=[]
    while True:
        for i in range(len(clauses)):
            for j in range(i+1,len(clauses)):
                resolvents=resolve(clauses[i],clauses[j])
                if resolvents==None:
                    continue
                if resolvents==[]:
                    print(True)
                    return
                if resolvents not in new:
                    new.append(resolvents)

        #checking subset
        count=0
        for z in new:
            if z in clauses:
                count+=1

        if count==len(new):
            print(False)
            return
        for z in new:
            clauses.append(z)

#clauses=[[2, -1], [1, 3, -2], [-2], [1]]
clauses=[]
lines=stdin.readlines()
for i in range(len(lines)):
    if lines[i][0]!='c' and lines[i][0]!='p':
         clauses.append(list(map(int,lines[i].split()))[0:-1])

prsolver(clauses)
