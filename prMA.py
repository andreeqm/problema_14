matrice=[]
n=int(input("Dimensiunea matricei de la 2 pana la 10: "))
if n>=2 and n<=10:
    for i in range(0,n):
        a=int(input("Elementele sunt: "))
        for j in range(0,n):
            matrice.append(a[i][j])
print(matrice)
#dp-diagonala principala
dp=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i==j:
            dp.append(matrice[i][j])
print("Suma diagonalei principale este= ",sum(dp))
#ds-diagonala secundara
ds=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i+j==n-1:
            ds.append(matrice[i][j])
print("Suma diagonalei secundare este= ",sum(ds))
#msddp-mai sus de diagonala principala
msddp=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i-j<0:
            msddp.append(matrice[i][j])
print("Suma diagonalei mai sus de diagonala principala este=",sum(msddp))
#mjddp-mai jos de diagonala principala
mjddp=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i-j>0:
            ds.append(matrice[i][j])
print("Suma diagonalei mai jos de diagonala principala este=",sum(mjddp))
#msdds-mai sus de diagonala secundara
msdds=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i+j<n-1:
            ds.append(matrice[i][j])
print("Suma diagonalei mai sus de diagonala secundara este= ",sum(msdds))
#mjdds-mai jos de diagonala secundara
mjdds=[]
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i+j>n-1:
            ds.append(matrice[i][j])
print("Suma diagonalei mai jos de diagonala secundara este= ",sum(mjdds))
