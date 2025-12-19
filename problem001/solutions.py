def brute_force(limit=1000):
    total = 0 
    # iterate through each number in range
    for i in range(limit): 
        # check if i is divisible by 3 or 5
        if i % 3 == 0 or i % 5 == 0: 
            total += i
    return total



def arithmetic_sum(n, step): 
    # calculate how many multiples there are in numbers 1 -> step
    m = n // step 
    # use arithmetic sequence sum formula to find sum
    return step * m * (m + 1) // 2 

def efficient_solution(limit=1000): 
    # add together sum of multiples 3 and 5, minus their crossover, since they will be repeated
    return (arithmetic_sum(limit-1, 3) + 
            arithmetic_sum(limit-1, 5) - 
            arithmetic_sum(limit-1, 15))



def run_all():
    """run and test all approaches"""
    limit = 1000
    expected = 233168
    
    print(f"=== Euler problem 1 solutions ===")
    print(f"limit: {limit}")
    print(f"expected answer: {expected}\n")
    
    #test all functions
    print(brute_force(limit))
    print(efficient_solution(limit))



run_all()
