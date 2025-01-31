s1 = 'hello'
s2 = 'world'
print(s1 + ' ' + s2)
print(s1, 'hello')
print(3*s2)
print(int(10/2)*s1)
print(s1, len(s1))
print(3*s2, len(3*s2))
for c in s2:
    print(c)

s3 = ''
for c in s1:
    s3 += c*4
print(s3)

for c in s1:
    print(c*4, end='')

print('h' in s1)
print('d' in s2)
print('x' in s1)
print('wor' in s2)