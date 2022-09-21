def binary_inserts(data):
    for i in range(1, len(data)):
        x = data[i]
        left = 0
        right = i - 1
        while left <= right:
            j = (left + right) // 2
            if x < data[j]:
                right = j - 1
            else:
                left = j + 1
        k = i - 1
        while k >= left:
            data[k + 1] = data[k]
            k = k - 1
        data[left] = x
    return data

data = [0, 5, -5, 10, 8, 1]
print(binary_inserts(data))

