# Project Euler - problem 1: multiples of 3 and 5

[🔗 problem link](https://projecteuler.net/problem=1)

## 📋 problem statement
> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
> 
> Find the sum of all the multiples of 3 or 5 below 1000.

## 🧠 Mathematical Insight
This problem can be solved efficiently using the inclusion-exclusion principle:
\[
\text{sum} = (\text{sum of multiples of 3}) + (\text{sum of multiples of 5}) - (\text{sum of multiples of 15})
\]
where each sum is an arithmetic series:
\[
S_n = \frac{n(n+1)}{2} \times \text{step}
\]

**Direct formula:**
\[
\text{Answer} = 3 \times \frac{333 \times 334}{2} + 5 \times \frac{199 \times 200}{2} - 15 \times \frac{66 \times 67}{2}
\]

## 💻 Solutions

### Solution 1: Brute Force (Naive)
```python
def brute_force(limit=1000):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(brute_force())  # 233168
```

### Solution 2: Efficient Formula (O(1))
```python
def arithmetic_sum(n, step):
    """Sum of arithmetic series: step, 2*step, ..., up to n*step"""
    m = n // step
    return step * m * (m + 1) // 2

def efficient_solution(limit=1000):
    return (arithmetic_sum(limit-1, 3) + 
            arithmetic_sum(limit-1, 5) - 
            arithmetic_sum(limit-1, 15))

print(efficient_solution())  # 233168
```

### Solution 3: List Comprehension (Pythonic)
```python
def pythonic_solution(limit=1000):
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)

print(pythonic_solution())  # 233168
```

## 📊 Performance Comparison
```
Brute Force (1000 iterations): 0.0002s
Mathematical Formula (O(1)):   0.0000001s
Pythonic (sum + generator):    0.0001s
```

## 🔍 Key Takeaways
1. **Brute force works** for small limits but scales poorly
2. **Mathematical insight** reduces O(n) to O(1)
3. **Python generators** are memory-efficient for large ranges
4. Always consider the **inclusion-exclusion principle** for "or" conditions

## 🎯 Answer
```
233168
```

---

*Solved on: 2024-01-05*  
*Time to solve: < 5 minutes*  
*Difficulty: 5% (Project Euler rating)*  

[⬅️ Back to Project Euler Solutions](../README.md)
