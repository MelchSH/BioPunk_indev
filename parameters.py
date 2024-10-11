from dataclasses import dataclass
from typing import Tuple,List,Optional

@dataclass
class Bioreactor_user_parameters:
    Mumax: float
    Ks: float
    X_Kd: float
    S_Kd: float
    P_Kd: float
    Yxs: float
    X0: float
    S0: float
    V0: float
    P0: float
    F0: float
    V: float 
    X_in: float
    X_out: float
    S_in: float
    S_out: float
    Sf: float
    Alpha: float
    Beta: float
    Volmax: float
    Vmin: float


@dataclass
class ODE_user_parameters:
    method: str
    t_span: Tuple[float,float] #hrs
    t_eval: Optional[List[float]]
    rtol: float
    atol: float

from main import *


