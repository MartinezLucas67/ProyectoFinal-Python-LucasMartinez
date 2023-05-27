# Proyecto Final Coder Comision 40440 - Python
+ Alumno Lucas Martinez Flores
## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abrir cmd y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

#
pip install -r requirements.txt

#
## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
python manage.py createsuperuser

+ Entrar con usuario y contraseña via:

127.0.0.1:8000/admin


# Superusuario de pruebas
+ usuario: lucascoder
+ contra: admin1234

# Descripcion del Proyecto
+ La pagina fue creada para poder subir articulos sobre cualquier cosa en realidad, pero por demostracion elegi tema sobre el cafe. No tiene mucha info sobre el tema.
+ El visitante de la web (el usuario no logueado) va a poder ver todo el listado de los articulos, ver la pagina de inicio con un maximo de 5 articulos, podra acceder a la vista Historia del Cafe y tambien a la vista Acerca de mi. Podra registrarse si desea y hacer login. Aunque vea la vista de todos los articulos y le aparezca la opcion de Añadir un articulo no va a poder crearlo sin antes iniciar sesion.
+ Usuario logueado podra crear articulo, modificarlo, y eliminarlo, tambien podra subir su avatar y eliminarlo, tambien podra editar su perfil. Tiene acceso a todo las vistas que puede acceder el usuario no logueado.
+ Un Admin puede hacer todo desde el panel de Administrador.


# Video Demostración
+ https://youtu.be/RQjLYNSPb3g
# Comentraios
+ El txt requirementents tiene cosas del CKEditor que no lo pude agregar al codigo. No me funciono y no pude resolverlo.
