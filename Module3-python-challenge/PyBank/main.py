import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

with open(budget_csv) as budget:
    csv_reader = csv.reader(budget,delimiter=",")
    csv_header = next(budget)
   
    NoMonths = []
    TotalProfit = []
    MonthlyChange = []

    for row in csv_reader:
        NoMonths.append(row[0])
        TotalProfit.append(int(row[1]))
    
    for i in range(len(TotalProfit)-1):
        MonthlyChange.append(TotalProfit[i+1]-TotalProfit[i])

    MaxIncrease = max(MonthlyChange)
    MaxIncMonth = MonthlyChange.index(max(MonthlyChange))+1
    MaxDecrease = min(MonthlyChange)
    MaxDecMonth = MonthlyChange.index(min(MonthlyChange))+1

    print("Financial Analysis")
    print("----------------------")
    print(f"Total number of months: {len(NoMonths)}")
    print(f"Net Total Profit/Loss: ${sum(TotalProfit)}")
    print(f"Average change in profit/loss: ${round(sum(MonthlyChange)/len(MonthlyChange),2)}")
    print(f"Greatest increase in profits: {NoMonths[MaxIncMonth]} (${MaxIncrease})")
    print(f"Greatest decrease in profits: {NoMonths[MaxDecMonth]} (${MaxDecrease})")

filepath = os.path.join("Analysis","AnalysisResults.txt")
with open(filepath,"w") as textfile:
    print("Financial Analysis", file=textfile)
    print("----------------------", file=textfile)
    print(f"Total number of months: {len(NoMonths)}", file=textfile)
    print(f"Net Total Profit/Loss: ${sum(TotalProfit)}", file=textfile)
    print(f"Average change in profit/loss: ${round(sum(MonthlyChange)/len(MonthlyChange),2)}", file=textfile)
    print(f"Greatest increase in profits: {NoMonths[MaxIncMonth]} (${MaxIncrease})", file=textfile)
    print(f"Greatest decrease in profits: {NoMonths[MaxDecMonth]} (${MaxDecrease})", file=textfile)
