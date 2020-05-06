#Write a function called compute_sum() that takes in a single integer argument n 
# and returns the sum of the positive integers from 1 to n. For example compute_sum(4) 
# would return 10, or 1+2+3+4. 

def compute_sum(n):
    sum = n
    # while n > 0:
    #     sum += (n-1)
    #     n -=1
    sum = (n/2)*(n+1)
    print (sum)
    

compute_sum(8)
compute_sum(10)
compute_sum(12)
compute_sum(14)
    
