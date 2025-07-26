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
import datetime
import os
import FormatValues as FV

#=================
# Here are CONSTANTS
#=================

with open('Policies.dat', 'r') as f:
 
 POLNUM = int(f.readline())
 
 PROCFEE = float(f.readline()) 

 HST_RATE = float(f.readline())          

 BASICPREM = float(f.readline())

 DISCOUNT = float(f.readline())

 LIAB = float(f.readline())

 GLASS = float(f.readline()) 

 LOANER = float(f.readline())

#=================
# Here are Inputs
#=================

VALID_PROVINCES = ["NL", "NS", "NB", "PE", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

VALID_PAYMENT_TYPE = {"Full", "Monthly","Down Pay"}

print(" ======= New Insurance Policy ======== ")

Fname = input ("Enter Your First Name : ").title()
Lname = input("Enter Your Last Name : ").title()
Address = input("Enter Your Address : ").title()
City = input("Enter Your City : ").title()


while True: 

   Prov = input("Enter Province ( X,X ) ").upper()
   if Prov in VALID_PAYMENT_TYPE:
      break
   else:
      print("Invalid province. Please enter a valid 2-letter code. ")


   Postal = input("Enter Postal Code (Ex) X9X 9X9 : ")
   Phone = input("Enter Phone Number (10 digit): ")
   PolicyDate = datetime.datetime.now().strftime("%Y-%m-%d")

   NumCars = input("Enter Number of cars youd like to insure: ")

   Extra_Li = input("Would you like to add Extra Liability (Y/N) ")
   GlassCover = input("Add Glass Coverage ? : (Y?N) ")
   LoanerCar = input("Do you require a loaner car? (Y/N) : ")
   
   while True:
      PayType = input("Enter Your Payment Type: (FULL / MONTHLY / DOWN PAY )").title()
      if PayType in VALID_PAYMENT_TYPE:
         break
      else:
         print("Invalid Pay Type. Try Again")




#=================
# Here are Calculations
#=================

#Base Prem Calculations 

InsurancePrem = BASICPREM * NumCars 

#Discount for additional cars after first one 

if NumCars > 1:
   InsurancePrem -= (BASICPREM * DISCOUNT) * (NumCars - 1)

   #Calculate Cost Of Option Costs 

   ExtraCost = 0 

   # Cost Will start at 0 for this variable 

   if Extra_Li:
      ExtraCost += LIAB * NumCars # This was tricky... cost applies per car 
   if GlassCover:
      Extra =+ GLASS * NumCars
   if LoanerCar:
      ExtraCost += LOANER * NumCars # loaner Car covereage 

   
   #Adding up insurance and optional cost 
   TotalPrem = InsurancePrem + ExtraCost

   #Tax calc here 
   HST = TotalPrem * HST_RATE

   #Adding tax to total 
   TotalCost = TotalPrem * HST 

   #Monnth Pay will only apply if the customer types " Monthly "
   if PayType == "Monthly":
      #Over 8 months 
    MonthlyPayment = (TotalCost + PROCFEE) / 8 
   else:
      MonthlyPayment = 0 # if not appliciable for full / down pay 

      

#=================
# Here are Output
#=================


print("===================Poicy Summary=======================")

print(f" Policy #:                                        ",  POLNUM)
print(f" Customer Name :                                  ",  Fname , Lname)
print(f" Address :                                        ",  Address + ",", City + ",", Prov + ",", Postal )
print(f" Phone :                                          ",  Phone)
print(f" Policy Date :                                    ",  PolicyDate )
print(f" Number Of Cars :                                 ",  NumCars )
print(f" Extra Liability :                                {----}")
print(f" Glass Coverage :                                 {----}")
print(f" Loaner Car Coverage :                            {----}")
print(f" Payment Type :                                   ",  PayType )
print(f" Total Premium :                                  ",  TotalPrem )
print(f" HST :                                            ",  HST )
print(f" Total Cost :                                     ",  TotalCost )



if PayType == "Monthly":
   print(f"Monthly Payment (8x) : {{FV.FDollarr2{MonthlyPayment}")
 



#=================
# Housekeeping 
#=================


 







#=================
# Here are Outputs
#=================

with open('Policies.dat', 'w') as f:
    f.write(f"{POLNUM}\n")
    f.write(f"{PROCFEE}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{BASICPREM}\n")
    f.write(f"{DISCOUNT}\n")
    f.write(f"{LIAB}\n")
    f.write(f"{GLASS}\n")
    f.write(f"{LOANER}\n")
    
