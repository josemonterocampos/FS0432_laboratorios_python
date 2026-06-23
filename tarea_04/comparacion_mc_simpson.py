import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt
import time

d = 3  # dimensión del problema
valor_analitico = (2.0 / np.pi)**d


print(f"--- Integración en d={d} ---")
print(f"Analítico:   {valor_analitico:.8f}")

# ---------------------------------------------------------
# MÉTODO DE MONTE CARLO
# ---------------------------------------------------------

N_total_mc = 10**6


t0_mc = time.time()

# Generar N_total_mc puntos aleatorios en dimensión d
x = np.random.uniform(0.0, 1.0, size=(N_total_mc, d))

# Evaluar el integrando en cada punto
f = np.prod(np.sin(np.pi * x), axis=1)

# Estimación Monte Carlo
integral_mc = np.mean(f)

t1_mc = time.time()
error_mc = abs(integral_mc - valor_analitico)   

print(
    f"Monte Carlo: {integral_mc:.8f} "
    f"(Error: {error_mc:.8f}, Tiempo: {t1_mc - t0_mc:.4f}s)"
)

# ---------------------------------------------------------
# MÉTODO DE SIMPSON
# ---------------------------------------------------------

N_simpson = 10
N_total_simpson = N_simpson**d

t0_simpson = time.time()

x_1d = np.linspace(0, 1, N_simpson)
malla = np.meshgrid(*[x_1d] * d, indexing="ij")

Z = np.prod([np.sin(np.pi * m) for m in malla], axis=0)

integral_simpson = Z
for _ in range(d):
    integral_simpson = simpson(integral_simpson, x=x_1d, axis=0)

t1_simpson = time.time()
error_simpson = abs(integral_simpson - valor_analitico)

print(
    f"Simpson:     {integral_simpson:.8f} "
    f"(Error: {error_simpson:.8f}, Tiempo: {t1_simpson - t0_simpson:.4f}s)"
)

N_simpson = 10

for d in range(1, 8):

    valor_analitico = (2/np.pi)**d

    N_total = N_simpson**d

    print(f"\nd = {d}")
    print(f"Puntos totales = {N_total:,}")

    try:

        t0 = time.time()

        x_1d = np.linspace(0, 1, N_simpson)

        malla = np.meshgrid(
            *[x_1d]*d,
            indexing="ij"
        )

        Z = np.prod(
            [np.sin(np.pi*m) for m in malla],
            axis=0
        )

        integral = Z

        for _ in range(d):
            integral = simpson(
                integral,
                x=x_1d,
                axis=0
            )

        t1 = time.time()

        error = abs(
            integral - valor_analitico
        )

        print(
            f"Integral = {integral:.8e}"
        )

        print(
            f"Error = {error:.3e}"
        )

        print(
            f"Tiempo = {t1-t0:.4f} s"
        )

    except Exception as e:

        print("No fue posible continuar")
        print(e)

        break

dimensiones = [1, 2, 4, 8, 16, 32]

errores_mc = []
tiempos_mc = []

N_mc = 100000

for d in dimensiones:

    valor_analitico = (2/np.pi)**d

    t0 = time.time()

    x = np.random.uniform(0, 1, (N_mc, d))
    f = np.prod(np.sin(np.pi*x), axis=1)
    integral_mc = np.mean(f)

    t1 = time.time()

    errores_mc.append(abs(integral_mc - valor_analitico))
    tiempos_mc.append(t1 - t0)

    print(
        f"d={d:2d} "
        f"I={integral_mc:.8e} "
        f"Error={errores_mc[-1]:.3e} "
        f"Tiempo={tiempos_mc[-1]:.4f}s"
    )

plt.figure(figsize=(8,5))
plt.semilogy(dimensiones, errores_mc, 'o-')
plt.xlabel("Dimensión")
plt.ylabel("Error absoluto")
plt.title("Monte Carlo")
plt.grid(True)
plt.show()