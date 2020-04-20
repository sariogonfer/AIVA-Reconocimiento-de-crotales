# Reconocimiento de crotales

El objetivo de este proyecto consiste en la identificación de cabezas de ganado a través de la identificación que aparece en su crotal. Para ello, esta identificación será extraida de imágenes del crotal a las cuales se les aplicará técnicas de visión artificial.

Este proyecto forma es compone una de las prácticas para la asignatura __Aplicaciones Industriales y Comerciales__ del [Master Universitario en Visión Artificial](https://mastervisionartificial.es) de la **Universidad Rey Juan Carlos de Madrid**.

## Ejecutar el proyecto

Para descargar el proyecto, descarga el código fuente desde este repositorio o clonalo:

```
git clone git@github.com:RoberG/AIVA-Reconocimiento-de-crotales.git .
```

### Prerequisitos

El sistema funciona bajo la versión 3 de Python. 

Los paquetes necesarios se podrán instalar directamente del fichero **_requirements.txt_**.

```
pip install -r  requirements.txt
```

Para instalar la herramienta como si un paquete de Python se tratase (y poder ejecutar los tests):
```
pip install .
``` 
#### Tesseract (old)

**Solo necesario si se utiliza este reader**. También será necesario instalar el motor de reconocimiento óptico Tesseract. Para ello se deben seguir los siguientes paso:

1. Ubuntu

Abrid la terminal y ejecutar la siguiente comando:

```
sudo apt update sudo apt install tesseract-ocr
```

2. Windows

Descargar el binario de la aplicación desde la página del proyecto: [link](https://tesseract-ocr.github.io/tessdoc/Downloads)

#### Docker

En caso de querer ejecutar el contenedor la imagen **Docker** preparado para correr la aplicación web, es necesario tener instalado la aplicación **Docker** en el nuestro sistema. Se puede encontrar las instruciones para instalar esta herramienta en [link](https://docs.docker.com/get-docker/)

## Ejecución


### Línea de comandos

Para ejecutar la aplicación a través de la terminal del sistema, podemos ejecutar la aplicación de la siguiente manera:

``` 
cd reconocimiento_crotales
python App.py process_image PATH_IMAGE
``` 

### Aplicación Web. Docker. (recomendada)

Se ha creado una imagen de **Docker** con el fin de facilitar la puesta en marcha del sevidor web creado en este proyecto. Para ello, solo necesitaremos tener instalada la herramienta **Docker** sin necesidad de tener instalado el resto de requisitos. 

Para poder crear y ejecutar un contenedor con esta imagen, debemos ejecutar el siguiente comando:

``` 
docker run -it -p 8000:8000 sario/aiva-reconocimiento-crotales
``` 

Esto pondrá en marcha un servidor que podrá ser accesible a través del puerto 8000 de nuestro sistema (http://localhost:8000). La imagen es descargada automáticamente desde el repositorio oficial [AIVA-Reconocimiento de crotales](https://hub.docker.com/r/sario/aiva-reconocimiento-crotales).

### Aplicación Web. Directamente en el sistema.

Si se quiere ejecutar la aplicación web directamente sobre el sistema operativo en el que estamos trabajando, en primer lugar será necesario tener instalado todos los requisitos de la aplicación y la propia aplicación. Con todo ello instalado, podremos lanzar una servidor ejecutando la aplicación en local con el siguiente comando:

``` 
python -m reconocimiento_crotales.server
```

## Tests

El sistema dispone de una serie de tests unitarios preparados para comprobar el correcto funcionamiento del mismo. Para ejecutarlos:

```
cd tests
python -m unittest 
```

## Autores

* **Roberto Gallardo Cava** - [RoberG](https://github.com/RoberG)
* **César González Fernández** - [sariogonfer](https://github.com/sariogonfer)
