class Student(object)
 student_count = 0

  def __new__(self):
    print('Student._new_')

  def __init__(self):
    print('Student._init_')
    self.gpa = 4.00

  def study_hard(self):
    print('Sir, yes sir.')
