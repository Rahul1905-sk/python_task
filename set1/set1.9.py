def fibonacci(n):
    sequence = []
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence
 
input_number = 10
fibonacci_sequence = fibonacci(input_number)
print(fibonacci_sequence)
