# Aplicación de Visualización Dinámica

Esta aplicación permite mostrar contenido dinámico en una pantalla, controlado remotamente a través de una interfaz web simple. Es ideal para presentaciones interactivas, exhibiciones o cualquier situación donde se necesite cambiar el contenido mostrado en tiempo real.

## Demostración

Puedes ver un video de demostración de la aplicación en funcionamiento aquí:

https://github.com/user-attachments/assets/80ac6a0c-61ac-4977-9989-fe2c6cbe0dc9

## Características

- En la pantalla principal, muestra pasos numerados con contenido específico.
- Cambia el fondo de la pantalla con cada actualización, y el archivo es gestionado aleatorimente desde el servidor, usando unsplash.com (requiere API)
- Transiciones suaves entre cambios de contenido y fondo mdainte CSS.
- Pantalla principal es controlada remotamente a través de una interfaz web sencilla, desde un Arduino o un cliente equivalente haciendo un llamado simple HTTP GET a una URL

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
   pip install flask flask-socketio requests io
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
