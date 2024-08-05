# "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in range(len(numbers)):
    if numbers[i] == 2:
        primes.append(numbers[i])
    if numbers[i] != 1:
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                #print("Not Primes", numbers[i])
                not_primes.append(numbers[i])

            else:
                #print("Primes", numbers[i])
                primes.append(numbers[i])
            break

print("Primes :", primes)
print("Not Primes :", not_primes)