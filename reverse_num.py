#Write a function that will reverse a integer number using a stack and return the reversed number as an integer. 
# For example, if your input number is 3479 the function will return 9743. 

def size(stack): 
    return len(stack) 
  
def isEmpty(stack): 
    if size(stack) == 0: 
        return true 
  
def push(stack,item): 
    stack.append(item) 
  
def pop(stack): 
    if isEmpty(stack): return
    return stack.pop() 
  
def reverse_num(num): 
    stack = []

    n = len(num)
  
    for i in range(0,n,1): 
        push(stack,num[i]) 
  
    number="" 

    for i in range(0,n,1): 
        number+=pop(stack) 
          
    return number 

print(reverse_num("3479")) 
print(reverse_num("85612")) 
print(reverse_num("895572")) 
print(reverse_num("752725")) 
  