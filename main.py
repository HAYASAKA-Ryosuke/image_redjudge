from PIL import Image
import numpy as np
width = 1674
height = 900 
#left=213
#center=427
#width = 500
#height = 404
left = width/3
center = (width/3)*2

im = Image.open("torero.png")
rgbimg = im.convert("RGB")
rgb = list(rgbimg.getdata())
data=[]
data = np.zeros((height,width,3), 'uint8')
print(data[0][0][0])
count=0
for i in range(0,height):
    for j in range(0,width):
        r=rgb[count][0]
        g=rgb[count][1]
        b=rgb[count][2]
        if (r>110 and g<100 and b<100):
            #print("r:"+str(r)+"g:"+str(g)+"b:"+str(b))
            data[i][j][0]=250
            data[i][j][1]=250
            data[i][j][2]=250
            #data[i][j][0]=rgb[count][0]
            #data[i][j][1]=rgb[count][1]
            #data[i][j][2]=rgb[count][2]
        else:
            data[i][j][0]=0
            data[i][j][1]=0
            data[i][j][2]=0
        count=count+1
leftcount=0
centercount=0
rightcount=0
for i in range(0,height):
    for j in range(0,width):
        if data[i][j][0]==250:
            if j<left:
                leftcount=leftcount+1
            if j>left and j<center:
                centercount=centercount+1
            if j>center:
                rightcount=rightcount+1
if leftcount>centercount and leftcount>rightcount:
        print("leftcount:"+str(leftcount))
if centercount>rightcount and centercount>leftcount:
        print("centercount:"+str(centercount))
if rightcount>centercount and rightcount>leftcount:
        print("rightcount:"+str(rightcount))
#pilImg = Image.fromarray(data)
#pilImg.show()

