#importing statistics for mean,median,mode
import statistics
#for generating 25 random numbers 
import random
def find_mean_mode_median(list1):
#mean of the list1
    mean1=statistics.mean(list1)
#median of the list1
    median1=statistics.median(list1)
#mode of the list1
    mode1=statistics.mode(list1)
    print("mean is ",mean1)
    print("median is ",median1)
    print("mode is",mode1)
#for generating 25 random numbers 
list1=random.choices(range(1,10),k=25)
print(list1)
find_mean_mode_median(list1)
