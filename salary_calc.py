"""Author: Tejas Pitkar 
    Script: Salary calculator """
import math

# Personal Details
name = input("Enter your first name: ")
position= input("Enter your job position: ")
    
def regPay():
#Computes regular hours weekly pay
    hwage= float(input("Enter hourly wage rate: "))
    tothours=int(input("Enter total regular hours you worked this week: "))
    regular_pay= float(hwage * tothours)
    print ("Your regular pay for this week is: ", regular_pay)
    return hwage, regular_pay

def overTime(hwage, regular_pay):
#Computes overtime pay and adds the regular to give a total
    totot_hours= int(input("Enter total overtime hours this week: "))
    ot_rate = float(1.5 * (hwage))
    otpay= totot_hours * ot_rate 
    print("The total overtime pay this week is: " ,otpay )
    sum = otpay + regular_pay 
    print("So total pay due this week is: ", sum)
        
def main():
#Main function to pass vars from regPay to overTime and call.
    hw , r_p = regPay()
    overTime(hw, r_p)
        
#Call main
main()


            





