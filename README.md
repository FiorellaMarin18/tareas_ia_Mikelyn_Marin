📋 Gestor de Tareas
Este es un proyecto de una aplicación web sencilla para gestionar tareas, construida usando Flask (como servidor backend en Python) y HTML/CSS/JavaScript para el frontend.
La aplicación permite agregar tareas, verlas, marcarlas como hechas y eliminarlas. Los datos se guardan en un archivo JSON, por lo que no necesitas instalar una base de datos.

🔧 Funcionalidades principales
Interfaz moderna y fácil de usar.

Crear, ver, actualizar y eliminar tareas (funcionalidades CRUD).

Cada tarea tiene un título, una descripción, una fecha de vencimiento y un estado ("pendiente" o "hecho").

Las tareas se guardan en un archivo tasks.json, que funciona como una base de datos sencilla.

El frontend se comunica con el backend a través de una API RESTful.

🧱 Estructura del proyecto
El proyecto está organizado en carpetas y archivos de la siguiente manera:

El archivo app.py contiene todo el código del servidor Flask y las rutas de la API.

La carpeta templates/ contiene el archivo HTML que se muestra en el navegador.

La carpeta static/ contiene los estilos CSS y el código JavaScript para la lógica del cliente.

El archivo tasks.json guarda todas las tareas creadas por el usuario.

▶️ Cómo ejecutar la aplicación
Asegúrate de tener Python 3 instalado.

Crea un entorno virtual (opcional, pero recomendado).

Instala Flask con el comando pip install Flask.

Ejecuta el servidor con python app.py.

Abre tu navegador en http://localhost:5000 para usar la aplicación.

🧪 ¿Qué hace cada parte?
HTML (index.html): contiene la estructura de la página, el formulario para agregar tareas y el espacio donde se muestran.

CSS (style.css): define el diseño visual de la página, con un estilo moderno, botones redondeados y colores agradables.

JavaScript (script.js): se encarga de enviar y recibir datos del servidor, actualizar la lista de tareas y gestionar eventos como marcar una tarea como hecha o eliminarla.

Flask (app.py): recibe las solicitudes del navegador, gestiona las tareas, y responde con los datos en formato JSON.

tasks.json: almacena todas las tareas en un formato simple para que sean persistentes.

📝 Licencia
Este proyecto es completamente libre y puedes usarlo, modificarlo y compartirlo como desees. 