pw = input('Enter your password: ')
s = ''

for i in pw:
    s = s + str(ord(i))
    
print(s)
