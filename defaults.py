from main import *
from dataclasses import dataclass

@dataclass
class Base_Bioreactor_Arguments():
    Mumax: float = 0.5
    Ks: float = 0.1
    X_Kd: float = 0.01
    S_Kd: float = 0
    P_Kd: float = 0.1
    Yxs: float = 0.4
    X0: float = 0.1
    S0: float = 10.0
    V0: float = 1
    P0: float = 0
    F0: float = 0
    V: float = V0
    X_in: float = 0
    X_out: float = 0
    S_in: float = 0
    S_out: float = 0



