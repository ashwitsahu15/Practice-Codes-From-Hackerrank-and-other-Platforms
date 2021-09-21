def remdup(l) :
    ans=l[:]
    for i in range(len(l)) :
        if l[i] in l[i+1:] :
            ans.remove(l[i])
    return ans

def splitsum(l):
  pos=0
  neg=0
  for v in l:
    if v >0:
      pos=pos+v*v
    if v< 0:
      neg=neg+v*v*v
  return ([pos,neg])

def matrixflip(m,d):
  H=[]
  if d=='h':
    for r in m:
      hr=[]
      for row in range(1,len(r)+1):
        hr.append(r[-row])
      H.append(hr)
    return(H) 
  if d=='v':
    V=[]
    for vr in range(1,len(m)+1):
      V.append(m[-vr])
    return(V)