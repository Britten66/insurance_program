#Author Christopher Britten - SD 15 
#Date 07-22-2025
#Desc: This Program allows the insurance comany to enter
#and process new insurance policies for customers.
#The program gathers peronal and coverage information. 
#calculated the premium, taxed and monthly payment. 

#The Program Will store the fata in a file for future referall 

#=================
# Here are imports 
#=================


#=================
# Here are CONSTANTS
#=================

f = open('Policies.dat', 'r')
HST_RATE = float(f.readline())
f.close()


#=================
# Here are Calculations 
#=================
