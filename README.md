# JOBNTER

JOBNTER es un *script* de Python que automatiza la búsqueda de empleo y el envío de CVs a través de LinkedIn. Funciona para aquellas posiciones abiertas que ofrecen la opción "Solicitud sencilla".

Está basado en [LinkedIn-Easy-Apply-Bot](https://github.com/nicolomantini/LinkedIn-Easy-Apply-Bot), de Nicoló Mantini, y está construido sobre los módulos Selenium y BeautifulSoup.

## Instrucciones
He intentado escribir estas instrucciones para que incluso aquellas personas con conocimientos solo a nivel de usuario sobre ordenadores también puedan aprovechar JOBNTER.

- Descarga jobnter.py desde este repositorio.
- Descarga chromedriver.exe (puedes obtenerlo desde este [enlace](https://chromedriver.chromium.org/downloads)).
- Coloca ambos archivos en el mismo directorio.
- Abre jobnter.py con cualquier editor de texto y completa "nombre de usuario", "contraseña", "posición" y "ubicación" (líneas 27 a 30 en el código) con tus propios datos de entrada (simplemente reemplaza las *XXXXXX*). Guarda el archivo.
- Asegúrate de tener Python 3.X instalado en tu ordenador (puedes obtenerlo en este [enlace](https://www.python.org/downloads/)).
- ¡Ejecuta jobnter.py y relájate! (suponiendo que eres un usuario de Windows, simplemente escribe "python jobnter.py" en una "ventana de ejecucion de comandos del sistema de Windows" - si no sabes lo que es esto, puedes encontrarlo fácilmente haciendo una búsqueda en Google).

Nota: JOBNTER está preconfigurado para aplicar a hasta 100 posiciones abiertas cada vez que lo ejecutas, comenzando por la más reciente. Puedes ejecutarlo tantas veces como desees...simplemente da a LinkedIn el tiempo suficiente para actualizar su sitio con nuevas oportunidades y ejecuta JOBNTER nuevamente.

**¡Buena suerte en tu búsqueda!**

***

JOBNTER is a Python script for automating job search and CV submission on LinkedIn. It works on those open positions that offer the "Easy Apply" option.

It´s based on [LinkedIn-Easy-Apply-Bot](https://github.com/nicolomantini/LinkedIn-Easy-Apply-Bot), from Nicoló Mantini, and built on top of Selenium and BeautifulSoup modules.

## Instructions
I´ve tried to write these instruction so even those people with just user-level knowledge about computers can also take advantage of JOBNTER.

- Download jobnter.py from this repository.
- Download chromedriver.exe (you can get it from this [link](https://chromedriver.chromium.org/downloads)).
- Place both files on the same directory.
- Open jobnter.py with any text editor and fill in "username", "password", "position" and "location" (lines 27 to 30 in the code) with your own input data (just replace the XXXXXX). Save the file.
- Be sure you have Python 3.X installed on you computer (you can get it on this [link](https://www.python.org/downloads/)).
- Run jobnter.py and relax! (assuming you are a Windows user, just write "python jobnter.py" in a Windows Command Prompt).
- JOBNTER is preset for applying up to 100 open position each time you run it, starting at the most recently published one. You can run it as many times as you want...just give linkedIn enought time to update its site with new opportunities and run JOBNTER again.
- **Good luck in your search!**
