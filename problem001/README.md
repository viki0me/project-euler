# Project Euler - problem 1: multiples of 3 and 5

[🔗 problem link](https://projecteuler.net/problem=1)

## 📋 problem statement
> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
> 
> Find the sum of all the multiples of 3 or 5 below 1000.

## 💻 solutions

### solution 1: brute force 
```python
def brute_force(limit=1000):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(brute_force())  #233168
```

### solution 2: efficient formula
```python
def arithmetic_sum(n, step):
    m = n // step
    return step * m * (m + 1) // 2

def efficient_solution(limit=1000):
    return (arithmetic_sum(limit-1, 3) + 
            arithmetic_sum(limit-1, 5) - 
            arithmetic_sum(limit-1, 15))

print(efficient_solution())  # 233168
```


## 💡 performance comparison
```
brute force (1000 iterations): 0.0002s
mathematical formula (O(1)):   0.0000001s
```

## 🔍 key notes
1. **brute force method works** for small limits but scales poorly
2. **mathematical insight** reduces O(n) to O(1)

## ⭐️ answer
```
233168
```

---

*solved on: 18-12-2025*  
*time to solve: < 5 minutes*  
*difficulty: 5% (Project Euler rating)*  

[⬅️ back to Project Euler solutions](../README.md)
