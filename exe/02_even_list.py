def num_list(numbers):
    even_list = []
    for n in numbers:
        if n % 2 == 0:
            even_list.append(n)
    even_list.sort(reverse=True)
    return even_list


nums = list(map(int, input("Enter numbers: ").split(',')))
print(num_list(nums))
