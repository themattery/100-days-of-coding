line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input().upper() # Where do you want to put the treasure?

column = position[0]
line = position[1]

if column == 'A':
  column = 0
elif column == 'B':
  column = 1
else:
  column = 2

map[int(line)-1][int(column)] = 'X'

print(f"{line1}\n{line2}\n{line3}")