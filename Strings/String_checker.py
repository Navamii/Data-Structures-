

#op = True
# inp = +91 9035800105

#op = False
#inp = +919035800105

s1 = input()
l1 = s1.split()
if l1[0] == '+91' and len(l1[1]) == 10:
    print('True')
else:
    print('False')
