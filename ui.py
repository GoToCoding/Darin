from tkinter import Tk, Canvas, Frame, BOTH, W


class UI(Frame):

    def __init__(self, parent, table):
        Frame.__init__(self, parent)

        self.table = table

        self.parent = parent
        self.parent.title("GoToCoding/checks15x15")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        for i in range(15):
            coord = chr(ord('a') + i)
            if i >= ord('i') - ord('a'):
                coord = chr(ord('a') + i + 1)
            if coord == 'm':
                canvas.create_text(i * 60 + 10, 920, anchor=W, font=("Purisa", 50), text=coord)
            else:
                canvas.create_text(i * 60 + 20, 920, anchor=W, font=("Purisa", 50), text=coord)

        for i in range(15):
            if i < 10:
                canvas.create_text(930, i * 60 + 30, anchor=W, font=("Purisa", 50), text=str(i))
            else:
                canvas.create_text(920, i * 60 + 30, anchor=W, font=("Purisa", 50), text=str(i))

        for i in range(15):
            for j in range(15):
                color = '#111'
                canvas.create_rectangle(60 * i, j * 60, 60 * (i + 1) - 1, 60 * (j + 1) - 1, outline='#fff', fill=color)

        for i in range(15):
            for j in range(15):
                if self.table[i][j] == 1:
                    color = '#f50'  # First player
                elif self.table[i][j] == -1:
                    color = '#fff'  # Second player
                else:
                    continue
                canvas.create_oval(60 * i + 10, j * 60 + 10, -10 + 60 * (i + 1) - 1, -10 + 60 * (j + 1) - 1, outline='#fff', fill=color)

        canvas.pack(fill=BOTH, expand=1)


def draw_table_once(table):
    root = Tk()
    UI(root, table)
    root.geometry("980x1000")
    root.mainloop()
