# Multiprocessing vs Multithreading Performance Test

## 📘 Description
This Python program compares the performance of **multiprocessing** and **multithreading** while performing **mensuration calculations** (area, perimeter, volume, surface area, etc.).  
The function `do_something()` performs repeated geometry computations, and the execution time is measured when running:
- Multiple **processes** (using the `multiprocessing` module)
- Multiple **threads** (using the `threading` module)

---

## ⚙️ How It Works
1. The user enters:
   - Number of **processes**
   - Number of **threads**
2. The program runs both multiprocessing and multithreading versions.
3. It measures the time taken for each approach.
4. Finally, you can compare which method was faster.

---

## 🧠 System Setup
- **Language:** Python 3  
- **Modules Used:**  
  ```python
  import math
  import time
  import multiprocessing
  import threading
  ```
- **Function:** `do_something(count, out_list)` performs complex mensuration operations.

**Multiprocessing Time:** `5.23498797416687 s`  
**Multithreading Time:** `13.821916580200195 s`

---

## 📊 Comparison Table

| No. of Processes/Threads | Multiprocessing Time (s) | Multithreading Time (s) |
|---------------------------|---------------------------|---------------------------|
| 5                         | 1.72                      | 7.35                      |
| 10                        | 3.25                      | 9.45                      |
| 15                        | 5.23                      | 13.82                     |

---

## 💡 Conclusion
- **Multiprocessing** was observed to be **faster and more efficient** for CPU-bound operations such as heavy mathematical calculations.  
- **Multithreading** performed slower because of Python’s **Global Interpreter Lock (GIL)**, which prevents true parallel execution of threads for CPU-heavy tasks.  
- Hence, **multiprocessing** is the better choice for tasks involving large numerical computations.

---

## 🧰 Example Output
```
===== MENSURATION PERFORMANCE TEST =====
Enter number of processes: 10
Enter number of threads: 10

List processing complete.
Multiprocessing time = 3.1546270847320557
List processing complete.
Multithreading time = 12.893417358398438
```
