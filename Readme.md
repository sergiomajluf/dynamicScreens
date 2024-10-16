# Aplicación de Visualización Dinámica

Esta aplicación permite mostrar contenido dinámico en una pantalla, controlado remotamente a través de una interfaz web simple. Es ideal para presentaciones interactivas, exhibiciones o cualquier situación donde se necesite cambiar el contenido mostrado en tiempo real.

## Demostración

Puedes ver un video de demostración de la aplicación en funcionamiento aquí:
[![Ver Demo]](demo-control-externo.mp4)

## Características

- Muestra pasos numerados con contenido específico.
- Cambia el fondo de la pantalla con cada actualización.
- Control remoto a través de una interfaz web sencilla.
- Transiciones suaves entre cambios de contenido y fondo.

## Instalación

Para instalar y ejecutar esta aplicación, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema (versión 3.6 o superior).

2. Clona este repositorio o descarga los archivos en tu computadora.

3. Abre una terminal y navega hasta el directorio del proyecto.

4. Crea un entorno virtual (recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

5. Instala las dependencias necesarias:
   ```
   pip install flask flask-socketio requests
   ```

6. Configura tu clave de API de Unsplash (para las imágenes de fondo):
   - Crea una cuenta en Unsplash y obtén una clave de API.
   - Crea un archivo `.env` en el directorio del proyecto y añade:
     ```
     UNSPLASH_ACCESS_KEY=tu_clave_de_api_aqui
     ```

7. Ejecuta la aplicación:
   ```
   python app.py
   ```

8. Abre un navegador y ve a `http://localhost:5000` para ver la pantalla principal.

9. Para acceder al panel de control, ve a `http://localhost:5000/control` en otra pestaña o dispositivo.

¡Disfruta usando tu nueva aplicación de visualización dinámica!
