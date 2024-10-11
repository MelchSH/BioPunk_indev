from scipy.integrate import solve_ivp
from defaults import ODE_default_parameters
from parameters import ODE_user_parameters, Bioreactor_user_parameters

def get_Bioreactor_Parameters():
    try:
        Bioreactor_parameters = Bioreactor_user_parameters
    except ValueError as MissingParamsError:
        print(MissingParamsError)
        print("Missing or Failed to Load Parameters\n Loading Default Parameters")
    else:
        Bioreactor_parameters = Bioreactor_user_parameters

    return Bioreactor_parameters

def get_ODE_Parameters():
    try:
        ODE_parameters = ODE_user_parameters()
    except ValueError as MissingParamsError:
        print(MissingParamsError)
        print("Missing or Failed to Load Parameters\n Loading Default Parameters")
    else:
        ODE_parameters = ODE_default_parameters

    return ODE_parameters

def integrate_ode(ode_function,y0,parameters= get_ODE_Parameters):
    t_span = parameters.t_span
    t_eval = parameters.t_eval
    result = solve_ivp(ode_function, t_span, y0, t_eval=t_eval, method=parameters.method, rtol=parameters.rtol,atol=parameters.atol)

    return result

