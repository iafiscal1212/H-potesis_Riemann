# Checklist de revision formal

Este documento sirve para revisar cualquier argumento matematico relacionado con RH.

## 1. Dominio de validez

- Verificar en que region es valida cada formula.
- No usar la serie de zeta fuera de `Re(s)>1` salvo que se trabaje con una continuacion valida.
- Indicar si una formula es local, global, asintotica o formal.

## 2. Convergencia

- Revisar convergencia absoluta.
- Revisar convergencia uniforme.
- Justificar intercambio de sumas, productos, limites e integrales.
- Distinguir entre igualdad puntual e igualdad en sentido de distribuciones.

## 3. Analisis complejo

- Controlar polos, ceros y residuos.
- Revisar multiplicidades.
- Controlar ramas del logaritmo complejo.
- Verificar orientacion de contornos y signos.

## 4. Circularidad

- Identificar si algun paso asume una consecuencia equivalente a RH.
- Marcar dependencias logicas.
- Separar equivalencias conocidas de pruebas independientes.

## 5. Evidencia numerica

- Registrar precision, parametros y librerias.
- No tratar verificacion finita como prueba general.
- Usar experimentos para generar conjeturas, no para cerrar demostraciones.

## 6. Simetria funcional

- La simetria `xi(s)=xi(1-s)` no implica por si sola que todos los ceros esten en la linea critica.
- Cualquier argumento basado en simetria debe incluir un mecanismo adicional que fuerce la localizacion.

## 7. Clasificacion final

Cada resultado revisado debe clasificarse como:

- `valido`
- `valido-condicional`
- `incompleto`
- `circular`
- `experimental`
- `incorrecto`
