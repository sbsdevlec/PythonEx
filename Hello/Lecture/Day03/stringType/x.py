l=[(1,2),(3,4)]
s=""
for t in l:
    s += "(%s,%s)," % t
s = s[:-1]
print(s, type(s))

l=(1,2,3,4,5,6,7,8,9,0)
s=""
for t in l:
    s += "%s" % t
print(s, type(s))
print("/".join(s))