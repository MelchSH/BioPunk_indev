import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from defaults import Base_Bioreactor_Arguments

print(Base_Bioreactor_Arguments())

class bioreactor_monod():   
    def __init__(self):
        pass
    def monod(t,y,Mumax,X_Kd):
        X,S,P = y

        Mu = Mumax*X - X*X_Kd



