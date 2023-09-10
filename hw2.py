class Homework2:
  def DifferenceOfSums(self, numbers):
    sumThrees = 0;
    sumFives = 0;
    for i in numbers:
      if i % 3 == 0:
        sumThrees += i
      if i % 5 == 0:
        sumFives += i
    return abs(sumThrees - sumFives)


# l = Homework2()
# print(l.DifferenceOfSums([1, 2, 3, 4, 5, 10]))

