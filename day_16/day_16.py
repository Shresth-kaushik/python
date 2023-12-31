# Pretty table package installation in the python in pyCharm .
from prettytable import PrettyTable
table = PrettyTable()
# task is to form a table
table.add_column("Pokemon Name", ["Pikaschu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# to align the elements in left
table.align = "l"
print(table)
