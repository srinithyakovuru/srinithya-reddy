

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))