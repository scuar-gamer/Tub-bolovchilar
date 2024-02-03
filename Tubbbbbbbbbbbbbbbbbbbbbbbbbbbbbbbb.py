n=int(input())
s=[]
i=2
while i*i <= n:
    while n%i < 1:
        s.append(i)
        n /= i
    i += 1
if n>1:
    s.append(i)
print(*s)
