import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_Bioreactor_Parameters

class bioreactor_continous_monod():
    def __init__(self):
        pass

    def unpack_parameters(parameters=get_Bioreactor_Parameters):
        Mumax = parameters.Mumax
        Ks = parameters.Ks
        X_Kd = parameters.X_Kd
        Yxs = parameters.Yxs
        S_in = parameters.S_in
        S_out = parameters.S_out #Used only on specific cases, S_in == S_out, F_in == F_out
        F = parameters.F0

    def monod(y,t, F, V, Ks,Kd,mumax,Yxs,S_in):
        X, S = y
        mu = mumax *(S/(Ks+S))
        D = F/V
        dXdt = (mu-D)*X -(X*Kd)
        dSdt = D*(S_in-S)-(mu/Yxs)*X
        return [dXdt,dSdt]
