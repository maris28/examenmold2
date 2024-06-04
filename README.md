# examenmold2
Repositorio del examen del módulo 2.
## Tecnologías
EC2, Python, Flask, Git
## Instalación
1. Creamos una EC2 con Amazon Linux, tipo de instancia t2.small. Para poder utilizar Flask, habilitaremos el puerto 5000 de la instancia.
2. Actualizamos paquetería con el comando: sudo yum update -y
3. Intalamos pip con el comando: sudo yum install pip
4. Instalamos un control de versiones, en este caso, git con el comando: sudo yum install git -y
5. Verificamos que se ha instalado git con: git --version
6. Instalamos python con el comando: sudo yum install python3
7. Verificamos que está instaldo python: python3 --version>
8. Instalamos flask con el comando: pip install Flask
## Clonar repositorio
- Para dar permisos a la isntancia usamos este comando para generar la keygen ssh-keygen -t ed25519 -C "correo_repositorio"
- Accedemos a .ssh, cd .ssh
- Obtenemos la clave pública, cat id_ed25519.pub
- En git, el repositorio, seleccionamos settings, deploy keys y ponemos la clave pública.
- En la EC2 clonamos el repositorio con git clone git@github.com:maris28/examenmold2.git

## Estructura de ficheros
- Creamos una carpeta general para el proyecto, src
- Dentro de src crearemos la carpeta "templates" (mkdir templates) donde estarán los archivos html, las plantillas que inyectará el framework.
- A la misma altura que templates tendremos:
    - El archivo app.py, 
    - El archivo clases.py, incluimos los atributos del empleado y métodos del empleado.
 
# Para que arranque la aplicación utilizaremos el comando python3 app.py
