# Caza Bichos (Proyecto de Juego mBlock/Python)

![Gameplay GIF Placeholder](https://via.placeholder.com/800x400.png?text=Añade+un+GIF+de+tu+juego+aquí)

**Caza Bichos** es un desafiante juego de disparos arcade de supervivencia con una **ambientación desértica**, desarrollado con **Python en el entorno de mBlock**. Como un centinela solitario bajo el sol abrasador, tu misión es defender el cielo del desierto de una variedad de criaturas voladoras. Deberás sobrevivir durante un tiempo limitado, gestionando tus vidas y munición mientras tomas decisiones estratégicas en una fracción de segundo.

Este proyecto, nacido como un trabajo para el profesorado de educación tecnológica, evolucionó hasta convertirse en una exploración profunda de las mecánicas de juego, el diseño de software y las buenas prácticas de programación.

## 📜 Tabla de Contenidos
- [🚀 Sobre el Proyecto](#-sobre-el-proyecto)
- [✨ Características Principales](#-características-principales)
- [🎮 Cómo Jugar](#-cómo-jugar)
- [🕹️ Los Bichos y Sus Roles Estratégicos](#️-los-bichos-y-sus-roles-estratégicos)
- [🔧 Instalación](#-instalación)
- [📝 Notas del Autor](#-notas-del-autor)
- [📄 Licencia](#-licencia)

---

## 🚀 Sobre el Proyecto

**Caza Bichos** va más allá de un simple juego de "apuntar y disparar". Su diseño se centra en la toma de decisiones rápidas bajo presión, obligando al jugador a identificar amenazas, priorizar objetivos y gestionar recursos en el hostil entorno del desierto. El juego está construido sobre una arquitectura basada en eventos y utiliza la clonación de sprites para generar un entorno dinámico y desafiante.

**Tecnologías:**
- **Lenguaje:** Python
- **Entorno:** mBlock 5
- **Principios:** Diseño de software modular, gestión de estados y desarrollo iterativo.

---

## ✨ Características Principales

- **Ambientación Desértica:** Sumérgete en un escenario árido donde cada criatura se recorta contra el cielo azul.
- **Múltiples Tipos de "Bichos":** Enfréntate a tres criaturas aéreas, cada una con un comportamiento, rol y nivel de amenaza únicos.
- **Jerarquía de Amenazas:** No todos los objetivos son iguales. Aprende a priorizar al **Búho del desierto** para proteger tus vidas.
- **Mecánica de Criatura Sagrada:** ¡No dispares a todo lo que se mueve! El **Tucán exótico** es un aliado. Dispararle te penalizará duramente, pero protegerlo te recompensará.
- **Sistema de Vidas y Recompensas:** Comienzas con 3 vidas, pero puedes ganar más gracias a la rara y brillante **Libélula Dorada**.
- **Múltiples Condiciones de Fin de Partida:** La partida puede terminar por el calor del mediodía (falta de tiempo), por quedarte sin vidas, o al alcanzar la gloriosa victoria por puntos.
- **Puntuación Final Basada en Eficiencia:** Tu score final no solo depende de los puntos brutos, sino de tu dificultad, las vidas restantes y el tiempo utilizado.

---

## 🎮 Cómo Jugar

1.  **El Objetivo:** Sobrevive bajo el sol del desierto y consigue la mayor puntuación posible. La partida termina si te quedas sin tiempo, sin vidas, o si alcanzas los 500 puntos.
2.  **Los Controles:** Mueve el mouse para apuntar y haz clic para disparar.
3.  **Identifica a los Bichos:**
    - 🎯 **Libélula (Enjambre del Oasis):** Tu principal fuente de puntos. ¡Cuidado con su variante dorada, que te dará una vida extra!
    - 🦉 **Búho (Depredador Nocturno Extraviado):** Es rápido y su movimiento es impredecible. Si dejas que se escape, **perderás una vida**. ¡Derríbalo a toda costa!
    - 🦜 **Tucán (Espíritu del Oasis):** **¡NO LE DISPARES!** Es un aliado sagrado. Si le aciertas por error, perderás puntos y una vida. Si lo dejas cruzar el cielo sano y salvo, te recompensará.

---

## 🕹️ Los Bichos y Sus Roles Estratégicos

- **Fondo (El Desierto):** Es el cerebro del juego. Controla los estados (Inicio, Juego, Fin), gestiona las variables globales como el tiempo, las vidas y los puntos, y determina las condiciones de victoria o derrota.
- **Arma y Bala (El Cazador):** Tu conexión con el juego. El arma sigue al mouse y la bala es la encargada de interactuar con el mundo.
- **Libélula (La Plaga):** El enemigo más común. Fácil de abatir, pero su recompensa es menor. Su variante dorada puede cambiar el curso de la partida.
- **Búho (La Amenaza):** El enemigo más peligroso. Su movimiento con gravedad lo hace difícil de predecir y su capacidad de quitar vidas lo convierte en el objetivo de mayor prioridad.
- **Tucán (El Dilema):** No es un enemigo, es una prueba. Obliga al jugador a dejar de disparar por reflejo y a tomar decisiones conscientes.
- **Corazones y Calaveras (La Interfaz Viva):** No son solo un contador. Son un sistema visual dinámico que muestra tus aciertos (ganando corazones) y tus errores (con calaveras que son cicatrices permanentes de tus fallos).

---

## 🔧 Instalación

1.  Asegúrate de tener instalado [mBlock 5](https://www.mblock.cc/) y configurado el entorno de Python.
2.  Clona este repositorio en tu máquina local:
    ```bash
    git clone [URL de tu repositorio de GitHub aquí]
    ```
3.  Abre el archivo del proyecto (`.mblock`) con mBlock.
4.  ¡Ejecuta el juego y a disfrutar!

---

## 📝 Notas del Autor

Este proyecto comenzó como un requisito académico, pero rápidamente se convirtió en un campo de pruebas personal para aprender y aplicar conceptos de desarrollo de software que van más allá del currículum. La documentación, la planificación con `Roadmap.md`, el uso de `Git` para control de versiones y la refactorización constante han sido tan importantes como el propio código.

Mi objetivo ha sido no solo "hacer que funcione", sino entender el "porqué" de cada decisión de diseño, creando un producto del que me siento orgulloso y que, espero, pueda servir de inspiración o aprendizaje para otros.

---

## 📄 Licencia

Este proyecto se distribuye bajo una licencia de **uso educativo y personal**. Eres libre de usarlo, modificarlo y aprender de él. No se permite su uso comercial sin la autorización explícita del autor.