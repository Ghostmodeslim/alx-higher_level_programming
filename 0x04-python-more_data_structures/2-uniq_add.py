#!/usr/bin/python3
def uniq_add(my_list=[]):
unique_numbers = 0
for i in set(my_list):
unique_numbers += i
return(unique_numbers)
