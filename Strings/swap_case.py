s1 = input()
#s1 = 'Random acesss'
l1 = s1.split(' ')
l2 = []
for i in l1:
    if i[0].isupper():
        s2 = i[0].lower()+i[1:len(s1)-1]
        l2.append(s2)
    if i[0].islower():
        s2 = i[0].upper()+i[1:len(s1)-1]
        l2.append(s2)
print(' '.join(l2))


# using swapcase function

#s1 = input()
#s1 = 'Random acesss'
#l1 = s1.split(' ')
#l2 = []
# for i in l1:
#   s2 = i[0].swapcase()+i[1:]
#   l2.append(s2)

#print(' '.join(l2))
