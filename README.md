# Caza Bichos (Proyecto de Juego mBlock/Python)

![Gameplay GIF Placeholder](https://via.placeholder.com/800x400.png?text=Añade+un+GIF+de+tu+juego+aquí)

**Caza Bichos** es un desafiante juego de disparos arcade de supervivencia con una **ambientación desértica**, desarrollado con **Python en el entorno de mBlock**. Como un centinela solitario bajo el sol abrasador, tu misión es defender el cielo del desierto de una variedad de criaturas voladoras. Deberás sobrevivir durante un tiempo limitado, gestionando tus vidas y munición mientras tomas decisiones estratégicas en una fracción de segundo.

Este proyecto, nacido como un trabajo para el profesorado de educación tecnológica, evolucionó hasta convertirse en una exploración profunda de las mecánicas de juego, el diseño de software y las buenas prácticas de programación.

## 📜 Tabla de Contenidos
- [🚀 Sobre el Proyecto](#-sobre-el-proyecto)
- [✨ Características Principales](#-características-principales)
- [🎮 Cómo Jugar](#-cómo-jugar)
- [🕹️ Sprites y Sus Roles Estratégicos](#️-sprites-y-sus-roles-estratégicos)
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
- **Jerarquía de Amenazas:** No todos los objetivos son iguales. Aprende a priorizar al **Búho** para proteger tus vidas y a no dispararle al **Tucán** para evitar penalizaciones.
- **Balanceo Dinámico:** La velocidad, frecuencia de aparición y recompensa de puntos de todos los enemigos escalan con el nivel de dificultad, ofreciendo una curva de desafío justa y creciente.
- **Sistema de Recarga Táctica:** Gestiona tu cargador de 6 balas con una recarga automática o **manual (tecla 'R')** que crea ventanas de vulnerabilidad y recompensa la planificación.
- **Sistema de Vidas y Recompensas:** Comienzas con 3 vidas, pero puedes ganar más gracias a la rara y brillante **Libélula Dorada**.
- **Múltiples Condiciones de Fin de Partida:** La partida puede terminar por el calor del mediodía (falta de tiempo), por quedarte sin vidas, o al alcanzar la gloriosa victoria.
- **Interfaz de Juego Completa (HUD):** Monitoriza en tiempo real tu tiempo restante, vidas, munición actual y el progreso hacia tu objetivo de victoria.

---

## 🎮 Cómo Jugar

1.  **El Objetivo:** ¡**Derrota a 20 libélulas** para ganar la partida! También puedes perder si se agota el tiempo o te quedas sin vidas.
2.  **Los Controles:**
    - **APUNTAR:** Mueve el Ratón
    - **DISPARAR:** Haz Clic
    - **RECARGA TÁCTICA:** Pulsa la tecla 'R'
3.  **Identifica a los Bichos:**
    - 🎯 **Libélula (Objetivo Principal):** Tu objetivo para ganar. ¡Cuidado con su variante dorada, que te dará una vida extra!
    - 🦉 **Búho (Amenaza Prioritaria):** Si dejas que se escape, **perderás una vida**. ¡Derríbalo a toda costa!
    - 🦜 **Tucán (Aliado Sagrado):** **¡NO LE DISPARES!** Si le aciertas, perderás puntos y una vida. Si lo dejas cruzar la pantalla, te recompensará.

---

## 🕹️ Sprites y Sus Roles Estratégicos

- **Fondo (El Desierto):** Es el cerebro del juego. Controla los estados, gestiona las variables globales y determina las condiciones de victoria o derrota (tiempo, vidas, o las 20 libélulas).
- **Arma:** Tu herramienta principal. Gestiona el disparo, el contador de balas en el cargador y la **mecánica de recarga** (automática y manual).
- **Bala:** El proyectil y el **registrador de estadísticas**. Cada clon de bala es un disparo, pero el sprite original se encarga de calcular y mostrar tu **precisión final**.
- **Búho (La Amenaza):** El enemigo más peligroso. Su movimiento con gravedad y su capacidad de quitar vidas lo convierten en el objetivo de mayor prioridad.
- **Tucán (El Dilema):** No es un enemigo, es una prueba de autocontrol. Obliga al jugador a pensar antes de disparar.
- **Libélula (El Objetivo):** El enemigo más común y la clave para la victoria.
- **Corazones y Calaveras (La Interfaz Viva):** Un sistema visual dinámico que muestra tus vidas actuales y las cicatrices permanentes de tus errores.
- **Contadores de Interfaz (El HUD):** Un conjunto de sprites dedicados a mostrar en tiempo real el **Temporizador**, la **Munición en el Cargador** y tu **Progreso de Bajas de Libélulas**.

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