```mermaid
flowchart TD
    A[Inicio del juego] --> B[Arma: posicionarse y apuntar al mouse]
    B --> C[Jugador hace click]
    C --> D[Bala: aparece en posición del arma]
    D --> E[Bala se mueve hacia destino]
    E --> F{Colisión con libélula?}
    F -- Sí --> G[Puntos +10]
    F -- No --> H[Seguir moviéndose]
    G --> I[Subir dificultad si < máximo]
    H --> J[Bajar dificultad si < mínimo o falla]
    I --> K[Libélula: generar nueva desde línea de horizonte]
    J --> K
    K --> L[Libélula se mueve hacia destino aleatorio]
    L --> M{Bala tocó libélula o distancia < 1?}
    M -- Sí --> G
    M -- No --> N[Libélula continúa moviéndose]
    N --> O[Repetir ciclo hasta fin de juego]

    PANTALLA PRINCIPAL
    Logo o titulo de juego
    Se agregará boton de jugar
    Se agregará botón de leer reglas de juego
    Boton de opciones
    Autor
  
    PANTALLA DE SELECCIÓN DE OPCIONES
    Se agregará sección de dificultad, explicación de ellas
    Se pondrá selección de volumen global, sonido previo para comparar escucha, rotador de sonidos aleatorios
    Boton para volver al menú

    PANTALLA DE JUEGO
    Indicador de nivel de dificultad
    Contador de puntos animado
    Timer animado
    Indicador de vidas
    Animación de vidas
    Barra de vidas
    Se pondra un sonido de vuelo a las libelulas
    Se pondra un sonido de disparo
    Se pondra nimacion de golpe y salida de bala
    Se pondra sonido de muerte de libelula
    Sonido de fallo de disparo
    Enemigo al que no dispararle y sus complementos derivados

    PANTALLA DE VICTORIA
    Se agregara un personaje saltando y girando de izq a der conanimación de fuegos artificiales y sonidos
    Se pondrá botón de reiniciar o salir
    Se pondrá boton de siguiente dificultad
    Mensaje de puntaje final
    Estadísticas rápidas (aciertos, fallos, precisión).

    PANTALLA DE DERROTA
    Se agregara un sonido de golpe 
    Se agregará sonido de perdida de fondo
    Se pondra un personaje triste
    Se pondrá Boton de reiniciar o salir
    Se pondrá boton de anterior dificultad
    Mensaje de puntaje final
    Estadísticas rápidas (aciertos, fallos, precisión).