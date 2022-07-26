'''task_2
sum_range(start, end)'''

def sum_range(start: int, end: int) -> int:
    sum = 0
    if start <= end:
        for i in range(start, end + 1):
            sum += i
    else:
        for i in range(end, start + 1):
            sum += i
    return sum

start = int(input('input start: '))
end = int(input('input end: '))

print(sum_range(start, end))