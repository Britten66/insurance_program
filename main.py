# Author Christopher Britten - SD 15
# Date 07-22-2025
# Desc: This Program allows the insurance comany to enter
# and process new insurance policies for customers.
# The program gathers peronal and coverage information.
# calculated the premium, taxed and monthly payment.

# The Program Will store the fata in a file for future referall

# =================
# Here are imports
# =================
import time
import datetime
import os
import FormatValues as FV

# =================
# Here are CONSTANTS
# =================

# this is reading the default file
with open("Defaults.dat", "r") as f:

    POLNUM = int(f.readline())
    PROCFEE = float(f.readline())
    HST_RATE = float(f.readline())
    BASICPREM = float(f.readline())
    DISCOUNT = float(f.readline())
    LIAB = float(f.readline())
    GLASS = float(f.readline())
    LOANER = float(f.readline())

while True:
    # =================
    # Here are Inputs
    # =================
    # Clears the screen .
    os.system("cls" if os.name == "nt" else "clear") 

    VALID_PROVINCES = ["NL","NS","NB","PE","QC","ON","MB", "SK", "AB","BC","YT","NT", "NU",]

    VALID_PAYMENT_TYPE = ["Full", "Monthly", "Down Pay"]

    print(" ======= New Insurance Policy ======== ")
    Fname = input("Enter Your First Name : ").title()
    Lname = input("Enter Your Last Name : ").title()
    Address = input("Enter Your Address : ").title()
    City = input("Enter Your City : ").title()

    Postal = input("Enter Postal Code (Ex) X9X 9X9 : ").upper()
    Phone = input("Enter Phone Number (10 digit): ")
    FormattedPhone = FV.format_phone(Phone)
    PolicyDate = datetime.datetime.now().strftime("%Y-%m-%d")

    NumCars = input("Enter Number of cars youd like to insure: ")
    NumCars = int(NumCars)

    Extra_Li = input("Would you like to add Extra Liability (Y/N) ")

    GlassCover = input("Add Glass Coverage ? : (Y/N) ")

    LoanerCar = input("Do you require a loaner car? (Y/N) : ")

 #=====
 # Claim Lists Are Started Here
 #======  

    ClaimNum = []
    ClaimDate = []
    ClaimAmt = []

#======
# PRov validations
#======

    while True:
        Prov = input("Enter Province (XX) ").upper()
        if Prov in VALID_PROVINCES:
            break
        else:
            print("Invalid province. Please enter a valid 2-letter code. ")
#======
# Payment Type Validations Here
#======

    DownPayment = 0
    MonthlyPayment = 0

    while True:
        PayType = input("Enter Your Payment Type: (FULL / MONTHLY / DOWN PAY )").title()
        if PayType in VALID_PAYMENT_TYPE:
            break
        else:
            print("Invalid Pay Type. Try Again")

# =================
# Here are Calculations
# =================

    # Base Prem Calculations

    InsurancePrem = BASICPREM * NumCars

    # Discount for additional cars after first one here

    if NumCars == 1:
        InsurancePrem = BASICPREM
    else:
        InsurancePrem = BASICPREM + (NumCars - 1) * (BASICPREM * (1 - DISCOUNT))

    # Extra Cost Calc Here .. This Starts With 0 Here

    ExtraCost = 0

    # Boolean value will hav eto be validated with y/n value
    Extra_Li = Extra_Li.upper() == "Y"
    GlassCover = GlassCover.upper() == "Y"
    LoanerCar = LoanerCar.upper() == "Y"

    # Extra Cov Cost Validation Here

    if Extra_Li:
        ExtraCost += LIAB * NumCars

    if GlassCover:
        ExtraCost += GLASS * NumCars

    if LoanerCar:
        ExtraCost += LOANER * NumCars

    # ptional cost
    TotalPrem = InsurancePrem + ExtraCost

    # Tax calc here
    HST = TotalPrem * HST_RATE
    TotalCost = TotalPrem + HST

    if PayType == "Down Pay":
        DownPayment = input("Enter Down Payment Amount: $")
        DownPayment = float(DownPayment)

    if PayType == "Monthly":
        MonthlyPayment = (TotalCost + PROCFEE) / 8
    elif PayType == "Down Pay":
        MonthlyPayment = (TotalCost - DownPayment + PROCFEE) / 8
    else:
        MonthlyPayment = 0

    # Helping the boolean have a nicer output as yes or no

    Extra_LiPrint = "Yes" if Extra_Li else "no"
    GlassPrint = "Yes" if GlassCover else "no"
    LoanerPrint = "Yes" if LoanerCar else "no"

