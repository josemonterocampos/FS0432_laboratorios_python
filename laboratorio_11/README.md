# Laboratorio 11
Estudiante: Jose Ricardo Montero Campos
Carné: C05005

## Requisitos

Tener instalado:

* Python 3
* NumPy
* Matplotlib

Instalar las bibliotecas necesarias:

```bash
pip install numpy matplotlib
```

## Ejecución

### Método de Jacobi

Ejecutar:

```bash
python poisson_2d_jacobi.py
```

o

```bash
py poisson_2d_jacobi.py
```

El programa genera:

* solucion_jacobi_heatmap.png
* solucion_exacta_heatmap.png
* error_absoluto_jacobi_heatmap.png
* error_convergencia_jacobi.png

Además imprime en pantalla el número de iteraciones, el error de convergencia final y el error máximo respecto a la solución exacta.

### Método de Gauss-Seidel

Ejecutar:

```bash
python poisson_2d_gauss_seidel.py
```

o

```bash
py poisson_2d_gauss_seidel.py
```

El programa genera:

* solucion_gauss_seidel_heatmap.png
* solucion_exacta_heatmap.png
* error_absoluto_gauss_seidel_heatmap.png
* error_convergencia_gauss_seidel.png

Además imprime en pantalla el número de iteraciones, el error de convergencia final y el error máximo respecto a la solución exacta.
