# Via 1-2 - Representacion integral de Xi y nucleo Phi

## Clasificacion

`hecho-demostrado` + `base-tecnica` + `puente-a-positividad-total`

Esta nota fija una normalizacion operacional para la representacion integral de la funcion Xi de Riemann y prepara la Via 2: positividad total del nucleo.

---

## 1. Funcion Xi

Partimos de

```math
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\left(\frac{s}{2}\right)\zeta(s)
```

y

```math
\Xi(z)=\xi\left(\frac12+iz\right).
```

Con esta convencion, RH equivale a que todos los ceros de `Xi(z)` sean reales.

---

## 2. Representacion integral normalizada

Usaremos la normalizacion compatible con el flujo de de Bruijn-Newman:

```math
H_t(z)=\int_0^\infty e^{t u^2}\Phi(u)\cos(zu)\,du.
```

Para `t=0`:

```math
H_0(z)=\int_0^\infty \Phi(u)\cos(zu)\,du.
```

Esta funcion coincide, salvo convenciones de normalizacion que deben comprobarse en cada fuente, con la funcion `Xi(z)` asociada a Riemann:

```math
H_0(z)=\Xi(z).
```

En este repositorio se adopta como convencion de trabajo:

```math
\Xi(z):=H_0(z).
```

Cualquier cambio de normalizacion debera registrarse explicitamente.

---

## 3. Nucleo Phi

La forma estandar del nucleo es

```math
\Phi(u)=\sum_{n=1}^{\infty}
\left(2\pi^2 n^4 e^{9u}-3\pi n^2 e^{5u}\right)
\exp\left(-\pi n^2 e^{4u}\right).
```

Este nucleo decrece superexponencialmente cuando `u -> +infty`.

La presencia de

```math
\exp(-\pi n^2 e^{4u})
```

hace que para `u` grande la serie sea extremadamente pequena.

---

## 4. Propiedades relevantes

### 4.1 Realidad

Para `u real`, `Phi(u)` es real.

### 4.2 Decrecimiento

`Phi(u)` decrece mas rapido que cualquier exponencial ordinaria cuando `u -> +infty`.

Esto permite que la integral

```math
\int_0^\infty \Phi(u)\cos(zu)\,du
```

defina una funcion entera en `z`.

### 4.3 Positividad puntual

La positividad puntual de `Phi(u)` es util, pero no basta para RH.

Punto critico:

```math
\Phi(u)>0 \not\Rightarrow \Xi(z) \text{ tiene solo ceros reales.}
```

Se necesita una propiedad mucho mas fuerte.

---

## 5. Puente hacia positividad total

La Via 2 propone estudiar nucleos como

```math
K(x,y)=\Phi(x+y)
```

para `x,y>0`.

La pregunta operacional es:

```math
\det\left[\Phi(x_i+y_j)\right]_{i,j=1}^m \ge 0
```

para todo

```math
0<x_1<\cdots<x_m,\qquad 0<y_1<\cdots<y_m.
```

Si una forma adecuada de positividad total se demostrara, podria conectarse con teoremas tipo Polya-Schoenberg-Karlin para forzar que transformadas de Fourier/coseno tengan ceros reales.

---

## 6. Cuidado logico

La cadena deseada seria:

```math
K(x,y)=\Phi(x+y) \text{ totalmente positivo}
```

```math
\Longrightarrow \Xi \in \text{Laguerre-Polya}
```

```math
\Longrightarrow \Xi \text{ tiene solo ceros reales}
```

```math
\Longrightarrow RH.
```

Pero actualmente el primer paso no esta demostrado en este proyecto.

Tampoco se ha demostrado todavia que la version exacta de positividad total requerida sea suficiente para `Xi in LP` sin condiciones adicionales.

Por tanto, la Via 2 queda como una conjetura intermedia investigable, no como prueba.

---

## 7. Primer experimento numerico

Definir una funcion truncada

```math
\Phi_N(u)=\sum_{n=1}^{N}
\left(2\pi^2 n^4 e^{9u}-3\pi n^2 e^{5u}\right)
\exp\left(-\pi n^2 e^{4u}\right).
```

Luego calcular determinantes pequenos:

```math
D_m=\det\left[\Phi_N(x_i+y_j)\right]_{i,j=1}^m.
```

Casos iniciales:

- `m=1,2,3`.
- mallas pequenas de `x_i,y_j` positivos.
- precision alta.

Objetivo experimental:

1. Buscar evidencia a favor o en contra de positividad total.
2. Detectar contraejemplos pequenos si existen.
3. Identificar si hay que modificar el nucleo, el dominio o la variable.

---

## 8. Riesgo principal

Aunque todos los determinantes numericos pequenos sean positivos, eso no prueba positividad total.

Aunque falle un truncamiento `Phi_N`, eso no implica que falle `Phi`.

Los experimentos solo sirven para orientar la busqueda de un lema demostrable.

---

## 9. Siguiente paso

Crear script reproducible:

```text
experiments/phi_total_positivity.py
```

con funciones:

- `phi(u, N)`
- `kernel_matrix(xs, ys, N)`
- `determinant_test(grid, m, N)`

Registrar resultados iniciales en:

```text
experiments/results_phi_total_positivity.md
```
