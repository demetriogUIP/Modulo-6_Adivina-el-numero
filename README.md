# Modulo-6_Adivina-el-numero

Este proyecto desarrolla un juego interactivo de adivinanza de números en Python.

---

## 💡 Breve Resumen del Proyecto

El proyecto es un juego de adivinanza que genera un número secreto entre 1 y 20. El jugador dispone de **5 intentos** para adivinarlo. La aplicación ofrece pistas ("mayor" o "menor") y cuenta con validación robusta para asegurar que solo se acepten números dentro del rango permitido, **sin consumir intentos** en caso de errores de entrada.

---

## Funcionalidad desarrollada por Demetrio

- Generación del número secreto entre 1 y 20.
- Entrada del usuario mediante teclado.
- Comparación entre el número ingresado y el número secreto.
- Mensajes indicando si el número secreto es mayor o menor.
- Finalización del juego cuando el usuario acierta.

Esta es la base sobre la cual los demás integrantes extenderán el proyecto (niveles de dificultad, repetir juego, etc.).

---

## Funcionalidad desarrollada por Yohel

* Límite de Intentos: Se limitó el juego a un máximo de 5 intentos por partida.
* Gestión de Fin de Juego: Se implementó la estructura `for` para gestionar la condición de victoria (`break`) y la condición de derrota (fin del bucle).
* Validación de Entrada: Se mejoró el manejo de errores (`try/except`) para:
    * Asegurar que la entrada sea un número entero válido.
    * Validar que el número se encuentre estrictamente entre 1 y 20. Es decir que solo aplica para la dificultad basica. Los demas companeros deben agregar las otras dificultades con las respectivas validaciones
    * Garantizar que las entradas inválidas (letras o números fuera de rango) no gasten uno de los 5 intentos.

---

---

## Funcionalidad desarrollada por John Roa

Se implementó el sistema de **niveles de dificultad**, permitiendo que el jugador configure el rango del número secreto antes de iniciar la partida. Se añadieron tres niveles:

* **Fácil:** números del 1 al 10
* **Medio:** números del 1 al 20
* **Difícil:** números del 1 al 50

Para esto se creó la función `seleccionar_dificultad()`, la cual muestra el menú, valida la opción elegida y retorna el rango correspondiente. Este rango se utiliza para generar el número secreto dinámicamente mediante:

```python
numero_secreto = random.randint(MINIMO, MAXIMO)
```

Con esta mejora, el juego se vuelve más flexible y ofrece una experiencia ajustada al nivel que el jugador prefiera.

---

## Forma de Uso (Experiencia del Jugador)

Para jugar, sigue estos pasos:

1.  El programa iniciará generando un número secreto al azar entre 1 y 20.
2.  Tendrás un total de **5 intentos** para adivinar el número.
3.  En cada turno, el programa te indicará cuál es tu intento actual.
4.  Ingresa tu número:
    * Si el número es correcto, ¡ganas!
    * Si es incorrecto, el programa te dirá si el número secreto es MAYOR o MENOR que tu suposición.
    * Si ingresas letras o un número fuera del rango 1-20, el programa te pedirá que vuelvas a intentarlo sin perder un intento.
5.  Si agotas tus 5 intentos, el programa mostrara el número secreto.

Esta es la base sobre la cual los demás integrantes extenderán el proyecto ( niveles de dificultad, repetir juego, etc.).
