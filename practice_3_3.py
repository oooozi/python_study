list = ["apple", "banana", "orange", "strawberry"]

def longest(x):
    if not x:
        return None
    
    longest_string = x[0]
    for string in x:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

result = longest(list)
print(f"{list}에서 가장 긴 문자열 : ", result)
