input = []
with open('d1_input.txt', 'r') as file:
    data = file.read()
    input = [ int(x) for x in data.split() ]


#pt1
count = 0
for i,v in enumerate(input):
    if v > input[i-1]:
        count += 1

print(count)

#pt2
count2 = 0
i = 0
while i < (len(input) - 3):
    if input[i+3] > input[i]:
        count += 1
    i += 1

print(count2)

