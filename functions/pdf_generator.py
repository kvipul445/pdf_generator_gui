from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
import os
import numpy as np

files = [  "Famous-Quotes-About-Life-11.jpg" , "download.jpg"]
def plotImage(f):
    im = imread(os.path.join("", f)).astype(np.float32) / 255
    plt.imshow(im)
    a = plt.gca()
    a.get_xaxis().set_visible(False) # We don't need axis ticks
    a.get_yaxis().set_visible(False)

pdf_file = open("page1.pdf","w+")
pp = PdfPages("page1.pdf")
for i in range(len(files)):
    plt.subplot()
    plotImage(files[i])
    pp.savefig(plt.gcf())
pp.close()