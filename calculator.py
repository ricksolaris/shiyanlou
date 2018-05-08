#!/usr/bin/env python3
import sys

dict_tax2 = {0:[0,0,0.03],1:[1500,105,0.1],2:[4500,555,0.2],3:[9000,1005,0.25],4:[35000,2755,0.3],5:[55000,5505,0.35],6:[80000,13505,0.45]}
insurance_list = [0.08,0.02,0.005,0,0,0.06]
threshhold = 3500
#print(sys.argv)
#print(sys.argv[1:])
def tax_calc(salary):
    sum_insurance = float()
    for insurance in insurance_list:
        sum_insurance += float(salary)*insurance
        #return sum_insurance
        #print(sum_insurance)

for arg in sys.argv[1:]:
    #print(arg)
    #print(arg.split(':'))
    #tax_salary = float()
    user_info = arg.split(':')
    user_id = user_info[0]
    user_salary = float(user_info[1])
    print(user_id,user_salary)
    tax_calc(user_salary)

