from dataclasses import dataclass
from typing import Tuple,List,Optional

@dataclass
class Bioreactor_default_parameters:
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
    Sf: float = 70
    Alpha: float = 0.3
    Beta: float = 0.05
    Volmax: float = 7
    Vmin: float = 1e-6

@dataclass
class ODE_default_parameters:
    method: str = "LSODA"
    t_span: Tuple[float,float] = (0, 10) #hrs
    t_eval: Optional[List[float]] = None
    rtol: float = 1e-3
    atol: float = 1e-6

from main import *


