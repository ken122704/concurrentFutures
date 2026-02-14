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