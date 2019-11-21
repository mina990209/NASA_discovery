import src/graphics.py

win = GraphWin("Ames Test", 500, 500)
# draw a box
rect = Rectangle(Point(125,125), Point(375, 375))
rect.setFill("red")
rect.draw(win)
# rect.setFill("red")
val_disp = Text(Point(250, 250), 42)
val_disp.draw(win)

win.getMouse()
win.close()
