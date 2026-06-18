import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# -----------------------------
# Parametros fisicos y numericos
# -----------------------------

Lx = 1.0
Ly = 1.0

Nx = 50
Ny = 50

kappa = 1.0

h = Lx / Nx

r = 0.20
t_final = 0.1
snapshot_interval = 20

# Calculo de dt y numero de pasos

dt = r * h**2 / kappa
num_steps = int(t_final / dt)


# -----------------------------
# Condicion inicial
# -----------------------------

u = np.zeros((Nx + 1, Ny + 1))

# -----------------------------
# Condiciones de frontera
# -----------------------------

def aplicar_frontera(u):

    # Bordes izquierdo y derecho
    u[0, :] = 10.0
    u[Nx, :] = 10.0

    # Bordes inferior y superior
    u[:, 0] = 5.0
    u[:, Ny] = 5.0


aplicar_frontera(u)


# -----------------------------
# Evolucion temporal
# -----------------------------

snapshots = []
tiempos = []

u_new = np.copy(u)

for n in range(num_steps + 1):

    # Guardar snapshots y tiempos

    if n % snapshot_interval == 0:
        snapshots.append(np.copy(u))
        tiempos.append(n * dt)

    # Actualizacion explicita

    for i in range(1, Nx):
        for j in range(1, Ny):

            u_new[i, j] = (
                u[i, j]
                + r * (
                    u[i + 1, j]
                    + u[i - 1, j]
                    + u[i, j + 1]
                    + u[i, j - 1]
                    - 4.0 * u[i, j]
                )
            )

    # Aplicar condiciones de frontera

    aplicar_frontera(u_new)

    # Preparar siguiente iteracion

    u, u_new = u_new, u


# -----------------------------
# Animacion
# -----------------------------

fig, ax = plt.subplots(figsize=(6, 5))

im = ax.imshow(
    snapshots[0].T,
    origin="lower",
    extent=[0, Lx, 0, Ly],
    cmap="hot",
    vmin=0.0,
    vmax=np.max(snapshots[-1])
)

cbar = plt.colorbar(im, ax=ax)
cbar.set_label("Temperatura")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Ecuacion de calor 2D")

time_text = ax.text(
    0.02,
    0.95,
    "",
    transform=ax.transAxes,
    color="white",
    fontsize=11,
    verticalalignment="top"
)


def actualizar(frame):
    im.set_data(snapshots[frame].T)
    time_text.set_text(f"t = {tiempos[frame]:.4f}")
    return im, time_text


anim = FuncAnimation(
    fig,
    actualizar,
    frames=len(snapshots),
    interval=80,
    blit=True
)

anim.save("calor_2d.gif", writer="pillow", fps=15)

print("dt =", dt)
print("num_steps =", num_steps)
print("Snapshots almacenados =", len(snapshots))
print("Animacion guardada como calor_2d.gif")

plt.show()