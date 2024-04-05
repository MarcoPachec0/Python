# Write your code below this line 👇
import math
def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint")
# Write your code above this line 👆

# Define a function called paint_calc() so the code below works.
# 1 can of paint can cover 5 square meters
# number of cans = (wall height x wall width) ÷ coverage per can

# 🚨 Don't change the code below 👇
test_h = int(input('Height of wall (m)')) # Height of wall (m)
test_w = int(input('Width of wall (m)')) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)