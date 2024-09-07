mtrx = [[1,2,3,4,5,6,],
        [7,8,9,10,11,12],
        [13,14,15,16,17,18],
        [19,20,21,22,23,24],
        [25,26,27,28,29,30],
        [31,32,33,34,35,36]]
mtrx1 = []
mas = []
mas1 = []
for i in range(len(mtrx)):
    mas+=mtrx[i][i+1:]
    mas1+=mtrx[i][:i+1]
mas2 = mas+mas1
mas2[mas1.index(max(mas1))+15], mas2[mas.index(max(mas))] = mas2[mas.index(max(mas))], mas2[mas1.index(max(mas1))+15]
mas = mas2[:15]
mas1 = mas2[15:]
n=5
c=0
m = 1
a = 1
g = 0
for i in range(6):
    mtrx1.append(mas1[g:i+m]+mas[c:n])
    c=n
    m+=a
    a+=1
    n+=4-i
    g=m-1
print(mtrx1)