# Library of functions for formatting numbers and dates.

import datetime

#Receipt Generator Function

def Receipt_gen_id(FirstName, LastName, Plate, Phone):
      if len(Phone) == 10 and Phone.isdigit():
        Initials = FirstName[0].upper() + LastName[0].upper()
        LastThree = Plate[-3:]
        LastFour = Phone[-4:]
        return(f"{Initials}-{LastThree}-{LastFour}")
      else:
       print("Phone Number Is invalid. Please try again")
      exit()

#Here is current Date 

CURRENT_DATE = datetime.datetime.now() 

def first_payment_date():
    one_month = datetime.timedelta(days=30)
    return (CURRENT_DATE + one_month).strftime("%b %d, %Y")

#Format Phone Function

def format_phone(Phone):

    area = Phone[0:3]
    middle = Phone[3:6]
    end = Phone[6:10]
    return "(" + area + ")" + middle + "-" + end 



#Mileage Function

def mileage_valid(mileage_input):
    try:
         mileage = int(mileage_input)
         if mileage >= 0:
            return mileage
         else:
            print("Mileage must be greater than zero ")
    except ValueError:
        print("Mileage Must Be Whole Number")
            
   



def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to #,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to #,###.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to ####.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to ####.#.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to ####.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr
