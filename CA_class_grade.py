# codeacademy.com's micro project
# to practice list,dict and functions

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)
def get_average(student):
  homework = average(student["homework"]) / 10
  quizzes = average(student["quizzes"]) * (3/10.0)
  tests = average(student["tests"]) * (6/10.0)
  return homework+quizzes+tests
def get_letter_grade(score):
  if score>89:
    return "A"
  elif score>79:
    return "B"
  elif score>69:
    return "C"
  elif score>59:
    return "D"
  else:
    return "F"
print(get_letter_grade(get_average(lloyd))  )
def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)
students = [alice,lloyd,tyler]
print(get_class_average(students))