# Contexto matematico

## Advertencia inicial

La Hipotesis de Riemann, abreviada RH, sigue abierta. Este archivo distingue entre:

- hechos demostrados;
- equivalencias conocidas;
- conjeturas intermedias;
- experimentos numericos;
- ideas especulativas.

Ninguna via debe presentarse como demostracion hasta superar una auditoria formal completa.

## Funcion zeta

La funcion zeta de Riemann se define inicialmente por

```math
\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}
```

para

```math
\operatorname{Re}(s)>1.
```

En esta region tambien se tiene el producto de Euler:

```math
\zeta(s)=\prod_p\frac{1}{1-p^{-s}},
```

donde `p` recorre los numeros primos.

Este producto conecta la zeta con la factorizacion unica de los enteros.

## Continuacion analitica

La serie original no converge en la franja critica

```math
0<\operatorname{Re}(s)<1.
```

Por tanto, RH solo se formula correctamente usando la continuacion analitica de `zeta(s)`, que es meromorfa en el plano complejo y tiene un polo simple en `s=1`.

## Funcion xi

Se define

```math
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\left(\frac{s}{2}\right)\zeta(s).
```

La funcion `xi` satisface la ecuacion funcional simetrica

```math
\xi(s)=\xi(1-s).
```

La linea critica

```math
\operatorname{Re}(s)=\frac12
```

es el eje natural de esta simetria.

## Funcion Xi

Definimos

```math
\Xi(t)=\xi\left(\frac12+it\right).
```

RH equivale a que todos los ceros de `Xi(t)`, considerada como funcion entera de la variable compleja `t`, sean reales.

## Formula explicita

La funcion de von Mangoldt es

```math
\Lambda(n)=
\begin{cases}
\log p, & n=p^k,\\
0, & \text{en otro caso}.
\end{cases}
```

La funcion de Chebyshev es

```math
\psi(x)=\sum_{n\le x}\Lambda(n).
```

La derivada logaritmica de la zeta satisface, para `Re(s)>1`,

```math
-\frac{\zeta'(s)}{\zeta(s)}=\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n^s}.
```

Mediante la formula de Perron y desplazamiento de contorno se obtiene, en forma simplificada,

```math
\psi(x)=x-\sum_\rho \frac{x^\rho}{\rho}+\text{terminos conocidos menores},
```

donde `rho` recorre los ceros no triviales de `zeta(s)`.

## Interpretacion

Si

```math
\rho=\beta+i\gamma,
```

entonces

```math
x^\rho=x^\beta e^{i\gamma\log x}.
```

La parte real `beta` controla el tamano de la oscilacion que ese cero introduce en el conteo ponderado de primos.

RH afirma que siempre

```math
\beta=\frac12.
```

## Equivalencia aritmetica central

Una forma equivalente, en terminos generales, es

```math
\psi(x)=x+O(\sqrt{x}\log^2 x).
```

Esta cota expresa que el error en la distribucion ponderada de los primos es casi del menor tamano posible dentro de este marco.
