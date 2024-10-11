import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from defaults import Bioreactor_default_parameters

class bioreactor_continous_monod():
    def __init__(self):
        pass

    def monod(y,t, F, V, Ks,Kd,mumax,Ysx,Sin):
        X, S = y
        mu = mumax *(S/(Ks+S))
        D = F/V
        dXdt = (mu-D)*X -(X*Kd)
        dSdt = D*(Sin-S)-(mu/Ysx)*X
        return [dXdt,dSdt]
