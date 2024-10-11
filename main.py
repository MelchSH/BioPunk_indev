

### Import dependencies
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import tkinter as tk
from interface import *

if __name__ == "__main__":
    root = tk.Tk()
    app = Diagram_App(root)
    root.mainloop()


