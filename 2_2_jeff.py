import os

correct = 0
passwordlist = []
with open('2.txt') as f:
    text = f.read()
    for x in text.splitlines():
        line = x.replace("-", " ")
        line1 = line.replace(": ", " ")
        line2 = line1.split(" ")
        print(line2)
        first_position = int(line2[0])
        second_position = int(line2[1])
        target_char = line2[2]
        password = (line2[3])
        password_1 = password[(first_position - 1)]
        password_2 = password[(second_position - 1)]
        if password_1 == target_char or password_2 == target_char:
            if password_1 != password_2:
                correct += 1
print(correct)