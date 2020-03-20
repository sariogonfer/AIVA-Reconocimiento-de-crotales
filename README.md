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

También será necesario instalar el motor de reconocimiento óptico Tesseract. Para ello se deben seguir los siguientes paso:

1. Ubuntu

Abrid la terminal y ejecutar la siguiente comando:

```
sudo apt update sudo apt install tesseract-ocr
```

2. Windows

Descargar el binario de la aplicación desde la página del proyecto: [link](https://tesseract-ocr.github.io/tessdoc/Downloads)

## Tests

El sistema dispone de una serie de tests unitarios preparados para comprobar el correcto funcionamiento del mismo. Para ejecutarlos:

```
cd tests
python -m unittest 
```

## Autores

* **Roberto Gallardo Cava** - [RoberG](https://github.com/RoberG)
* **César González Fernández** - [sariogonfer](https://github.com/sariogonfer)
