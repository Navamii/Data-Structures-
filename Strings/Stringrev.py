# s1 = 'Hello world'
# print(s1[::-1])


#Second solution#

s1 = input()
list1 = []
for i in range((len(s1)-1), -1, -1):
    list1.append(s1[i])
print(''.join(list1))
