l1= [1,2,3,4,5,6]
'''for i in l1:
    sq=i**2
    print(sq)
    l2.append(sq)
print(l2)
l2=[i*i for i in l1]
print(l2)'''
l2=[i for i in l1 if i%2==0]
print(l2)





