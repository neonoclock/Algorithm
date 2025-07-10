HM = input()
H,M = map(int, HM.split())

if M >=45 :
    M = M-45
else:
    M=M+15
    H=H-1
    if H<0:
        H=23
        
print(H, M)