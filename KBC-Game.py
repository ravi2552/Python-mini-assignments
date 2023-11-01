questions = [
  ["What is the output of the following Python code? ==>>  print(3 + 4 * 2) ", "11", "14", "70", "10", 2],
  ["Which of the following is not a valid Python data type? ", "float", "complex", "array", "tuple", 3],
  ["What does the acronym API stand for in programming?", "Application Program Interface", "Application Programming Interface", "Application Protocol Interface", "Application Procedure Interface", 2],
  ["In Python, how do you round the number 7.6 to the nearest integer?", "round(7.6, 0)", "round(7.6)", "round(7.6, 1)", "int(7.6)", 2],
  ["Which of the following is not a valid way to comment a single line of code in Python?", "# This is a comment", "// This is a comment", "/* This is a comment */", "''' This is a comment '''", 2],
  ["What is the result of the following expression in Python? ==>> 5 ** 2 ", "10", "25", "7", "10", 2],
  ["In Python, which of the following data structures is used to store elements with key-value pairs?", "List", "Tuple", "Dictionary", "Set", 3],
  ["Which programming language is often used for web development and is known for its simplicity and readability?", "Python", "Java", "c++", "Ruby", 1],
  ["Which programming language is often used for developing mobile applications for Android?", "Shift", "Kotlin", "Java", "C++", 2],
  ["What is the primary purpose of a 'for' loop in programming?", "To define a function", "To create an object", "To repeat a block of code a specific number of times", "To perform a mathematical calculation", 3],
  ["Which of the following operators is used for string concatenation in Python?", "+", "-", "*", "/", 1],
  ["What is the term for a variable that is accessible from any part of a program?", "Global variable", "Local variable", "Private variable", "Constant variable", 1],
  ["Which data structure follows the Last-In-First-Out (LIFO) principle?", "Queue", "Stack", "List", "Linked list", 2],
  ["What is the file extension for a Python source code file?", ".py", ".exe", ".doc", ".txt", 1],
  ["Which of the following is an example of a high-level programming language?", "Machine code", "Assembly language", "c++", "Binary code", 3],
  ["What does the acronym HTML stand for in web development?", "Hyper Text Markup Language", "High Tech Modern Language", "Hyper Transfer Markup Language", "Hyperlink and Text Markup Language", 1],
]

levels = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 500000, 650000, 800000, 1000000, 1500000, 2000000, 2500000, 3000000]
money = 0
for i in range(0, len(questions)):
  question = questions[i]
  print(f"\n\nQuestion for {levels[i]}")
  print(question[0])
  print(f"a. {question[1]}          b. {question[2]}")
  print(f"c. {question[3]}     d. {question[4]}")
  answer = int(input("Enter your answer from (1-4) or 0 to quit\n"))
  if answer == 0:
    money = levels[i-1]
    break
  if answer == question[-1]:
    print(f"Congrats! You won {levels[i]}")
    if i == 4:
      money = 10000
    elif i == 9:
      money = 320000
    elif i == 14:
      money = 10000000
  else:
    print(f"Sorry! You lost {levels[i]}")
    break

print(f"Total money you won {money}")

