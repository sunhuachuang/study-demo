n = 100000;

prime_numbers = [2]

if n <= 2:
    print(2);
else:
    for x in range(3, n, 2):
        for y in prime_numbers:
            if x%y  == 0:
                break;
        else:
            prime_numbers.append(x);

print(prime_numbers.pop());
