d = int(input('enter the number of days: '))
dic = {'E' : 1, 'M' : 2, 'H' : 3}
erica = list( )
bob = list( )
def lulu(nam):
    for i in range(d):
        diffi = input("enter the difficulty on {0}th day: ".format(i))
        nam.append(diffi)
lulu(erica)
lulu(bob)
print(erica)
print(bob)
nerica=list( )
nbob=list( )
def nun(lik, yak):
    for x in lik:
        yak.append(dic[x])
nun(erica, nerica)
nun(bob, nbob)
se = sum(nerica)
sb = sum(nbob)
print(se)
print(sb)
if (se == sb):
    print("tie")
elif (se > sb):
    print("erica wins")
else:
    print("bob wins")