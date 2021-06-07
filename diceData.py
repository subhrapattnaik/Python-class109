# we can also draw a distribution using plotly's 
#figure_factory module
#install scipy package

#pip install scipy
#use displot() to draw the distribution graph
#it takes two arguments, --the data, the label

import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics

dice_result=[]
count=[]
#we want to add this 100 times
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    #print(dice1,dice2)
    dice_result.append(dice1+dice2)
    count.append(i)

#y axis can be anystring  ex: "Result" is taken here..
#you can take "abc" or "xyz"
#frequency shows in y axis(out of 1)

mean=sum(dice_result)/len(dice_result)
std_deviation=statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)



print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of data:",std_deviation)


first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]


print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))


fig=ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.show()



#if for loop is for a bigger number like i=1000 ,the graph will be nearly same everytime you run it
#if for loop is for a smaller no like i=10,graph will be different everytime you run it.
