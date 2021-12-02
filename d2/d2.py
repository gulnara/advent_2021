
file1 = open('d2_input.txt', 'r')
lines = file1.readlines()

# pt1
final_h = 0
final_d = 0
for line in lines:
    k = line.split()
    if k[0] == 'forward':
        final_h += int(k[1])
    elif k[0] == 'down':
        final_d += int(k[1])
    else:
        final_d -= int(k[1])
result1 = final_d * final_h

#pt2
final_h = 0
final_d = 0
aim = 0
for line in lines:
    k = line.split()
    if k[0] == 'forward':
        final_h += int(k[1])
        final_d += (aim * int(k[1]))
    elif k[0] == 'down':
        aim += int(k[1])
    else:
        aim -= int(k[1])




result2 = final_d * final_h
print(result1)
print(result2)
