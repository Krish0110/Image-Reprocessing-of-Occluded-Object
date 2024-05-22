import os
import matplotlib.pyplot as plt
from PIL import Image
import torch
import torch.nn.functional as F
import torchvision.transforms.functional as TF
import cv2
import numpy as np

from model import PConvUNet

from torchvision import transforms


resize = transforms.Resize(size = (512,512))
def inpaint_Func(main_win):

    os.chdir(r'D:\bachelor\Minor\final project')



    # Define the used device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


    # Define the model
    print("Loading the Model...")
    model = PConvUNet(layer_size=7)
    model.load_state_dict(torch.load('modelFile.pth', map_location=device)['model'])
    model.to(device)
    model.eval()

    # Loading Input and Mask
    print("Loading the inputs...")
    print(os.getcwd())


    os.chdir(r'D:\bachelor\Minor\final project\images')

    #org = Image.open('ronaldo.jpg')
    org = Image.open('original.png')


    #mask = Image.open('cv-gen1.png')
    #mask = Image.open('ronaldomask.png')
    #mask = Image.open('M.png')
    mask = Image.open('BinaryMask.png')

    '''image = cv2.imread('binaryImage.png')

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # define range of black color in HSV
    lower_val = np.array([0,0,0])
    upper_val = np.array([179,255,127])
    # Threshold the HSV image to get only black colors
    mask1 = cv2.inRange(hsv, lower_val, upper_val)
    # invert mask to get black symbols on white background
    mask2 = cv2.bitwise_not(mask1)
    height, width, channels = image.shape '''


    #image = Image.fromarray(mask2)
    org = TF.to_tensor(org.convert('RGB'))
    mask = TF.to_tensor(mask.convert('RGB')) 


    


    org = resize(org)
    mask =  resize(mask)

    inp = org * mask

    # Model prediction
    print("Model Prediction...")
    with torch.no_grad():
        inp_ = inp.unsqueeze(0).to(device)
        mask_ = mask.unsqueeze(0).to(device)
        
        raw_out, raw_mask = model(inp_, mask_)
        #raw_out, raw_mask = model(raw_out, mask_)


    # Post process
    raw_out = raw_out.to(torch.device('cpu'))
    raw_out = raw_out.clamp(0.0, 1.0)
    out = mask * inp + (1 - mask) * raw_out
    out1 = TF.to_pil_image(out.cpu().detach()[0])
    out1.save("out1.jpg")

    # plt.imshow(org.cpu().detach().permute(1,2,0))
    # plt.show()

    # plt.imshow(inp.cpu().detach().permute(1,2,0))
    # plt.show()

    plt.imshow(out.cpu().detach()[0].permute(1,2,0))
    plt.show()
    outputResize(out1,main_win)

def outputResize(out1,main_win):
    main_win.resizeOuputImage(out1)

#inpaint_Func()



