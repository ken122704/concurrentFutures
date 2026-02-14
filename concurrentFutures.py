# ==============================
# MEMBER 1 – DEDUCTION FUNCTIONS
# ==============================

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

    return total_deductions