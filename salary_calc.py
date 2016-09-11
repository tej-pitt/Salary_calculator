"""Author: Tejas Pitkar 
    Script: Salary calculator """
import math

class SalPay(object):
    def __init__(self,name,position):
        self.name= name
        self.position= position 
        # Personal Details
        print("Welcome to ABLE HOME&OFFICE TOOMBUL Salary calculator!")
        name = input("Enter your first name: ")
        position= input("Enter your job position: ")
    
    def regPay(self):
        #Computes regular hours weekly pay
        hwage= float(input("Enter hourly wage rate: "))
        tothours=float(input("Enter total regular hours you worked this week: "))
        regular_pay= float(hwage * tothours)
        print ("Your regular pay for this week is:$ ", regular_pay)
        print("Your fortnightly pay with the same cycle is: $",2*regular_pay)
        return hwage, regular_pay 

    def overTime(self,hwage, regular_pay):
        #Computes overtime pay and adds the regular to give a total
        totot_hours= int(input("Enter total overtime hours this week: "))
        ot_rate = float(1.5 * (hwage))
        otpay= totot_hours * ot_rate 
        print("The total overtime pay this week is:$ " ,otpay )
        sum = otpay + regular_pay 
        print("So total pay due this week is: $ %6.2f " % sum)
        super_pay = float((9.5/100)*sum)
        print ("Your super contribution this week is: $ ",super_pay)
        return super_pay 
    
    def taxpay(self):
        #Computes the taxes for different income thresholds, for resident Aussies.
        x = float(input("Enter the amount of your yearly income:$ "))
    
    
        while True:
            total = 0 
            if x  < 18200:
                print("Congrats! You dont have to pay any tax! :)")
                return x
                break 
            elif 18201 < x < 37000:
                total = ((x-18200)*0.19)
                print ("You have to pay $", total , "in taxes this year")
                return x 
                break 
            elif 37001 < x < 80000:
                total = 3572 + ((x-37000)*0.32)
                print("You have to pay $",(((x-37000)*0.325) +3572),"in taxes this year")
                return x 
                break 
            elif 80001 < x < 180000:
                total = 17547+((x-80000)*0.37)
                print ("You have to pay $",total ,"in taxes this year")
                return x 
                break 
            elif 180001 < x:
                total = 54547+((x-180000)*0.45)
                print ("You have to pay $",total ,"in taxes this year")
                return x 
                break
            else:
                print ("Invalid input. Enter again please.")
                continue
                    
    def super(self,x):
        #Computes super over a gross income at a rate of 9.5%
        super_rate = float(9.5/100)
        super_gross = float(super_rate*(x))
        print ("Your super contribution this year is: $ ",super_gross)
    
            
    def main(self):
        #Main function to pass vars from regPay to overTime and call.
    
        hw,r_p= self.regPay()
        self.overTime(hw, r_p)
        y = self.taxpay()
        self.super(y)
        

        

a= SalPay('name','position')
a.main()






            





