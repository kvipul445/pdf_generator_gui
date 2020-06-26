from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
import os
import numpy as np

class pdf_process:

    def plotImage(self,f):
        im = imread(os.path.join("", f)).astype(np.float32) / 255
        plt.imshow(im)
        a = plt.gca()
        a.get_xaxis().set_visible(False) # We don't need axis ticks
        a.get_yaxis().set_visible(False)

    def selected_directory(self,select_dir,name_of_pdf_file,selected_files):
        path = str(select_dir)+'/'+str(name_of_pdf_file)+'.pdf'
        open(path,"w+")
        pp = PdfPages(path)

        for i in range(len(selected_files)):
            plt.subplot()
            pdf_process.plotImage(self,selected_files[i])
            pp.savefig(plt.gcf())
        
        pp.close()
