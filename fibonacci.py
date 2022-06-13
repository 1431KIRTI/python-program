def fibbo(n):
  if(n<1):
    print("NA")
  elif(n==1):
    print(0)
  elif(n==2):
    print(0,1)
  else:
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n-2):
      c = a + b
      print(c,end=" ")
      a=b
      b=c

n = int(input("Enter n:"))
fibbo(n)
