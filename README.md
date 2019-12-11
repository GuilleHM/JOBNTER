# JOBNTER

JOBNTER es un *script* de Python que automatiza la búsqueda de empleo y el envío de CVs a través de LinkedIn. Funciona para aquellas posiciones abiertas que ofrecen la opción "Solicitud sencilla".

Está basado en [LinkedIn-Easy-Apply-Bot](https://github.com/nicolomantini/LinkedIn-Easy-Apply-Bot), de Nicoló Mantini, y está construido sobre los módulos Selenium y BeautifulSoup.

## Instrucciones
He intentado escribir estas instrucciones para que incluso aquellas personas con conocimientos solo a nivel de usuario sobre ordenadores también puedan aprovechar JOBNTER:

- Descarga jobnter.py y chromedriver.exe desde este repositorio.
- Coloca ambos archivos en el mismo directorio.
- Abre jobnter.py con cualquier editor de texto y completa "nombre de usuario", "contraseña", "posición" y "ubicación" (líneas 27 a 30 en el código) con tus propios datos de entrada (simplemente reemplaza las *XXXXXX*). Guarda el archivo.
- Asegúrate de tener Python 3.X instalado en tu ordenador (puedes obtenerlo en este [enlace](https://www.python.org/downloads/)).
- Abre un terminal (suponiendo que eres un usuario de Windows, esta es la "ventana de ejecucion de comandos del sistema de Windows" - si no sabes lo que es esto, puedes encontrarlo fácilmente haciendo una búsqueda en Google).
- Ejecuta este comando (simplemente esrcríbelo, sin las comillas, y pulsa enter): "pip install -U sys time random os csv datetime pyautogui beautifulsoup4 pandas selenium".
- Una vez se termine la ejecución del comando anterior, ¡Ejecuta jobnter.py y relájate!

Nota: JOBNTER está preconfigurado para aplicar a 100 posiciones abiertas cada vez que lo ejecutas, comenzando por la más reciente. Puedes cambiar esta configuración y ejecutarlo tantas veces como desees...simplemente da a LinkedIn el tiempo suficiente para actualizar su sitio con nuevas oportunidades y ejecuta JOBNTER nuevamente.

**¡Buena suerte en tu búsqueda!**

***

JOBNTER is a Python script for automating job search and CV submission on LinkedIn. It works on those open positions that offer the "Easy Apply" option.

It´s based on [LinkedIn-Easy-Apply-Bot](https://github.com/nicolomantini/LinkedIn-Easy-Apply-Bot), from Nicoló Mantini, and built on top of Selenium and BeautifulSoup modules.

## Instructions
I´ve tried to write these instruction so even those people with just user-level knowledge about computers can also take advantage of JOBNTER:

- Download jobnter.py and chromedriver.exe from this repository.
- Place both files on the same directory.
- Open jobnter.py with any text editor and fill in "username", "password", "position" and "location" (lines 27 to 30 in the code) with your own input data (just replace the XXXXXX). Save the file.
- Be sure you have Python 3.X installed on you computer (you can get it on this [link](https://www.python.org/downloads/)).
- Open a terminal window and run this command (whitout quotes): "pip install -U sys time random os csv datetime pyautogui beautifulsoup4 pandas selenium".
- Run jobnter.py and relax!
- JOBNTER is preset for applying to 100 open position each time you run it, starting at the most recently published one. You can modify and run it as many times as you want...just give linkedIn enought time to update its site with new opportunities and run JOBNTER again.

- **Good luck in your search!**
