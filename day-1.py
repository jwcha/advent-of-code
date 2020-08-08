"""
--- Day 1: Not Quite Lisp ---
Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?
"""

with open("day-1-input.txt","r") as f:
    instructions = f.read()


go_up_one_floor_count = instructions.count('(')
go_down_one_floor_count = instructions.count(')')
print(go_up_one_floor_count - go_down_one_floor_count)  # answer is floor 280.

###############################################################################

# PART 2
# given the same input and instructions, find the position of the first 
# character that causes Santa to enter the basement (floor -1). Assume that
# the first character in the instructions has position 1, the second character
# position 2, and so on...
#
# For example:
#   - ) causes him to enter the basement at character position 1.
#   - ()()) causes him to enter the basement at character position 5.

# QUESTION: WHAT IS THE POSITION OF THE CHARACTER THAT CAUSES SANTA TO FIRST ENTER THE BASEMENT?

# the boring and long way to solve this problem would be to keep track of which floor we are currently on as we evaluate
# each instruction character at a time. sigh...
current_floor = 0
position = 0
for c in instructions:
    if current_floor == -1: break
    elif c == '(': current_floor = current_floor + 1
    elif c == ')': current_floor = current_floor - 1
    else: pass
    position = position + 1

print(position)
