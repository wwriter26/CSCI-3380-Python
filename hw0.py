class Exam:
  def PassFail(self, exam1, exam2, exam3, exam4):
    #given four test grades out of 100, what is the minimum grade needed on the 200 point final to pass the class?
    #passing is 55% or higher
    #return the minimum grade needed on the final to pass the class
    totalGrade = exam1 + exam2 + exam3 + exam4
    fiftyFivePercent = 600 * .55
    finalGrade = fiftyFivePercent - totalGrade
    return int(finalGrade)
