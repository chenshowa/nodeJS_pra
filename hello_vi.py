a=0
b=0
c=0
for filename in url:
  if(filename[-5:]=="a.txt"):
    a+=1
  if(filename[-5:]=="b.txt"):
    b+=1
  if(filename[-5:]=="c.jpg"):
    c+=1
print("a.txt "+str(a))
print("b.txt "+str(b))
print("c.jpg "+str(c))

