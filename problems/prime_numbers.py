def is_prime(e):
    #val less than 1 or 1 is not prime
    if e <= 1:
        return False
    #2 is always prime 
    if e == 2:
        return True
    for i in range(2, int(e**0.5) + 1):
        #only need to loop e pow 1/2 
        #25 //5*5 python range gives one less
        if e % i == 0:
            return False
    return True 
# 
#map(int,x) //here int is function\

input = input("Enter the numbers separated by spaces: ").split()
#print(input)

list = list(map(int,input))
prime_list = []
#23 435 56
#[23, 435, 56]
#print(list)

for num in list:
    if is_prime(num):
        #print(f"{num} is a prime number.")
         prime_list.append(num)

print(prime_list)

   
