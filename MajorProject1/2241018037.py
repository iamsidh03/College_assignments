def basics_salary(hourly_rate,hours_worked_per_week):
    work_hours=40
    if hours_worked_per_week<=work_hours:
       return hourly_rate*hours_worked_per_week*4
    else:
        return hours_worked_per_week*hourly_rate*4+overtime_salary(hourly_rate,hours_worked_per_week)
def overtime_salary(hourly_rate,hours_worked_per_week):
    work_hours=40
    if hours_worked_per_week>40:
        extra_hrs=hours_worked_per_week-work_hours
        return extra_hrs*1.5*hourly_rate*4
    return 0
def total_salary(hourly_rate,hours_worked_per_Week):
    return basics_salary(hourly_rate,hours_worked_per_Week)

def  tax_amount(salary):

    if salary<60000:
        return 0.1*salary
    elif 65000<=salary<85000:
        return .15*salary
    else:
        return 0.20*salary
    
def gross_salary(basic_salary):
    allowances = 0.20 * basic_salary  # 20% allowance
    total_gross = basic_salary + allowances - tax_amount(basic_salary)
    return total_gross

def salary_bracket(gross_salary):
    if gross_salary < 50000:
        return "Low income"
    elif 50000 <= gross_salary <= 80000:
        return "Middle income"
    else:
        return "High income"

def employee_report(employees):
    print(f"{'Employee':<15} {'Basic Salary':<15} {'Gross Salary':<15} {'Tax Amount':<15} {'Bracket':<15}")
    print("="*75)
    for employee in employees:
        name, hourly_rate, hours_worked = employee
        basic = basics_salary(hourly_rate, hours_worked)
        gross = gross_salary(basic)
        tax = tax_amount(basic)
        bracket = salary_bracket(gross)
        print(f"{name:<15} {basic:<15.2f} {gross:<15.2f} {tax:<15.2f} {bracket:<15}")
   
employees = [
    ("John", 500, 45),   # Employee 1
    ("Jane", 400, 38),   # Employee 2
    ("Alice", 600, 42)   # Employee 3
]

employee_report(employees)