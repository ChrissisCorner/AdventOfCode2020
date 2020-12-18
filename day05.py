with open('day05.txt') as f:
    seatings = f.read().split('\n')

    print(seatings)

    seat_id = []

for s in seatings:
    row = s[:7].replace('F', '0')
    row = row.replace('B', '1')
    #row = int(row)

    column = s[-3:].replace('L', '0')
    column = column.replace('R', '1')
    #column = int(column)

    print(row)
    print(column)

    row = int(row, 2)
    column = int(column, 2)

    seat_number = row * 8 + column
    seat_id.append(seat_number)

    #print(row)
    #print(column)

seat_id.sort()
solution_part_one = seat_id[-1]

#solution inspired by The Morpheus Tutorials
solution_part_two = set(range(seat_id[0], seat_id[-1])) - set(seat_id)




#for s in seat_id:
 #   if s in solution_part_two:
  #      solution_part_two.remove(s)

print('soultion 1: ', solution_part_one)
print('solution two: ', solution_part_two)