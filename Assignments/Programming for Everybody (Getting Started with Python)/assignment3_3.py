s = (input("Enter Score: "))
try:
    score = float(s)
    if(score >= 0.0 and score <= 1.0):
         x = 1
except:
    print('please enter valid number between 0.0 to 1.0')
    quit()

if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')
