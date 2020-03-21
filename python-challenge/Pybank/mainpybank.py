import csv

f= open ('budget_data.csv') 

csv_f =csv.reader(f,delimiter=',')

#Take the header off

header = next(csv_f)

#open my text file to write to

fo= open('budget.txt','a')

#Set the variable and lists I will be working with
dates =[]
money=[]
Avg=int
Diff=int

#Begin writing to the txt file

fo.write('Financial Analysis \n')
fo.write('------------------ \n')



#Start a for loop to cycle through all the values in lists
for row in csv_f:

#Append the rows I will be working with
  dates.append(row[0])
  money.append(int(row[1]))

#Find and print month total using len and write
Total_months= len(dates)
fo.write('Total Months:')
fo.write(f'{Total_months}\n')

#Find and print month sum using sum and write
fo.write('Total:')
Total = sum(money)
fo.write ('${}'.format (f'{Total}\n'))

#Find and print average change using list with operator
fo.write('Average Change:')
import operator
test_list=money
#Checking my work as I go: print(str(test_list))
res=list(map(operator.sub,test_list[1:],test_list[:-1]))
#Checking my work as I go: print(str(res))
Diff=res
AvgDiff=(sum (res)/len (res))
fo.write('${0:.2f}'.format (AvgDiff))

#Calculate the max and min using max and min functions
Max1= max (Diff)
#print (Max1)
Min2= min(Diff)
#print (Min2) 

#Using the index function find date where the max, min were in adjacent list
A=Diff.index(Max1)+1
B=Diff.index(Min2)+1

#print(dates[A],dates[B])

#Write the date & increase
fo.write('\n Greatest Increase in Profits: \n')

fo.write(f'{dates[A]}' '   ${0}'.format (Max1))

#Write the date and decrease
fo.write('\n Greatest Decrease in Profits: \n')

fo.write(f'{dates[B]}' '   ${0}'.format (Min2))

#close out the txt file then close out the csv

fo.close()

f.close()









