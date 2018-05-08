#!/usr/bin/env python3
import sys

#dict_tax2 = {0:[0,0,0.03],1:[1500,105,0.1],2:[4500,555,0.2],3:[9000,1005,0.25],4:[35000,2755,0.3],5:[55000,5505,0.35],6:[80000,13505,0.45]}


def tax_calc(salary):
    taxable_part = salary - 3500 - salary*0.165
    if taxable_part <= 0:
        return '0.00'
    insurance_list = [
        (80000, 0.45, 13505),
        (55000, 0.35, 5505),
        (35000, 0.30, 2755),
        (9000, 0.25, 1005),
        (4500, 0.2, 555),
        (1500, 0.1, 105),
        (0, 0.03, 0)
    ]
    for insurance in insurance_list:
        #print(insurance[0],insurance[1])
        if taxable_part > insurance[0]:
            result = taxable_part*insurance[1]-insurance[2]
            return '{:.2f}'.format(result)
        #return sum_insurance
        #print(sum_insurance)
def main():
    # if len(sys.argv) != 2:
    #     print('Parameter Error')
    #     exit()
    try:
        for arg in sys.argv[1:]:
            salary_info = arg.split(':')
            #print(salary_info)
            salary_id = salary_info[0]
            salary = int(salary_info[1])
            after_tax = float(salary) - float(salary * 0.165) - float(tax_calc(salary))
            print(str(salary_id)+':'+str(after_tax))
    except ValueError:
        print('Parameter Error')
        exit()
    #print(tax_calc(salary))


if __name__ == '__main__':
    main()
# for arg in sys.argv[1:]:
#     #print(arg)
#     #print(arg.split(':'))
#     #tax_salary = float()
#     user_info = arg.split(':')
#     user_id = user_info[0]
#     user_salary = float(user_info[1])
#     print(user_id,user_salary)
#     tax_calc(user_salary)

