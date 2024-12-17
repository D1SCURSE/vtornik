def is_product_of_two(numbers, target):
    seen = set(numbers)  
    for num in seen:
        if num != 0 and target % num == 0:  
            complementary = target // num
            if complementary in seen and complementary != num:
                return True
    return False

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

if is_product_of_two(numbers, target):
    print("ДА")
else:
    print("НЕТ")
