# importing Statistics module
import statistics
  
# creating a simple data - set
sample = [1, 2, 3, 4, 5]
  
# Prints standard deviation
# xbar is set to default value of 1
print("Standard Deviation of sample is % s " 
                % (statistics.stdev(sample)))


#______________________________________________________-

# Python code to demonstrate stdev()  
# function on varioius range of datasets
  
# importing the statistics module
from statistics import stdev
  
# importing fractions as parameter values
from fractions import Fraction as fr
  
# creating a varying range of sample sets 
# numbers are spread apart but not very much
sample1 = (1, 2, 5, 4, 8, 9, 12)
  
# tuple of a set of negative integers
sample2 = (-2, -4, -3, -1, -5, -6)
  
# tuple of a set of positive and negative numbers
# data-points are spread apart considerably
sample3 = (-9, -1, -0, 2, 1, 3, 4, 19)
  
# tuple of a set of floating point values
sample4 = (1.23, 1.45, 2.1, 2.2, 1.9)
  
# Print the standard deviation of  
# following sample sets of observations
print("The Standard Deviation of Sample1 is % s" 
                              %(stdev(sample1)))
                                
print("The Standard Deviation of Sample2 is % s" 
                              %(stdev(sample2)))
                                
print("The Standard Deviation of Sample3 is % s" 
                              %(stdev(sample3)))
                                
                                
print("The Standard Deviation of Sample4 is % s" 
                              %(stdev(sample4)))

#-----------------------------------------------------------------
# Python code to demonstrate difference 
# in results of stdev() and variance()
  
# importing Statistics module
import statistics
  
# creating a simple data-set
sample = [1, 2, 3, 4, 5]
  
# Printing standard deviation
# xbar is set to default value of 1
print("Standard Deviation of the sample is % s " 
                    %(statistics.stdev(sample)))
  
# variance is approximately the 
# squared result of what stdev is
print("Variance of the sample is % s" 
     %(statistics.variance(sample)))
#--------------------------------------------------------------------------
# Python code to demonstrate use of xbar
# parameter while using stdev() function
  
# Importing statistics module
import statistics
  
# creating a sample list
sample = (1, 1.3, 1.2, 1.9, 2.5, 2.2)
  
# calculating the mean of sample set
m = statistics.mean(sample)
  
# xbar is nothing but stores 
# the mean of the sample set
  
# calculating the variance of sample set
print("Standard Deviation of Sample set is % s" 
         %(statistics.stdev(sample, xbar = m)))
#--------------------------------------------------------

# Python code to demonstarte StatisticsError
  
# importing the statistics module
import statistics
  
# creating a data-set with one element
sample = [1]
  
# will raise StatisticsError
print(statistics.stdev(sample))
#-------------------------------------------------------
#Standard Deviation is highly essential in the field of statistical maths and statistical study. It is commonly used to measure confidence in statistical calculations. For example, the margin of error in calculating marks of an exam is determined by calculating the expected standard deviation in the results if the same exam were to be conducted multiple times.
#It is very useful in the field of financial studies as well as it helps to determine the margin of profit and loss. The standard deviation is also important, where the standard deviation on the rate of return on an investment is a measure of the volatility of the investment.