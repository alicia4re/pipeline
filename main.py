#from ModuloAnalisis.MCF_NET import Main_EyeQuality as mcf
#from ModuloAnalisis.EyeQ_preprocess import EyeQ_process_main as eyeQ

from ModuloAnalisis import *
import ModuloAnalisis.EyeQ_preprocess.EyeQ_process_main as eyeQ
import ModuloAnalisis.MCF_NET.Main_EyeQuality as mcf
from ModuloAnalisis.EyeQ_preprocess.fundus_prep import *

import sys
sys.path.insert(1, './ModuloANalisis/MCF_NET/')
from progress.bar import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Analizamos las imágenes del dataset')
    eyeQ.runPreProcessEyeQ()
    mcf.run_MCF_NET()
    # Guardamos las imágenes en 3 carpetas según su calidad
    


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from shutil import copy
import pandas as pd
import os
# crear folder -> os.makedirs("pepe/alfonso/") te crea los folders pepe y alfonso
df = pd.read_csv("/dev/ds../nombre.csv")
for row in df.values():
    row[1]["good"]
    max_label = np.argmax([0.1,0.2,0.3])
    #if max_label==1
        # shutil.copy("../row[1]["image_name"]","/")

