from tkinter import *
import settings
import utils
from cell import Cell


root = Tk()

root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",
    width=1440,
    height=utils.height_prct(25)
                  )

top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper",
    font=("", 33)
)

game_title.place(
    x=utils.width_prct(33),
    y=25
)

left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
                 )
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
                    )
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25),
                 )

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
                            )

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

# Randomizes the placement of mines on grid
Cell.randomize_mines()

# Runs the window
root.mainloop()
