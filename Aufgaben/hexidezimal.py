
h=[]
v=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
y=input("gib die selbe zahl z nochmal ein")
print"Deine Zahl im Hexadezimalsystem ist:"
while y >0:
    rest= y % 16
    t =v[rest]
    h.append(t)
    y=y//16
res= h[::-1]
print res