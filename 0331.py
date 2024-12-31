s = input() 
a, b = map(int, input().split()) 


hours = int(s[:2])
minutes = int(s[3:])

hours += a

minutes += b

if minutes >= 60:
    hours += minutes // 60  
    minutes = minutes % 60 

#
hours = hours % 24 

print(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}")