# =================
# Here is Print Output
# =================

    print()
    print()
    print()
    print()

    print("===================Policy Summary=======================")
    print(f"{'Policy #':<30}{POLNUM:>26}")
    print(f"{'Customer Name:':<30}           {Fname} {Lname}")
    print(f"{'Policy Date:':<30}{PolicyDate:>26}")
    print(f"{'Address :':<30} {Address},{City},{Prov},{Postal}")
    print(f"{'Phone :':<30}           {FormattedPhone}")
    print(f"{'Number Of Cars :':<30}{NumCars:>26}")
    print(f"{'Extra Liability :':<30}{Extra_LiPrint:>26}")
    print(f"{'Glass Coverage :':<30}{GlassPrint:>26}")
    print(f"{'Loaner Car Coverage :':<30}{LoanerPrint:>26}")
    print(f"{'Payment Type :':<30}{PayType:>26}")
    # Put this if right in my output statments .. did not think of it as an issue bruno
    if PayType == "Down Pay":
        print(f"{'Down Payment:':<30}{FV.FDollar2(DownPayment):>26}")
    print(f"{'Total Premium :':<30}{TotalPrem:>26}")
    print(f"{'HST :':<30}{HST:>26}")
    print(f"{'Total Cost :':<30}{TotalCost:>26}")
    print(f"{'FIRST PAYMENT DATE:':<30}{FV.first_payment_date():>26}")
    print()
    print()
    print()

    # =================
    # Previous Claim Output Here
    # =================

   
    while True:
        ClaimNumber = input("Enter Previous Claim Number (Enter END To Quit) ").upper()
        if ClaimNumber == "END":
            break
        ClaimDateEntry = input("Enter The Claim Date(YYYY-MM-DD) ")
        ClaimAmount = input("Enter Claim Amount $ ")
        ClaimAmount = float(ClaimAmount)

        ClaimNum.append(ClaimNumber)
        ClaimDate.append(ClaimDateEntry)
        ClaimAmt.append(ClaimAmount)

        print()
        print("===============Claim Summary=====================")
        print(" Claim #      Claim Date     Amount")
        print("--------------------------------------")
        
        for i in range(len(ClaimNum)):
            print(f"{ClaimNum[i]:<13} {ClaimDate[i]:<16}{FV.FDollar2(ClaimAmt[i])}")
          
        if PayType == "Monthly":
            print(f"Monthly Payment (8x): {FV.FDollar2(MonthlyPayment)}")

        # append, this is needed to add entry into the policy data
        

        with open("Policies.dat", "a") as f:
            f.write(f"{POLNUM},{PolicyDate},{Fname},{Lname},{Address},{City},{Prov},{Postal},{Phone},{NumCars},{Extra_LiPrint},{GlassPrint},{LoanerPrint},{PayType},{TotalPrem:.2f},{HST:.2f},{TotalCost:.2f},{MonthlyPayment:.2f}\n")


        #=========
        # Claims Record Writing Here
        #=========
        with open("Claims.dat","a") as f:
         for i in range(len(ClaimNum)):
            f.write( f"{POLNUM},{ClaimNum[i]},{ClaimDate[i]},{FV.FDollar2(ClaimAmt[i])}\n")
          
            
        # =================
        # Housekeeping
        # =================

        # Added to check & see if the program was actually writing to policies.. Carried away.. Possible
        
        print()
        print()
        print("Auto Saving.", end="", flush=True)
        time.sleep(0.6)
        print(".", end="", flush=True)
        time.sleep(0.6)
        print(".", end="", flush=True)
        time.sleep(0.5)
        print(".", end="", flush=True)
        time.sleep(0.5)
        print("Saved!", flush=True)
        time.sleep(0.6)
        print("Done!")

    # =================
    # Here Data Is Written To Policies
    # =================

        POLNUM += 1

        with open("Defaults.dat", "w") as f:
            f.write(f"{POLNUM}\n")
            f.write(f"{PROCFEE}\n")
            f.write(f"{HST_RATE}\n")
            f.write(f"{BASICPREM}\n")
            f.write(f"{DISCOUNT}\n")
            f.write(f"{LIAB}\n")
            f.write(f"{GLASS}\n")
            f.write(f"{LOANER}\n")

    redo = input("Would You Like To Proccess Another Policy? (Y/N)").upper()
    if redo != "Y":
        break
