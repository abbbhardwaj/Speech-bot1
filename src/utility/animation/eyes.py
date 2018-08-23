from utility.animation.graphics import *


class EYE:

    @staticmethod
    def eyes():
        win = GraphWin("My Window", 500, 500)
        win.setBackground("Black")
        img1 = "utility/animation/rob3.gif"
        img2 = "utility/animation/rob2.gif"
        img3 = "utility/animation/close.gif"
        images = [img1, img1, img1, img1, img1, img1, img1, img1, img1, img3, img1, img1, img1, img1, img1, img1, img1
                  , img1, img3, img1, img1, img1]
        while True:
            for i in images:
                img = Image(Point(250, 250), i)
                img.draw(win)
                time.sleep(.2)
        time.sleep(20)
        win.getMouse()
        win.close()





