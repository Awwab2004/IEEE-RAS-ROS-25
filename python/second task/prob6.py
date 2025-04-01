def sum_even_numbers(num):
    return sum(i for i in range(1, num+1) if i % 2 == 0)
num = int(input("Enter a number: "))
print(f"The sum of even numbers from 1 to {num} is {sum_even_numbers(num)}")