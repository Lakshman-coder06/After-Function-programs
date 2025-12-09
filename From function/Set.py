A={1,2,3,4,3,2,1,4}
print(A)
B={}
print(type(B))
C=set({})
print(type(C))
D=set({})
D.add(2)
D.add(7)
D.add(6)
D.add(4)
D.add(5)
D.add(7)

for r in D:
    print(r)
if 9 in D:
    print("5 is Set D")
else:
    print("not in Set D")

print(D.pop())
print(D)

D.discard(8)
print(D)

D.clear()
print(D)

s1={5,4,6,3,9,4}
s2={8,4,9,7,1,2}
print(s1.union(s2))
print(s1.intersection(s2))

#copy a set
'''s3=s2
s3.add(10)
print(s3)
print(s2)   if we run this code means same output will come for both s2 and s3
because of the memory location s3 take a memory of s2 '''
s3=s2.copy()
s3.add(10)
print(s3)
print(s2) 
