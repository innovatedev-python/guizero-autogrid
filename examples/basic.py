# use the guizero_autogrid widgets if you don't want to calculate/specify grid on
# every child of a grid layout or to set the spacing between items on the grid
from guizero_autogrid import App, Auto, Box, NextRow, Text

# use the layout='grid' as usual
app = App(layout="grid", spacing=10)

# grid=[0,0] is not requried
t1 = Text(app, text="TEST col 0, row 0")

# grid=[1,0] is not requried
t2 = Text(app, text="TEST col 1, row 1")
# grid=[2,0] is not requried
t3 = Text(app, text="TEST col 2, row 0")

# use grid=Nextrow to move to the next row
t4 = Text(app, text="TEST col 0, row 1", grid=NextRow)

# to combine with spanning cells, use the Auto value for the row/col values
b1 = Box(app, grid=[Auto, Auto, 2, 1], border=1)
t5 = Text(b1, text="TEST col 2, row 0")


app.display()
