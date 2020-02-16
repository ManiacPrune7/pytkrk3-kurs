"""
    prezentacja uzycia modyfikowalnych argumentow do funkcji
"""

def add_employee(emp, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)


add_employee("Zygmunt")
add_employee("Marysia")
add_employee("Tymek")