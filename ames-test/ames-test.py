from graphics import*
# import pandas as pd

def main():
    # import csv file

    # test = pd.read_csv("tester.csv")
    # newtest = test.set_index("rows")
    # #
    # #
    # # # isolate specific variable; currently hardcoded
    # val = newtest.loc["row 2","col 1"]
    # print(val)

    #graphics section

    #     gui()
    #
    # def gui()
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


main()
