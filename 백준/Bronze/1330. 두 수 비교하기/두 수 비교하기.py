AB = input()
A,B = map(int,AB.split())

if (A>B):
    print(">")
elif (A<B):
    print("<")
elif (A==B):
    print("==")