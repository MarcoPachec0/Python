target = int(input('Please write a number: '))
sumEvenNumber = 0

for number in range(2, target+1):
      if number % 2 == 0:
          sumEvenNumber += number

print(sumEvenNumber)
