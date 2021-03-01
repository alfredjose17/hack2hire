salary = int(input("Enter Annual Salary:"))
age = int(input("Enter Age:"))
savings = int(input("Enter Annual Savings:"))

if savings == 0:
    print(f'Optimal Retirement Age: 85')

elif savings == salary:
    print(f'Optimal Retirement Age: {age}')
    
else:
    expenses = salary - savings
    life = 85

    netWorth = 0
    x = savings
    res = 0
    temp = expenses
    for i in range(age+1, 85):
        expenses = expenses*1.06
        salary = salary*1.06
        savings = salary - expenses
        #print(f"----{x}----")
        #print(i)

        xtemp = x
        etemp = expenses
        for j in range(i+1, 87):
            etemp *= 1.06
            xtemp -= etemp
            xtemp *= 1.1
            #print(xtemp)
        #print("/")
        if xtemp >= 0:
            #print("****")
            res = i
            break

        x = x*1.1 + savings

    print(f'Optimal Retirement Age: {res-1}')
