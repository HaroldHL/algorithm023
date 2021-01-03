def plusOne(digits):
    res = []
    while digits and digits[-1] == 9:
        digits.pop()
        res.append(0)
    if not digits:
        return [1] + res
    else:
        digits[-1] += 1
        return digits + res


print(plusOne([1,2,9]))

print(plusOne([9,9]))