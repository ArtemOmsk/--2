#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# def Fibonacci(n):
#     if n in [1, 2]: 
#         return  1
#     else:
#         return (n-1) + Fibonacci(n-2)

# def NegaFibonacci(n):
#     if 1 == 1: 
#         return  1
#     if 2 == 2: 
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2

# list = [0]
# userNumber = int(input('Enter any number: '))
# for e in range(1, userNumber + 1):
#     list.append(Fibonacci(e))
#     list.insert(0, NegaFibonacci(e))
# print(list)