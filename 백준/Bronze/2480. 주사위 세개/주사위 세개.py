score = input()
A,B,C = map(int, score.split())

if (A==B==C):
    prize = 10000+A*1000
elif (A==B or A==C):
    prize = 1000 + A * 100
elif (B==C):
    prize = 1000 + B * 100
else:
    prize = max(A, B, C) * 100
      
print(prize)