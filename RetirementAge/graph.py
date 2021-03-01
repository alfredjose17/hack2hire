import matplotlib.pyplot as plt
import numpy as np

def graph1():
    salary = int(input("Enter Annual Salary:"))
    age = int(input("Enter Age:"))
    savList = [85]

    for k in range(10, 100, 10):
        savings = salary*k/100
        expenses = salary - savings
        netWorth = 0
        x = savings
        res = 0
        temp = expenses
        for i in range(age+1, 85):
            expenses = expenses*1.06
            salary = salary*1.06
            savings = salary - expenses
            #print(f"----{x}----")
            xtemp = x
            etemp = expenses
            for j in range(i+1, 87):
                etemp *= 1.06
                xtemp -= etemp
                xtemp *= 1.1
                # print(xtemp)
            #print("/")
            if xtemp >= 0:
                #print("**")
                res = i
                break
            x = x*1.1 + savings
        savList.append(res-1)

    savList.append(age)
    # print(savList)
    arr = [0,10,20,30,40,50,60,70,80,90,100]
    xpoints = np.array(arr)
    ypoints = np.array(savList)

    plt.plot(xpoints, ypoints,marker = 'o')
    plt.title("Savings rate vs Retirement rate")
    plt.grid()
    # plt.xlabel("Savings rate")
    # plt.ylabel("Retirement age")
    plt.show()


def graph2():
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
        netFlow = []
        for i in range(age+1, 85):
            expenses = expenses*1.06
            salary = salary*1.06
            savings = salary - expenses
            #print(f"----{x}----")
            netFlow.append(x)

            xtemp = x
            etemp = expenses
            tempList = []
            for j in range(i+1, 86):
                etemp *= 1.06
                xtemp -= etemp
                xtemp *= 1.1
                tempList.append(xtemp)
            #print("/")
            if xtemp >= 0:
                #print("**")
                #res = i
                netFlow += tempList
                break

            x = x*1.1 + savings

    # for i in range(len(netFlow)):
    #     print(f'{i}: {netFlow[i]}')

    arr = []
    for i in range(21,81):
        arr.append(i)

    xpoints = np.array(arr)
    ypoints = np.array(netFlow)

    plt.plot(xpoints, ypoints)
    plt.title("Cash flow net worth @ 30"+ "%"+ " Savings rate")
    plt.grid(axis = 'y')
    plt.show()

print(graph1())
print(graph2())
