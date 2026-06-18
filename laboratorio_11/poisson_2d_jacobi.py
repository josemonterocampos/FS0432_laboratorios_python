# poisson_2d_jacobi.py
#
# Laboratorio 11
# Ecuacion de Poisson 2D usando el metodo de Jacobi

import numpy as np
import matplotlib.pyplot as plt


def fuente(x, y):
    return np.sin(np.pi * x) * np.sin(np.pi * y)


def solucion_exacta(x, y):
    return -np.sin(np.pi * x) * np.sin(np.pi * y) / (2.0 * np.pi**2)


def error_maximo(u, u_exacta):
    return np.max(np.abs(u - u_exacta))


def graficar_mapa(u, titulo, nombre_archivo):
    plt.figure(figsize=(6, 5))

    plt.imshow(
        u.T,
        origin="lower",
        extent=[0, 1, 0, 1],
        cmap="viridis"
    )

    plt.colorbar(label="u(x,y)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(titulo)
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=200)


def graficar_error_convergencia(errores, nombre_archivo):
    plt.figure(figsize=(6, 4))
    plt.plot(errores)
    plt.xlabel("Iteracion")
    plt.ylabel("Error de convergencia")
    plt.title("Error de convergencia")
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=200)


def main():

    N = 50
    h = 1.0 / N
    tol = 1e-8
    max_iter = 200000

    x = np.linspace(0.0, 1.0, N + 1)
    y = np.linspace(0.0, 1.0, N + 1)

    X, Y = np.meshgrid(x, y, indexing="ij")

    f = fuente(X, Y)
    u_exacta = solucion_exacta(X, Y)

    u = np.zeros((N + 1, N + 1))
    u_new = np.zeros((N + 1, N + 1))

    errores_convergencia = []

    iteracion = 0
    error_conv = 1.0

    while error_conv > tol and iteracion < max_iter:

        # Metodo de Jacobi
        for i in range(1, N):
            for j in range(1, N):

                u_new[i, j] = 0.25 * (
                    u[i + 1, j]
                    + u[i - 1, j]
                    + u[i, j + 1]
                    + u[i, j - 1]
                    - h**2 * f[i, j]
                )

        # Error de convergencia
        error_conv = np.max(
            np.abs(
                u_new[1:N, 1:N]
                - u[1:N, 1:N]
            )
        )

        errores_convergencia.append(error_conv)

        # Copiar puntos interiores
        u[1:N, 1:N] = u_new[1:N, 1:N]

        iteracion += 1

    error_exacto = error_maximo(u, u_exacta)

    print("Metodo: Jacobi 2D")
    print("N =", N)
    print("h =", h)
    print("Tolerancia =", tol)
    print("Iteraciones =", iteracion)
    print("Error de convergencia final =", error_conv)
    print("Error maximo respecto a la solucion exacta =", error_exacto)

    error_absoluto = np.abs(u - u_exacta)

    graficar_mapa(
        u,
        "Jacobi 2D: solucion numerica",
        "solucion_jacobi_heatmap.png"
    )

    graficar_mapa(
        u_exacta,
        "Poisson 2D: solucion exacta",
        "solucion_exacta_heatmap.png"
    )

    graficar_mapa(
        error_absoluto,
        "Error absoluto",
        "error_absoluto_jacobi_heatmap.png"
    )

    graficar_error_convergencia(
        errores_convergencia,
        "error_convergencia_jacobi.png"
    )

    plt.show()


if __name__ == "__main__":
    main()