import pdb

# pdb.set_trace()
lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
maxlist = [max(x) for x in lista]
# print(maxlist)

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True  

list2 = [3, 4, 8, 5, 5, 22, 13]

list_prime = list(filter(isPrime, list2))

print('Primos: ', list_prime)