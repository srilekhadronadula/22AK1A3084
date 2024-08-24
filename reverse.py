def revese(s):
    words=s.split()
    a=[word[::-1] for word in words]
    newwords=" ".join(a)
    return newwords
r=reverse("my name is srilekha")
print(r)
