# importing required libraries
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
  
# reading the image
testImage = img.imread('g4g.png')

fname = r'g4g.png'
image = Image.open(fname).convert("L")
  
# displaying the image
plt.imshow(testImage)
plt.show()