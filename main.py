from PIL import Image
import numpy as np


class JudgeGoal():
    def __init__(self, width=1674, height=900, selectcolor_judge=110, othercolor1_judge=100, othercolor2_judge=100):
        self.width = width
        self.height = height
        self.selectcolor_judge = selectcolor_judge
        self.othercolor1_judge = othercolor1_judge
        self.othercolor2_judge = othercolor2_judge

    def loadimage(self, filename):
        self.im = Image.open(filename)
        rgbimg = self.im.convert("RGB")
        self.rgb = list(rgbimg.getdata())

    def objectselect(self, colorname='red'):
        self.data = np.zeros((self.height, self.width, 3), 'uint8')
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if colorname == 'red':
                    selectcolor = self.rgb[count][0]
                    othercolor1 = self.rgb[count][1]
                    othercolor2 = self.rgb[count][2]
                if colorname == 'green':
                    othercolor1 = self.rgb[count][0]
                    selectcolor = self.rgb[count][1]
                    othercolor2 = self.rgb[count][2]
                if colorname == 'blue':
                    othercolor1 = self.rgb[count][0]
                    othercolor2 = self.rgb[count][1]
                    selectcolor = self.rgb[count][2]
                if (selectcolor > self.selectcolor_judge and othercolor1 < self.othercolor1_judge and othercolor2 < self.othercolor2_judge):
                    self.data[i][j][0] = 250
                    self.data[i][j][1] = 250
                    self.data[i][j][2] = 250
                else:
                    self.data[i][j][0] = 0
                    self.data[i][j][1] = 0
                    self.data[i][j][2] = 0
                count += 1

    def objectdirection(self):
        leftcount = 0
        centercount = 0
        rightcount = 0
        left = self.width/3
        center = (self.width/3)*2
        for i in range(self.height):
            for j in range(self.width):
                if self.data[i][j][0] == 250:
                    if j < left:
                        leftcount = leftcount+1
                    if j > left and j < center:
                        centercount = centercount+1
                    if j > center:
                        rightcount = rightcount+1
        if leftcount > centercount and leftcount > rightcount:
                print("leftcount:"+str(leftcount))
                return "left"
        if centercount > rightcount and centercount > leftcount:
                print("centercount:"+str(centercount))
                return "center"
        if rightcount > centercount and rightcount > leftcount:
                print("rightcount:"+str(rightcount))
                return "right"

    def imageshow(self):
        pilImg = Image.fromarray(self.data)
        pilImg.show()

