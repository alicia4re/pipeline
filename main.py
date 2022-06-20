#from ModuloAnalisis.MCF_NET import Main_EyeQuality as mcf
#from ModuloAnalisis.EyeQ_preprocess import EyeQ_process_main as eyeQ

from ModuloAnalisis import *
import ModuloAnalisis.EyeQ_preprocess.EyeQ_process_main as eyeQ
import ModuloAnalisis.MCF_NET.Main_EyeQuality as mcf



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Analizamos las imágenes del dataset')
    eyeQ.runPreProcessEyeQ
    mcf.run_MCF_NET
    # Guardamos las imágenes en 3 carpetas según su calidad
    


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
