# Hipotesis de Riemann - Archivo de Investigacion

Repositorio de investigacion sobre la Hipotesis de Riemann.

## Estado

La Hipotesis de Riemann sigue siendo un problema abierto. Este repositorio no parte de una supuesta demostracion, sino de un programa ordenado para estudiar formulaciones equivalentes, rutas de ataque, experimentos reproducibles y posibles lemas intermedios.

## Enunciado

Sea

```math
\zeta(s)=\sum_{n=1}^{\infty}\frac{1}{n^s}
```

para `Re(s)>1`, extendida por continuacion analitica al plano complejo salvo el polo en `s=1`.

La Hipotesis de Riemann afirma:

```math
\zeta(\rho)=0,\quad 0<\operatorname{Re}(\rho)<1
\quad\Longrightarrow\quad
\operatorname{Re}(\rho)=\frac12.
```

Equivalente: todos los ceros no triviales de la funcion zeta estan sobre la linea critica.

## Principios de trabajo

1. Separar hechos demostrados, equivalencias conocidas, conjeturas intermedias, experimentos y especulaciones.
2. Evitar circularidad: ningun argumento puede asumir RH para probar RH.
3. Documentar vias fallidas con el mismo cuidado que vias prometedoras.
4. Mantener trazabilidad entre formulas, lemas, experimentos y posibles pruebas.
5. Tratar cualquier supuesto avance como borrador hasta auditoria formal.

## Estructura

```text
.
├── README.md
├── ROADMAP.md
├── docs/
│   ├── 00-context.md
│   └── 01-routes-catalog.md
├── log/
│   └── 2026-06-05-initialization.md
├── experiments/
│   └── README.md
└── notes/
    └── README.md
```

## Lineas iniciales de investigacion

1. Funcion Xi y clase de Laguerre-Polya.
2. Positividad total del nucleo de Riemann.
3. Representacion de Herglotz para `-Xi'/Xi`.
4. Programa espectral tipo Hilbert-Polya.
5. Flujo de de Bruijn-Newman.
6. Formula explicita y control del error en primos.
7. Criterios equivalentes: Li, Weil, Mobius y Chebyshev.
8. Aproximantes finitos, polinomios estables y modelos matriciales.
9. Auditoria de intentos de prueba.
