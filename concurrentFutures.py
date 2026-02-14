import threading

def compute_sss(salary):
    print(f"SSS computed by: {threading.current_thread().name}")
    return salary * 0.045

def compute_philhealth(salary):
    print(f"PhilHealth computed by: {threading.current_thread().name}")
    return salary * 0.025

def compute_pagibig(salary):
    print(f"Pag-IBIG computed by: {threading.current_thread().name}")
    return salary * 0.02

def compute_tax(salary):
    print(f"Tax computed by: {threading.current_thread().name}")
    return salary * 0.10

from concurrent.futures import ThreadPoolExecutor

def task_parallelism_demo(salary):
    print("\n===== TASK PARALLELISM (ThreadPoolExecutor) =====")

    with ThreadPoolExecutor() as executor:
        future_sss = executor.submit(compute_sss, salary)
        future_philhealth = executor.submit(compute_philhealth, salary)
        future_pagibig = executor.submit(compute_pagibig, salary)
        future_tax = executor.submit(compute_tax, salary)

        sss = future_sss.result()
        philhealth = future_philhealth.result()
        pagibig = future_pagibig.result()
        tax = future_tax.result()

    total_deduction = sss + philhealth + pagibig + tax

    print(f"SSS: {sss:.2f}")
    print(f"PhilHealth: {philhealth:.2f}")
    print(f"Pag-IBIG: {pagibig:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Total Deduction: {total_deduction:.2f}")

    return total_deduction

def compute_payroll(employee):
    name, salary = employee

    sss = salary * 0.045
    philhealth = salary * 0.025
    pagibig = salary * 0.02
    tax = salary * 0.10

    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction

    return {
        "name": name,
        "gross_salary": salary,
        "total_deduction": total_deduction,
        "net_salary": net_salary
    }

from concurrent.futures import ProcessPoolExecutor

employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

def data_parallelism_demo():
    print("\n===== DATA PARALLELISM (ProcessPoolExecutor) =====")

    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_payroll, employees)

    for result in results:
        print("\n---------------------------")
        print(f"Employee: {result['name']}")
        print(f"Gross Salary: {result['gross_salary']:.2f}")
        print(f"Total Deduction: {result['total_deduction']:.2f}")
        print(f"Net Salary: {result['net_salary']:.2f}")


if __name__ == "__main__":

    
    sample_salary = 30000

    task_parallelism_demo(sample_salary)

    data_parallelism_demo()