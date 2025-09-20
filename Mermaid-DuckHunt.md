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
