###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #
import pandas as pd
path = ''
df =  pd.read_csv(path + "covid.csv", sep = ',')
df.head()
Deaths500_total = 0
Deaths500_count = 0
Deaths1000_total = 0
Deaths1000_count = 0
Deaths5000_total = 0
Deaths5000_count = 0
Confirmed500_total = 0
Confirmed500_count = 0
Confirmed1000_total = 0
Confirmed1000_count = 0
Confirmed5000_total = 0
Confirmed5000_count = 0
for row in df.iterrows():
    print(row[1]['Country'])
    if row[1]['Active'] > 500:
        Deaths500_total = Deaths500_total + row[1]['Deaths']
        Deaths500_count = Deaths500_count + 1
        Confirmed500_total = Confirmed500_total + row[1]['Confirmed']
        Confirmed500_count = Confirmed500_count + 1
    if row[1]['Active'] > 1000:
        Deaths1000_total = Deaths1000_total + row[1]['Deaths']
        Deaths1000_count = Deaths1000_count + 1
        Confirmed1000_total = Confirmed1000_total + row[1]['Confirmed']
        Confirmed1000_count = Confirmed1000_count + 1
    if row[1]['Active'] > 5000:
        Deaths5000_total = Deaths5000_total + row[1]['Deaths']
        Deaths5000_count = Deaths5000_count + 1
        Confirmed5000_total = Confirmed5000_total + row[1]['Confirmed']
        Confirmed5000_count = Confirmed5000_count + 1
print("average of death among those countries that have more than 500 active cases is :"+str(Deaths500_total/Deaths500_count))
print("average of confirmed among those countries that have more than 500 active cases is :"+str(Confirmed500_total/Confirmed500_count))
print("average of death among those countries that have more than 1000 active cases is :"+str(Deaths1000_total/Deaths1000_count))
print("average of confirmed among those countries that have more than 1000 active cases is :"+str(Confirmed1000_total/Confirmed1000_count))
print("average of death among those countries that have more than 5000 active cases is :"+str(Deaths5000_total/Deaths5000_count))
print("average of confirmed among those countries that have more than 5000 active cases is :"+str(Confirmed5000_total/Confirmed5000_count))

