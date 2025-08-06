import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, lambdify
from matplotlib import cm

def back(user):
    if not user.strip():
        raise ValueError("Input is empty.")
    try:
        expr = sympify(user)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")
    
    variables = list(expr.free_symbols)
    variables.sort(key=lambda s: s.name)
    return variables, expr

def D2(variables, expression, xrange):
    f = lambdify(variables, expression, 'numpy')
    x_vals = np.linspace(xrange[0], xrange[1], 100)
    y_vals = f(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals)
    ax.grid()
    ax.set_title(f"Graph of {expression}")
    return fig

def D3(variables, expression, xrange, yrange):
    f = lambdify(variables, expression, 'numpy')
    x_vals = np.linspace(xrange[0], xrange[1], 100)
    y_vals = np.linspace(yrange[0], yrange[1], 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = f(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"Surface of {expression}")
    return fig