import os 
os.system("cls")

spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low=0
high=0
normal=0

for month in spendings:
    if month < 1000:
        low +=1
    elif month <=2500:
        normal +=1
    else:
        high +=1
print('Number of months with low spendings: ', + str(low) + ', Normal spendings: ', + str(normal) + ', High spendings: ' + str(high) + '.')
