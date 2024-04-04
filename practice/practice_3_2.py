list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

def common(x, y):
    common_numbers = []
    for number in x:
        if number in y:
            common_numbers.append(number)
    return common_numbers

result1 = common(list1, list2)
print(f"{list1} 와 {list2} 의 공통값 : ", result1)

result2 = common(result1, [5,6,7])
print(f"{result1} 와 [5,6,7] 의 공통값 : ", result2)
