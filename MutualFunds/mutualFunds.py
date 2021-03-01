import csv
import statistics
import math
import numpy
def data1():
    with open('D:\ew_data1.csv','rt')as f:
        data = csv.reader(f)
        ans=[]
        monthlyreturn = []
        for row in data:
            ans.append([row[0],float(row[1])])
        for i in range(len(ans)-1):
            curmonth,prevmonth = ans[i][1], ans[i+1][1]
            calc = ((curmonth-prevmonth)/prevmonth)*100
            monthlyreturn.append(calc)
        # for i in monthlyreturn:
        #     print(i)
        temp_mr = [1 + (x/100) for x in monthlyreturn]
        # # print(temp_mr)
        
        mr_tot= float(numpy.prod(temp_mr))
        # mr_tot = abs(mr_tot)

        annual_return =  ((mr_tot ** (1/7) )- 1 )  *100
        # # print(annual_return)
        risk_free_rate = 6/100
        
        sharpe_ratio = (annual_return - risk_free_rate) / ( statistics.stdev(monthlyreturn)* math.sqrt(12))
        # ans=1
        # for i in monthlyreturn:
        #     ans *= (1+(i*0.01))

        # annual_return = ((ans ** 1/7)-1)*100
        # sharpe_ratio = (annual_return - risk_free_rate) / ( statistics.stdev(monthlyreturn)* math.sqrt(84))
        return sharpe_ratio
    
def data2():
    with open('D:\ew_data2.csv','rt')as f:
        data = csv.reader(f)
        ans=[]
        monthlyreturn = []
        for row in data:
            ans.append([row[0],float(row[1])])
        for i in range(len(ans)-1):
            curmonth,prevmonth = ans[i][1], ans[i+1][1]
            calc = ((curmonth-prevmonth)/prevmonth)*100
            monthlyreturn.append(calc)
        # for i in monthlyreturn:
        #     print(i)
        return sum(monthlyreturn)
        # for i in monthlyreturn:
        #     print(i)
        temp_mr = [1 + (x/100) for x in monthlyreturn]
        # # print(temp_mr)
        
        mr_tot= float(numpy.prod(temp_mr))
        # mr_tot = abs(mr_tot)

        annual_return =  ((mr_tot ** (1/7) )- 1 )  *100
        # # print(annual_return)
        risk_free_rate = 6/100
        
        sharpe_ratio = (annual_return - risk_free_rate) / ( statistics.stdev(monthlyreturn)* math.sqrt(12))
        # ans=1
        # for i in monthlyreturn:
        #     ans *= (1+(i*0.01))

        # annual_return = ((ans ** 1/7)-1)*100
        # sharpe_ratio = (annual_return - risk_free_rate) / ( statistics.stdev(monthlyreturn)* math.sqrt(84))
        return sharpe_ratio

def data3():
    with open('D:\ew_data3.csv','rt')as f:
        data = csv.reader(f)
        ans=[]
        monthlyreturn = []
        for row in data:
            ans.append([row[0],float(row[1])])
        for i in range(len(ans)-1):
            curmonth,prevmonth = ans[i][1], ans[i+1][1]
            calc = ((curmonth-prevmonth)/prevmonth)*100
            monthlyreturn.append(calc)
        # for i in monthlyreturn:
        #     print(i)
        return sum(monthlyreturn)
        # for i in monthlyreturn:
        #     print(i)
        temp_mr = [1 + (x/100) for x in monthlyreturn]
        # # print(temp_mr)
        
        mr_tot= float(numpy.prod(temp_mr))
        # mr_tot = abs(mr_tot)

        annual_return =  ((mr_tot ** (1/7) )- 1 )  *100
        # # print(annual_return)
        risk_free_rate = 6/100
        
        sharpe_ratio = (annual_return - risk_free_rate) / ( statistics.stdev(monthlyreturn)* math.sqrt(12))
        # ans=1
        # for i in monthlyreturn:
        #     ans *= (1+(i*0.01))

        # annual_return = ((ans ** 1/7)-1)*100
        # sharpe_ratio = (annual_return - risk_free_rate) / ( statistics.stdev(monthlyreturn)* math.sqrt(84))
        return sharpe_ratio

def data4():
    with open('D:\ew_data4.csv','rt')as f:
        data = csv.reader(f)
        ans=[]
        monthlyreturn = []
        for row in data:
            ans.append([row[0],float(row[1])])
        for i in range(len(ans)-1):
            curmonth,prevmonth = ans[i][1], ans[i+1][1]
            calc = ((curmonth-prevmonth)/prevmonth)*100
            monthlyreturn.append(calc)
        # for i in monthlyreturn:
        #     print(i)
        return sum(monthlyreturn)
        # for i in monthlyreturn:
        #     print(i)
        temp_mr = [1 + (x/100) for x in monthlyreturn]
        # # print(temp_mr)
        
        mr_tot= float(numpy.prod(temp_mr))
        # mr_tot = abs(mr_tot)

        annual_return =  ((mr_tot ** (1/7) )- 1 )  *100
        # # print(annual_return)
        risk_free_rate = 6/100
        
        sharpe_ratio = (annual_return - risk_free_rate) / ( statistics.stdev(monthlyreturn)* math.sqrt(12))
        # ans=1
        # for i in monthlyreturn:
        #     ans *= (1+(i*0.01))

        # annual_return = ((ans ** 1/7)-1)*100
        # sharpe_ratio = (annual_return - risk_free_rate) / ( statistics.stdev(monthlyreturn)* math.sqrt(84))
        return sharpe_ratio

def data5():
    with open('D:\ew_data5.csv','rt')as f:
        data = csv.reader(f)
        ans=[]
        monthlyreturn = []
        for row in data:
            ans.append([row[0],float(row[1])])
        for i in range(len(ans)-1):
            curmonth,prevmonth = ans[i][1], ans[i+1][1]
            calc = ((curmonth-prevmonth)/prevmonth)*100
            monthlyreturn.append(calc)
        # for i in monthlyreturn:
        #     print(i)
        return sum(monthlyreturn)
        # for i in monthlyreturn:
        #     print(i)
        temp_mr = [1 + (x/100) for x in monthlyreturn]
        # # print(temp_mr)
        
        mr_tot= float(numpy.prod(temp_mr))
        # mr_tot = abs(mr_tot)

        annual_return =  ((mr_tot ** (1/7) )- 1 )  *100
        # # print(annual_return)
        risk_free_rate = 6/100
        
        sharpe_ratio = (annual_return - risk_free_rate) / ( statistics.stdev(monthlyreturn)* math.sqrt(12))
        # ans=1
        # for i in monthlyreturn:
        #     ans *= (1+(i*0.01))

        # annual_return = ((ans ** 1/7)-1)*100
        # sharpe_ratio = (annual_return - risk_free_rate) / ( statistics.stdev(monthlyreturn)* math.sqrt(84))
        return sharpe_ratio

print(data1())
print(data2())
print(data3())
print(data4())
print(data5())
