import cv2
import numpy as np
import sys
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QFileDialog
from PyQt5.QtWidgets import *
import os
from inpaint import inpaint_Func

run = False

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow,self).__init__()
    self.setGeometry(100,100,800,600)
    self.setWindowTitle("Main Window")
    self.originalImg=None
    self.imagePath=None
    self.setupUi()
  
  def setupUi(self):
    self.browseButton = QtWidgets.QPushButton(self)
    self.browseButton.setGeometry(QtCore.QRect(340, 260, 93, 28))
    self.browseButton.setObjectName("browseButton")
    self.text = QtWidgets.QLabel(self)
    self.text.setGeometry(QtCore.QRect(290, 240, 241, 16))
    self.text.setObjectName("text")
    self.filename = QtWidgets.QLineEdit(self)
    self.filename.setGeometry(QtCore.QRect(232, 300, 321, 22))
    self.filename.setObjectName("filename")
    self.openButton = QtWidgets.QPushButton(self)
        #(x,y,w,h)
    self.openButton.setGeometry(QtCore.QRect(340, 350, 93, 28))
    self.openButton.setObjectName("openButton")
    self.inpaintButton = QtWidgets.QPushButton(self)
       				 #(x,y,w,h)
    self.inpaintButton.setGeometry(QtCore.QRect(340, 500, 93, 28))
    self.inpaintButton.setObjectName("inpaintButton")
    self.retranslateUi()

  def retranslateUi(self):
    self.browseButton.setText("Browse")
    self.text.setText("Upload the image you want to edit")
    self.openButton.setText( "Open")
    self.browseButton.clicked.connect(self.buttonClicked)
    self.openButton.clicked.connect(self.openImageWindow)
    self.inpaintButton.setText( "Inpaint")
    self.inpaintButton.clicked.connect(self.inpaint)

  def buttonClicked(self):
    # print("hi")
    self.displayDialogeBox()

  def displayDialogeBox(self):
    #filepath leko 
    filepath=QFileDialog.getOpenFileName(main_win,'','',"PNG Files (*.png);;JPG Files(*.jpg)")
    #filename box ma filepath display gareko
    #filepath is a tuple so [0] gareko
    self.filename.setText(filepath[0])
    # print(filepath[0])
    self.imagePath=filepath[0]

  def inpaint(self):
      # print('3333')
      self.close()
      # inpaint_Func()
  
  def openImageWindow(self):
    # print(self.imagePath)
    self.originalImg = cv2.imread(self.imagePath)#loading image
    # image=self.originalImg
    # if image is not None:
    #       height,width,channel=image.shape
    #       print(height,width,channel)
    self.img = cv2.resize(self.originalImg, (512,512), interpolation = cv2.INTER_AREA)#resizng image to 512,512
    os.chdir(r'D:\bachelor\Minor\final project\images')
    cv2.imwrite("original.png", self.img)
    cv2.imshow('Masked Image',self.img)#Displaying original image
    self.blank = np.full((512,512,3), 255,dtype = 'uint8')
    cv2.setMouseCallback('Masked Image', self.select_region)#Mouse callback function
    while True:
        # print('1111')
        if cv2.waitKey(33) == 13: #13 is ascii of 'enter'
              #os.chdir(r'C:\Users\ACER\Desktop\Course Projects\Minor Project Resources\Git_Cloned Project Code(2080-11-25)\OcclusionRemoval-Image-Inpainting-\images')
              cv2.imwrite("BinaryMask.png", self.blank) # save image
              cv2.imwrite("MaskedImage.png", self.img) # save image
              
              cv2.destroyAllWindows()
              
              
              # print('2222')
              break
        
  def resizeOuputImage(self,output):
      # print('hi')
      image=self.originalImg
      if image is not None:
          height,width,channel=image.shape
          resizedOutput=output.resize((width,height))
          resizedOutput.save("finalOutput.jpg")
          resizedOutput.show()
          # print(height,width,channel) 
      else:
          print('Image not found')

  def select_region(self,event, x, y, flag, param):
    global run
    if event == cv2.EVENT_LBUTTONDOWN:
           run = True 
    if event == cv2.EVENT_LBUTTONUP:
          run = False
    if event == cv2.EVENT_MOUSEMOVE:
      if run == True:
                    cv2.circle(self.img, (x,y), 5 , (0,0,0), thickness = cv2.FILLED)
                    cv2.imshow('Masked Image',self.img)
                    cv2.circle(self.blank, (x,y), 5 , (0,0,0), thickness = cv2.FILLED)
                    #cv2.imshow('Binary Mask',self.blank)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_win=MainWindow()
    main_win.show()
    app.exec_()
    inpaint_Func(main_win)
       
  

#img_path = r'D:\6th sem\minor\project files\test projects\original.jpg'
########################## MAIN ############################################



#img = cv2.imread(img_path)#loading image

#img = cv2.resize(img, (512,512), interpolation = cv2.INTER_AREA)#resizng image to 512,512

#cv2.imshow('Masked Image',img)#Displaying original image

#blank = np.full((512,512,3), 255,dtype = 'uint8')

#cv2.setMouseCallback('Masked Image', select_region)#Mouse callback function

# while True:
# 	if cv2.waitKey(33) == ord('a'):
# 		cv2.imwrite("M.png", blank) # save image
# 		cv2.imwrite("MI.png", img) # save image

#cv2.waitKey(0)         














