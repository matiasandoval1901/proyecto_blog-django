# MiXDRiNKs | Blog de Tragos

*MiXDRiNKs*  es un blog dedicado a la recopilación de recetas de tragos clásicos y complejos. Nuestro objetivo es compartir nuestra pasión por la mixología y brindar inspiración para aquellos que buscan explorar y aprender sobre nuevos sabores y técnicas.
<br>

### Caracteristicas
---

- **Recetas variadas:** Cocteles clasicos, innovadores, con y sin alcohol, para todas las ocasiones.
- **Busqueda y filtrado:**  Fácil busqueda de recetas por categorias, nombre y autor.
-  **Imagenes y descripciones detalladas:** Fotos de alta calidad y descripciones paso a paso para cada receta.
- **Categorización:** Tragos organizados por categorias (Tragos Directos, Tragos Refrescados, Tragos Batidos, Tragos Aperitivos, Macerados, Tragos Licuados).
-  **Comentarios:** Los usuarios registrados pueden comentar libremente.
-  **Orientación:** Tecnicas de preparación, utensilios necesarios, Garnish.
<br>

### Tecnologias utilizadas:
---

- **Lenguaje de programación:** Python 3. x
- **Framework:** Django 5. x
- **Base de datos:** SQLite3
- **Diseño y CSS:** Tailwind CSS
- **Librerias y dependencias:** 
- **Pillow 10.4.0** (procesamiento de imagenes)
- **Python-dotenv 1.0.1** (gestión de variables de entorno)
- **Tzdata 2024.2** (gestión de zonas horarios)
- **Sqlparse 0.5.1** (análisis de consultas SQL)
- **Asgiref 3.8.1** (compatibilidad con ASGI)
<br>

### Instalación y configuración
---

##### Requisitos Previos
- **Python 3. x**
- **SQLITE3** (Inlcuido en Django)
- **Entorno de desarrollo** (RECOMENDADO: Visual Studio Code)

##### Instalacion

- Clona el repisotorio: **git clone < url-del-repositorio>**
- Instala las dependencias: **pip install -r requirements.txt**
- Crea un archivo **.env** con las variables de entorno necesarias.
- Ejecuta las migraciones de Django: **python manage.py migrate**
- Crea un superusuario: **python manage.py createsuperuser**

### Configuracion
---

- Configura el archivo **settings.py** segun tus necesidades basicas (base de datos, correo electronico, etc)
- Ajusta las variables de entorno en el archivo **.env**
- Ejecuta el servidor de desarrollo: **python manage.py runserver**

### Ejecución
---

- Accede a **http://localhost:8000/** para ver el blog en acción.

## ESTRUCTURA DEL PROYECTO

```
├── PROYECTO_BLOG-DJANGO/		<--- Carpeta del Repositorio
│ ├── blog/					    <--- Carpeta del proyecto Django
│ │ ├── apps/					<--- Aplicaciones Django
│ │ │ ├── contacto/            <--- Archivos y componentes del formulario de contacto
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── forms.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py	
│ │ │ ├── post/                <--- Archivos y configuraciones de publicaciones
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/		    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ ├── user/                <--- Archivos y configuraciones de gestión de usuarios
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/		    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── signals.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ └── ...
│ │ ├── blog/
│ │ │ ├── __pycache__/		    **Ignorada en el .gitignore**
│ │ │ ├── configurations/	    <--- Configuraciones django
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── local.py		    <--- Configuraciones para desarrollo local
│ │ │ │ ├── production.py	    <--- Configuraciones para produccion
│ │ │ │ ├── base.py		        <--- Configuraciones base
│ │ │ │ └── ...
│ │ │ ├── __init__.py
│ │ │ ├── asgi.py
│ │ │ ├── settings.py
│ │ │ ├── urls.py
│ │ │ ├── views.py
│ │ │ ├── wsgi.py
│ │ │ └── ...
│ │ ├── media/				    <--- Archivos multimedia - **ignorada en el .gitignore**
│ │ │ ├── post/
│ │ │ │ ├── post_default.jpeg
│ │ │ │ └── ...
│ │ │ ├── user/
│ │ │ │ ├── user_default.png
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── static/				         <--- Archivos estáticos utilizados
│ │ │ ├── assets/
│ │ │ │ ├── favicon.ico
│ │ │ │ └── ...
│ │ │ ├── css/
│ │ │ │ ├── style.css
│ │ │ │ └── ...
│ │ │ ├── js/
│ │ │ │ └── tailwind.config.js
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── templates/			    <--- Archivos templates (vistas del sitio)
│ │ │ ├── auth/               <--- Componentes relacionados con la autenticacion de usuario
│ │ │ │ ├── auth_login.html
│ │ │ │ ├── auth_register.html
│ │ │ │ └── ...
│ │ │ ├── Components/                   <---Componentes reutilizables del sitio
│ │ │ │ ├── commons/
│ │ │ │ |  ├── footer.html
│ │ │ │ |  ├── header.html
│ │ │ │ └── ...
│ │ │ │ ├── ui/                         <---Componente de navegacion principal del sitio
│ │ │ │ |  ├── navbar.html
│ │ │ │ └── ...
│ │ │ ├── contacto/                     <--- Estructura de formulario para enviar opiniones
│ │ │ │ ├── contacto.html
│ │ │ │ └── ...
│ │ │ ├── errors/                       <--- Contiene las vistas de Error
│ │ │ │ ├── error_forbidden.html
│ │ │ │ ├── error_not_found.html
│ │ │ │ ├── error_internal.html
│ │ │ │ └── ...
│ │ │ ├── layout/                      <--- Contiene las estructuras base para las vistas
│ │ │ │ ├── auth_layout.html
│ │ │ │ ├── base_layout.html
│ │ │ │ ├── general_layout.html
│ │ │ │ ├── post_layout.html
│ │ │ │ └── ...
│ │ │ ├── post/                        <--- Vistas relacionadas con las publicaciones
│ │ │ │ ├── post_delete.html
│ │ │ │ ├── post_detail.html
│ │ │ │ ├── post_list.html
│ │ │ │ ├── post_new.html
│ │ │ │ ├── post_update.html
│ │ │ │ └── ...
│ │ │ ├── user/                       <--- Archivos y configuraciones del perfil de usuario
│ │ │ │ ├── user_profile.html
│ │ │ │ └── ...
│ │ │ ├── about.html               <--- Informacion sobre el equipo
│ │ │ ├── index.html               <--- Vista de inicio/Contenido general
│ │ │ └── ...
│ │ ├── db.sqlite3			    <--- Base de datos - **Ignorada en el .gitignore**
│ │ ├── manage.py               <--- Gestion y administración del proyecto
│ │ └── ...
| ├── entorno/						<---Ejecucion del proyecto - **gitignore
| │ ├── Scripts/
| │ │ ├── activate.bat
| │ │ ├── deactivate.bat
| │ │ └── ...
| │ └── ...
│ ├── .gitignore
│ ├── README.md				    <--- Archivo README.md - Describe el proyecto
│ ├── requeriments.txt		    <--- Archivo requeriments.txt - Enlista los paquetes
| └── ...
└── ...
```