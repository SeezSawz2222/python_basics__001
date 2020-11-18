A=int(input())
B=int(input())
C=int(input())
L=[]
AB=((A+B)+abs(A-B))/2
L.append(AB)
BC=((B+C)+abs(B-C))/2
L.append(BC)
AC=((A+C)+abs(A-C))/2
L.append(AC)
D=max(L)
print(int(D),"eh o maior")
