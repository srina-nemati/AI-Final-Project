from tkinter import *

"this is the main library i'm using for this project."
"this is found from GITHUB"
"i used it just to draw hexCanvas and Hexagonal page"
"this page has just helped with cleaner UI and nothing else, it's just like a basic UI library"

class HexaCanvas(Canvas):
    """ A canvas that provides a create-hexagone method """

    def __init__(self, master, *args, **kwargs):
        Canvas.__init__(self, master, *args, **kwargs)
        self.hexaSize = 20

    def setHexaSize(self, number):
        self.hexaSize = number

    def create_hexagone(self, x, y, color="black", fill="blue", color1=None, color2=None, color3=None, color4=None,
                        color5=None, color6=None, text=None):
        """
        Compute coordinates of 6 points relative to a center position.
        Point are numbered following this schema :

        Points in euclidiean grid:
                    6

                5       1
                    .
                4       2

                    3

        Each color is applied to the side that link the vertex with same number to its following.
        Ex : color 1 is applied on side (vertex1, vertex2)

        Take care that tkinter ordinate axes is inverted to the standard euclidian ones.
        Point on the screen will be horizontally mirrored.
        Displayed points:

                    3
              color3/      \color2
                4       2
            color4|     |color1
                5       1
              color6\      /color6
                    6

        """
        size = self.hexaSize
        Δx = (size ** 2 - (size / 2) ** 2) ** 0.5

        point1 = (x + Δx, y + size / 2)
        point2 = (x + Δx, y - size / 2)
        point3 = (x, y - size)
        point4 = (x - Δx, y - size / 2)
        point5 = (x - Δx, y + size / 2)
        point6 = (x, y + size)
        # print(point1)
        # print(point2)
        # print(point3)
        # print(point4)
        # print(point5)
        # print(point6)

        # this setting allow to specify a different color for each side.
        if color1 == None:
            color1 = color
        if color2 == None:
            color2 = color
        if color3 == None:
            color3 = color
        if color4 == None:
            color4 = color
        if color5 == None:
            color5 = color
        if color6 == None:
            color6 = color

        self.create_line(point1, point2, fill=color1, width=1)
        self.create_line(point2, point3, fill=color2, width=1)
        self.create_line(point3, point4, fill=color3, width=1)
        self.create_line(point4, point5, fill=color4, width=1)
        self.create_line(point5, point6, fill=color5, width=1)
        self.create_line(point6, point1, fill=color6, width=1)
        if fill != None:
            self.create_polygon(point1, point2, point3, point4, point5, point6, fill=fill)
            Canvas.create_text(self, x, y, text=text, fill="black",
                               font=('Helvetica 20 bold'))  # todo todo


class HexagonalGrid(HexaCanvas):
    """ A grid whose each cell is hexagonal """

    def __init__(self, master, scale, grid_width, grid_height, *args, **kwargs):
        Δx = (scale ** 2 - (scale / 2.0) ** 2) ** 0.5
        width = 2 * Δx * grid_width + Δx
        height = 1.5 * scale * grid_height + 0.5 * scale

        HexaCanvas.__init__(self, master, background='white', width=width, height=height, *args, **kwargs)
        self.setHexaSize(scale)

    def setCell(self, xCell, yCell, txt=None, *args, **kwargs):
        """ Create a content in the cell of coordinates x and y. Could specify options throught keywords : color, fill, color1, color2, color3, color4; color5, color6"""

        # compute pixel coordinate of the center of the cell:
        size = self.hexaSize
        Δx = (size ** 2 - (size / 2) ** 2) ** 0.5

        pix_x = Δx + 2 * Δx * xCell
        if yCell % 2 == 1:
            pix_x += Δx

        pix_y = size + yCell * 1.5 * size

        self.create_hexagone(pix_x, pix_y, text=txt, *args, **kwargs)


#


#
if __name__ == "__main__":
    tk = Tk()

    grid = HexagonalGrid(tk, scale=50, grid_width=4, grid_height=4)
    grid.grid(row=0, column=0, padx=5, pady=5)

    # quit = Button(tk, text="Quit", command=lambda: correct_quit(tk))
    xAxisInput = Text(tk, height=2, width=2, bg="light yellow")
    yAxisInput = Text(tk, height=2, width=2, bg="light yellow")
    beeSelectBtn = Text(tk, height=2, width=2, bg="light yellow")
    # btn = Button(tk, height=2, text='submit move', bg = '#66ff66', command = onSubmitMove)
    xAxisInput.grid(row=10, column=10)
    yAxisInput.grid(row=10, column=9)
    beeSelectBtn.grid(row = 10, column = 8)
    # btn.grid(row=10, column=7)

    grid.setCell(0, 0, fill='green', txt="0 0")
    grid.setCell(0, 1, fill='green', txt="0 1")
    grid.setCell(1, 1, fill='yellow', txt="1 1")
    grid.setCell(2, 0, fill='cyan', txt="2 0")
    grid.setCell(0, 2, fill='teal', txt="0 2")
    grid.setCell(2, 1, fill='silver', txt="2 1")
    grid.setCell(1, 2, fill='white', txt="1 2")
    grid.setCell(1, 0, fill='gray', txt="1 0")

    tk.mainloop()
