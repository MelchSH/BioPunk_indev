import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_Bioreactor_Parameters

class bioreactor_batch_monod():   
    def __init__(self) -> None:
        pass

    def unpack_parameters(parameters=get_Bioreactor_Parameters):
        Mumax = parameters.Mumax
        Ks = parameters.Ks
        X_Kd = parameters.X_Kd
        Yxs = parameters.Yxs

    def monod(t,y,Mumax,Ks,X_Kd,Yxs):
        X, S = y
        if S > 0.01:
            Mu = Mumax*(S/(Ks+S))
        else:
            Mu = 0
        dXdt = (Mu*X)-(X*X_Kd)
        if S > 0.01:
            dSdt = -dXdt/Yxs
        else: 
            dSdt = 0
        S = max(S + dSdt, 0)

        return [dXdt, dSdt]

    





