import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from defaults import Bioreactor_default_parameters
from utils import get_Bioreactor_Parameters


class bioreactor_fed_monod():
    def __init__(self):
        pass
    
    def unpack_parameters(parameters= get_Bioreactor_Parameters):
        F0 = parameters.F0
        Mumax = parameters.Mumax
        Ks = parameters.Ks
        Sf = parameters.Sf
        Alpha = parameters.Alpha
        Beta = parameters.Beta
        Volmax = parameters.Volmax
        Sthreshold = parameters.Sthreshold
        Kd = parameters.Kd
        P_Kd = parameters.P_Kd
        Yxs = parameters.Yxs
        Vmin = parameters.Vmin
        
        return F0, Mumax, Ks, Sf, Alpha, Beta, Volmax, Sthreshold, Kd, P_Kd, Yxs, Vmin

    def monod(t,y,F0, Mumax, Ks, Sf, Alpha, Beta, Volmax, Sthreshold, X_Kd, P_Kd, Yxs, Vmin):

        X,S,P,V = y
        
        if S <= Sthreshold:
            F = F0
        else:
            F = 0
        if V >= Volmax:
            F = 0
        D = F/V

        V = max(V,Vmin)
        mu = Mumax*S/(Ks+S)
        dVdt = F
        dXdt = mu*X -D*X -X*X_Kd
        dSdt = -(mu*X)/Yxs + D*(Sf-S)
        if S > 0.01:
            dPdt = Alpha*mu*X + Beta*X
        else:
            dPdt = -P_Kd
        return [dXdt,dSdt,dPdt,dVdt]