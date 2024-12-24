s = input()

sm1 = 0
sm2 = 0
for i in range(3):

    sm1+=int(s[i])
    sm2+=int(s[i-3])
    


print("YES" if sm1 == sm2 else "NO")