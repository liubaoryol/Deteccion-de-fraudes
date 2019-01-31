# Deteccion-de-fraudes
Algoritmo de inteligencia artificial para detectar fraud bancario.
Consiste de tres partes, dos redes neuronales no supervisadas; Autoencoder, Self-Organizing Maps, y una red neuronal supervisada,
esta última es para aprender de fraudes sucedidos, para que no se vuelvan a repetir.

Con base en datos generamos algoritmos básicos para simular fraude, desde inconsistencias de
distancia entre compra hasta transacciones atípicas de cada cliente. El algoritmo autoencoder
encuentra características fundamentales de cierta clase (en este caso todas aquellas transacciones
no fraudulentas). Gracias a la percepción generada por el algoritmo de las características
fundamentales de las transacciones normales, las transacciones fraudulentas son captadas como
compras atípicas que no cumplen algunas de esas características, resultando en no ser reconocidas
por el autoencoder quedando clasificadas como fraude.
Adicionalmente, nuestro algoritmo logra clasificar a los clientes en grupos basándose en su
comportamiento, haciendo lo que se llama client – specific y logrando así un incremento en la
precisión de la detección de fraudes.

Nota: el algoritmo no funciona bien en la base sintética creada por nosotros, por ser una base con mucha aleatoriedad.

Idea adicional, utilizar series de tiempo para detectar tendencia y estacionalidad en los gastos.
