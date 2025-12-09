a=open("Festival.txt","r")
print(a.readlines())

'''
print(a.readline()) if we run program with this first it returns first element of the file
print(a.readline()) if we run program with same line again it returns second element of the file

'''
print(a.readable())

print(a.read())

a.close()
