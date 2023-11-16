import csv 
filepath = 'PyBank/Resources/budget_data.csv'
months = [] #Empty lists for storing the months in the csv file 
profitloss = [] #Empty lists for storing the profits and losses in the csv file
with open (filepath) as csvfile: 
    csvreader=csv.reader(csvfile, delimiter=',') #creating variable that holds the content
    header=next(csvreader) #storing the header row
    for row in csvreader:
        months.append(row[0]) #storing the months contents to the empty list
        profitloss.append(row[1]) #storing the profit and loss contents to the empty list
    totalmonths= len(months)  #The total number of months included in the dataset
    plcount = len(profitloss)
    totalpl = 0
    total_change = 0
    monthly_change=0 
    greatest_increase = 0
    greatest_decrease = 0
    for i in range(plcount):
        totalpl = totalpl + int(profitloss[i])  # The net total amount of "Profit/Losses" over the entire period
    for pro_loss1, pro_loss2 in zip(profitloss, profitloss[1:]): #using a zip function to use two iterables 
        monthly_change = float(pro_loss2) - float(pro_loss1) #calculating the monthly change
        total_change = total_change+ monthly_change

        if monthly_change > greatest_increase: #if the monthly change is larger than the month before then 
            greatest_increase = monthly_change #store the month
            greatest_inc_month = months[profitloss.index(pro_loss2)]
            greatest_inc_value = monthly_change #store the profit and loss 

        if monthly_change < greatest_decrease: #if the monthly change is smaller than the month before then 
            greatest_decrease = monthly_change #store the month
            greatest_dec_month = months[profitloss.index(pro_loss2)]
            greatest_dec_value = monthly_change #store the profit and loss 
            
    average_change = total_change/(plcount-1) #calculating the average change
 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${totalpl}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc_value})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec_value})")

output_file = 'PyBank/Analysis/pyBank.txt' #writing to an empty txt file
with open(output_file,"w",newline= '') as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write('----------------------------\n')
    datafile.write(f"Total Months: {totalmonths}\n")
    datafile.write(f"Total: ${totalpl}\n")
    datafile.write(f"Average Change: ${round(average_change,2)}\n")
    datafile.write(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc_value})\n")
    datafile.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec_value})\n")

