# Analysis Questions

## 1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.

**ANSWER:**

Task Parallelism executes different operations concurrently on the same data.  
● Demonstrated in Part A (ThreadPoolExecutor).  
● Each deduction (SSS, PhilHealth, Pag-IBIG, Tax) is a separate task applied to one salary.  
● Workload is divided by function type.  

Data Parallelism executes the same operation concurrently on different data.  
● Demonstrated in Part B (ProcessPoolExecutor).  
● One payroll function is applied to multiple employees.  
● Workload is divided by employees (data elements).  

---

## 2. Explain how concurrent.futures managed execution, including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor.

**ANSWER:**

The module handles concurrency using Executors and Future objects.  
● submit() – Sends a function to run asynchronously and returns a Future object.  
● map() – Automatically applies one function to multiple inputs in parallel.  
● Future – Holds the result of a task that may still be running. We use .result() to retrieve the output.  

The with statement ensures that the Executor:  
● Properly initializes worker threads/processes  
● Automatically shuts them down after execution  
● Releases system resources safely  

---

## 3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur?

**ANSWER:**

ThreadPoolExecutor uses threads within one process.  

Because of the Global Interpreter Lock (GIL):  
● Only one thread executes Python bytecode at a time.  
● True parallelism for CPU-bound tasks does not occur.  

In this lab (CPU-based computations), execution was concurrent but not fully parallel across multiple CPU cores.  

---

## 4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior.

**ANSWER:**

ProcessPoolExecutor creates separate processes.  

Each process:  
● Has its own memory space  
● Has its own Python interpreter  
● Has its own GIL  

Since the GIL is not shared, multiple CPU cores can run tasks simultaneously, achieving true parallelism.  

---

## 5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?

**ANSWER:**

For a large system (10,000 employees):  
● ThreadPoolExecutor does not scale well for CPU-bound tasks due to the GIL.  
● ProcessPoolExecutor scales better because:  
&nbsp;&nbsp;&nbsp;&nbsp;- Tasks are distributed across CPU cores  
&nbsp;&nbsp;&nbsp;&nbsp;- Employee computations are independent  
&nbsp;&nbsp;&nbsp;&nbsp;- Workload can be evenly divided  

Data Parallelism with processes is more efficient for large-scale payroll processing.  

---

## 6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.

**ANSWER:**

Task Parallelism:  
For one employee:  
● Calculate deductions  
● Generate payslip  
● Update database  
● Send email  

Best executor: ThreadPoolExecutor (especially for I/O-bound tasks).  

Data Parallelism:  
Process payroll for thousands of employees simultaneously.  

Best executor: ProcessPoolExecutor for multi-core utilization and faster computation.
