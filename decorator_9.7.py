def is_prime(func):
        def wrapper(*args):
            result = sum(args)
            if result % 2:
                print("Prime")
            else:
                print("Not Prime")
            return result
        return wrapper
@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

