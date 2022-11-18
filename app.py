class SquareRootCalculate:
  def square_root(self, n):
    return n ** 0.5

print("Enter a Number: ")
num = int(input())

obj1 = SquareRootCalculate()
squareroot = obj1.square_root(num)
print(f"The square root of {num} = {squareroot}")