x11=int(input())
if x11>=-2**15+1 and x11<=2**15+1:
    print("INT")
elif x11>=-2**31+1 and x11<=2**31+1:
    print("LONG")
else:
    print("LONG LONG")
