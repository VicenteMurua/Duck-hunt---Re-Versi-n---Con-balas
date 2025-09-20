# Duck Hunt mBlock Edition 🦆🎯

**Duck Hunt mBlock Edition** es una reimplementación del clásico juego de disparos estilo “Duck Hunt”, desarrollada con **Python y mBlock**. Los jugadores disparan a libélulas (objetos voladores) con un arma controlada con el mouse y deben ir aumentando su puntaje mientras la dificultad se ajusta dinámicamente.

## Tabla de Contenidos
- [Características](#características)
- [Instalación](#instalación)
- [Cómo jugar](#cómo-jugar)
- [Sprites y funcionalidades](#sprites-y-funcionalidades)
- [Variables del juego](#variables-del-juego)
- [Notas técnicas](#notas-técnicas)
- [Licencia](#licencia)

## Características
- Disparo controlado con el mouse.
- Libélulas que aparecen y se mueven de manera aleatoria.
- Sistema de puntaje basado en aciertos.
- Ajuste dinámico de dificultad:
  - Subir dificultad al acertar.
  - Bajar dificultad si se falla.
- Efectos de disparo (bala que se mueve y desaparece tras un tiempo).

## Instalación
1. Instalar [mBlock](https://www.mblock.cc/) y configurar Python si se requiere.
2. Clonar este repositorio:
   git clone https://github.com/tu-usuario/duck-hunt-mblock.git
3. Abrir el proyecto en mBlock.
4. Asegurarse de tener todas las dependencias de Python y mBlock disponibles.

## Cómo jugar
- Mueve el mouse para apuntar el arma.
- Haz click para disparar.
- Cada libélula que aciertes te da **10 puntos**.
- La dificultad aumenta o disminuye según tus aciertos y errores.
- Objetivo: obtener la mayor cantidad de puntos posible antes de que las libélulas lleguen al límite superior del escenario.

## Sprites y funcionalidades

### Arma
- Se posiciona inicialmente en la parte inferior central de la pantalla.
- Apunta siempre hacia el mouse.
- Dispara balas que siguen la posición del mouse.

### Bala
- Aparece en la posición del arma y se desplaza hacia donde apunta.
- Tras un tiempo, desaparece.
- Controla la variable `Bandera de disparo` para detectar colisiones.

### Libélula
- Se generan aleatoriamente desde la línea de horizonte.
- Se mueven hacia un destino aleatorio en el eje X y hacia la parte superior del escenario.
- Detectan colisiones con la bala y actualizan el puntaje.
- Variables importantes:  
  - `Distancia vectorial` para calcular proximidad a la bala.  
  - `Dirección final de libelula` para orientar la libélula.

### Control de dificultad
- **Subir dificultad:** al acertar en la libélula, la dificultad aumenta hasta un máximo.  
- **Bajar dificultad:** al fallar o interactuar con elementos específicos, la dificultad disminuye hasta un mínimo.

### Mira
- Siempre sigue al cursor del mouse.
- Facilita apuntar y disparar.

## Variables del juego
| Variable | Función |
|----------|---------|
| Bandera de disparo | Indica si hay una bala activa |
| Puntos | Puntaje del jugador |
| Dificultad | Controla la velocidad de las libélulas |
| Posición x de disparo / Posición y de disparo | Coordenadas actuales de la bala |
| Distancia de libelula-final eje x / eje y | Vector para calcular colisión |

## Notas técnicas
- Algunos fragmentos del código están marcados como `# not supported yet` debido a limitaciones de mBlock o integración con el binario original.
- Se utiliza `time.sleep()` para temporizar movimientos y efectos.
- Se calculan distancias vectoriales usando la fórmula:
  \[
  \text{Distancia} = \sqrt{(x_{\text{bala}} - x_{\text{libelula}})^2 + (y_{\text{bala}} - y_{\text{libelula}})^2}
  \]
- Clonación de libélulas para generar múltiples objetivos de manera continua.

## Licencia
Este proyecto es de **uso educativo y personal**.  
Puedes adaptarlo para aprender a programar juegos en mBlock, pero no está permitido su uso comercial sin autorización del autor.
