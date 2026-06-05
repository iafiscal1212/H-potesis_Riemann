# Roadmap

## Objetivo

Construir un archivo de investigacion ordenado sobre la Hipotesis de Riemann, con vias de ataque documentadas, experimentos reproducibles y criterios de auditoria.

## Fase 0 - Inicializacion

- [x] Crear repositorio.
- [x] Crear `README.md`.
- [x] Crear `ROADMAP.md`.
- [ ] Crear catalogo inicial de vias.
- [ ] Crear log inicial.
- [ ] Crear issues por via de investigacion.

## Fase 1 - Base comun

Documentar los objetos centrales:

- Funcion zeta.
- Producto de Euler.
- Continuacion analitica.
- Ecuacion funcional.
- Funcion xi y funcion Xi.
- Ceros triviales y no triviales.
- Formula explicita.
- Funcion de Chebyshev `psi(x)`.
- Funcion de von Mangoldt `Lambda(n)`.

## Fase 2 - Equivalencias

Documentar equivalencias verificables:

- RH y ceros reales de `Xi(t)`.
- RH y cota para `psi(x)-x`.
- RH y criterios de Weil.
- RH y criterios de Li.
- RH y cotas para la funcion de Mobius.
- RH y regiones libres de ceros.

## Fase 3 - Programas de ataque

Investigar una via cada vez:

1. Laguerre-Polya.
2. Positividad total.
3. Herglotz / Pick / Nevanlinna.
4. Hilbert-Polya espectral.
5. de Bruijn-Newman.
6. Control aritmetico mediante formula explicita.
7. Estabilidad de polinomios y aproximantes discretos.
8. Modelos matriciales hermiticos naturales.

## Fase 4 - Experimentos

Crear scripts y notebooks para:

- Evaluar numericamente el nucleo de Riemann `Phi(u)`.
- Calcular determinantes de positividad total.
- Construir aproximantes finitos de `Xi(t)`.
- Verificar estabilidad de polinomios discretizados.
- Comparar contra ceros conocidos.

## Fase 5 - Auditoria formal

Para cada avance:

- Identificar supuestos usados.
- Marcar si depende de RH.
- Revisar intercambio de limites, sumas e integrales.
- Revisar convergencia uniforme/absoluta.
- Revisar continuidad analitica y dominios.
- Revisar signos y ramas del logaritmo complejo.

## Clasificacion obligatoria de resultados

Todo resultado debe clasificarse como:

- `hecho-demostrado`
- `equivalencia-conocida`
- `conjetura-intermedia`
- `experimento-numerico`
- `idea-especulativa`
- `fallo-detectado`
