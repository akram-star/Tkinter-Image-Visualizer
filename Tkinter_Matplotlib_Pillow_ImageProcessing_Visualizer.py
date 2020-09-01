import numpy as np

import matplotlib.pyplot as plotter


import tkinter as Filetracker
from tkinter import filedialog,Text,Tk

import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

root = Filetracker.Tk(screenName='IMG')

root.title("IMAGE PROCESSING VISUALIZATION")

apps =[]


def openApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File(s)",
                                      filetypes=(("executables", "*.exe"), ("All Files", "*.*")))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = Filetracker.Label(frame, text=app, bg="red")
        label.pack()

def runApp():
    for app in apps:
        os.startfile(app)


def Img_Visulaizer():
    img = mpimg.imread('pizza.jpg')
    def Matplotlib_Visulaixer():
        # reading the image and projecting it graphically


        image_plot = plt.imshow(img)
        print(image_plot)

        plt.show()
    '''def Array_Image():
        #reading the image and printing it as an array
        img = mpimg.imread('download.jpg')
        print(img)'''
    def Rainbow():
        # Can we make it rainbow???????????
        lum_img = img[:, :, 0]
        plt.imshow(lum_img)
        plt.imshow(lum_img, cmap="rainbow")
        plt.colorbar()
        plt.show()
    def Grey_Image():
        # image read function
        img = mpimg.imread('pizza.jpg')
        # image sclicing into 2D.
        x = img[:, :, 0]
        # x co-ordinate denotation.
        plt.xlabel("Value")
        # y co-ordinate denotation.
        plt.ylabel("pixels Frequency")
        # title of an image .
        plt.title("Original Image")
        # imshow function with comperision of gray level value.
        plt.imshow(x, cmap="gray")
        # plot the image on a plane.
        plt.show()
    def Histogramm():
        # image read function
        img = mpimg.imread('pizza.jpg')
        # image sclicing into 2D.
        x = img[:, :, 0]
        # x co-ordinate denotation.
        plt.xlabel("Value")
        # y co-ordinate denotation.
        plt.ylabel("pixels Frequency")
        # title of an image .
        plt.title("Original Image")
        plt.title("Histogram for given Image'  ")
        plt.xlabel("Value")
        plt.ylabel("pixels Frequency")
        # hist function is used to plot the histogram of an image.
        plt.hist(x)
        plt.show()



    fot = Filetracker.Button(root, width=20, text="Matplotlib_Visulaixer", command=Matplotlib_Visulaixer)
    fot.pack()
    
    #Array_Image_1 = Filetracker.dialog()
    #Array_Image_1.pack()

    rain_bow= Filetracker.Button(root, width=20, text="Rainbow Image", command=Rainbow)
    rain_bow.pack()

    Grey_Image_1 = Filetracker.Button(root, width=20, text="Grey Image", command=Grey_Image)
    Grey_Image_1.pack()

    Histogramm1 = Filetracker.Button(root, width=20, text="Histogram", command=Histogramm)
    Histogramm1.pack()



canvas = Filetracker.Canvas(root, height=400, width=400, background="aquamarine")
canvas.pack()

frame = Filetracker.Frame(root, bg="orange")
frame.place(relheight=0.5, relwidth=0.5, relx=0.2, rely=0.2)

#open = Filetracker.Button(root, width=10, text="App Open", command=openApp)
#open.pack()

#run = Filetracker.Button(root, width=10, text="App Run", command=runApp)
#run.pack()

#fot = Filetracker.Button(root, width=20, text="Fourier's Transform", command=ft)
#fot.pack()

#toptions = Filetracker.Button(root, width=30, text="Fourier's Transform Visualization", command=ft_options)
#ftoptions.pack()

MV = Filetracker.Button(root, width=20, text="IMAGE VISUALIZER", command=Img_Visulaizer)
MV.pack()



for app in apps:
    l = Filetracker.Button(frame, text=apps.seek, width=10, command=runApp)
    l.pack()

root.mainloop(n=0)

