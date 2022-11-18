n=int(input())
for i in range (n):
    p=int(input())
    s=input()
    if s[:p//2]==s[p//2:]:
        print("yes")
    else:
        print("No")