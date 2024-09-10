type = input("Enter an expression: ")
print("Input two numbers: ")
a, b = int(input()), int(input())

def calculator(a, b):
    match type:
          case "+":
               print(a+b)
          case "-":
               print(a-b)
          case "*":
               print(a*b)
          case "/":
               print(a/b)
          case "%":
               print(a%b)
              
calculator(a, b)