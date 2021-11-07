row1= ["⬜️","⬜️","⬜️"]
row2= ["⬜️","⬜️","⬜️"]
row3= ["⬜️","⬜️","⬜️"]
map = [row1,row2,row3]
print(f"{row1}\n {row2}\n {row3}")
position = input("where do you want to put the treasure? \n")
h = int(position[0])
v = int(position[1])
select_row = mab[h-1]
select_row[v-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
