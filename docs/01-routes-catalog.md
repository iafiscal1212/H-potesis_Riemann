# Catalogo inicial de vias de investigacion

Este catalogo registra vias posibles para investigar RH. Cada via se clasifica por objetivo, idea, riesgo de circularidad y primer paso operativo.

## Via 1 - Laguerre-Polya

**Tipo:** equivalencia estructural.

**Idea:** Definir

```math
\Xi(t)=\xi\left(\frac12+it\right).
```

RH equivale a que `Xi(t)` tenga solo ceros reales. Una funcion entera real con solo ceros reales pertenece, bajo condiciones adecuadas, a la clase de Laguerre-Polya.

**Objetivo:** Demostrar que `Xi` pertenece a la clase de Laguerre-Polya.

**Ruta posible:** Construir aproximantes `Xi_N(t)` con solo ceros reales y probar convergencia local uniforme a `Xi(t)`.

**Riesgo:** Alto. Probar que los aproximantes naturales tienen solo ceros reales puede ser tan dificil como RH.

**Primer paso:** Documentar definicion de la clase Laguerre-Polya y criterios de pertenencia.

---

## Via 2 - Positividad total del nucleo de Riemann

**Tipo:** conjetura intermedia.

**Idea:** La funcion `Xi` admite una representacion tipo transformada de Fourier/coseno:

```math
\Xi(t)=\int_{-\infty}^{\infty}\Phi(u)e^{itu}\,du.
```

Si el nucleo `Phi` o un nucleo asociado como `K(x,y)=Phi(x+y)` tuviera positividad total fuerte, podria forzar ceros reales de la transformada.

**Objetivo:** Investigar si `K(x,y)=Phi(x+y)` es totalmente positivo.

**Riesgo:** Muy alto. La positividad de `Phi` no implica positividad total.

**Primer paso:** Escribir formula exacta del nucleo `Phi(u)` y calcular determinantes pequenos numericamente.

---

## Via 3 - Representacion de Herglotz para `-Xi'/Xi`

**Tipo:** criterio analitico.

**Idea:** Si se prueba que

```math
-\frac{\Xi'(z)}{\Xi(z)}
```

es una funcion de Herglotz/Pick en el semiplano superior, entonces los ceros de `Xi` deberian estar en el eje real, bajo condiciones tecnicas de crecimiento.

**Objetivo:** Encontrar una representacion integral positiva para la derivada logaritmica.

**Riesgo:** Alto. Una representacion positiva probablemente sea equivalente a RH.

**Primer paso:** Documentar el criterio de Herglotz y estudiar la derivada logaritmica de productos canonicos con ceros reales.

---

## Via 4 - Hilbert-Polya espectral

**Tipo:** programa estructural.

**Idea:** Si las partes imaginarias de los ceros,

```math
\rho=\frac12+i\gamma,
```

fueran valores propios de un operador autoadjunto, entonces los `gamma` serian reales y RH quedaria explicada estructuralmente.

**Objetivo:** Buscar operadores naturales construidos desde primos, zeta, theta o formula explicita.

**Riesgo:** Muy alto. No se conoce el operador.

**Primer paso:** Definir criterios minimos que un operador candidato debe satisfacer.

---

## Via 5 - Flujo de de Bruijn-Newman

**Tipo:** deformacion analitica.

**Idea:** Se estudia una familia deformada `Xi_lambda`. Existe una constante de de Bruijn-Newman `Lambda` tal que los ceros son reales para ciertos valores del parametro. RH equivale a una desigualdad sobre esa constante.

**Objetivo:** Entender RH como problema de estabilidad bajo flujo de calor.

**Riesgo:** Alto. Resultados conocidos indican que el caso critico es extremadamente delicado.

**Primer paso:** Documentar la definicion de `Xi_lambda` y la equivalencia con RH.

---

## Via 6 - Formula explicita y control aritmetico

**Tipo:** equivalencia aritmetica.

**Idea:** RH equivale a cotas fuertes para el error en la distribucion de primos, por ejemplo

```math
\psi(x)=x+O(\sqrt{x}\log^2 x).
```

**Objetivo:** Investigar si puede probarse la cota del error sin asumir localizacion de ceros.

**Riesgo:** Alto. El uso directo de la formula explicita suele ser circular.

**Primer paso:** Documentar con detalle la derivacion de la formula explicita y los puntos donde aparece circularidad.

---

## Via 7 - Criterios de Li, Weil y Mobius

**Tipo:** equivalencias conocidas.

**Idea:** RH tiene muchas formulaciones equivalentes en terminos de positividad o crecimiento de funciones aritmeticas.

**Objetivo:** Catalogar criterios equivalentes y buscar cual ofrece la estructura mas atacable.

**Riesgo:** Medio-alto. Las equivalencias no resuelven RH por si solas.

**Primer paso:** Crear fichas independientes para criterios de Li, Weil y sumas de Mobius.

---

## Via 8 - Aproximantes finitos y polinomios estables

**Tipo:** experimental/estructural.

**Idea:** Construir aproximaciones discretas de `Xi` mediante polinomios o polinomios exponenciales. Si los aproximantes son estables o tienen solo ceros reales y convergen correctamente, RH seguiria.

**Objetivo:** Encontrar aproximantes naturales no circulares.

**Riesgo:** Alto. Los truncamientos ingenuos suelen introducir ceros complejos.

**Primer paso:** Comparar truncamientos del nucleo, discretizaciones por cuadratura y aproximantes desde theta.

---

## Via 9 - Auditoria de supuestas pruebas

**Tipo:** control de calidad.

**Idea:** Muchos intentos fallan por errores recurrentes: uso indebido de series fuera de dominio, intercambio de limites, simetria mal interpretada, ramas del logaritmo o circularidad.

**Objetivo:** Construir una lista de chequeo para evaluar cualquier avance propio o externo.

**Riesgo:** Bajo. Es una via de higiene metodologica, no una prueba.

**Primer paso:** Crear checklist formal de auditoria.
