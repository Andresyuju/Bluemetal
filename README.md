# EternalBlue Automation Script

Este script de Python está diseñado para automatizar el proceso de prueba de la vulnerabilidad MS17-010, conocida como EternalBlue, en sistemas Windows.

## Advertencia

Este script es solo para propósitos educativos y de pruebas de penetración autorizadas. El uso de este script en redes o sistemas sin permiso explícito es ilegal y contrario a las prácticas éticas de ciberseguridad.

# Script de Explotación con Metasploit

Este script en Python utiliza Metasploit para ejecutar exploits contra sistemas Windows vulnerables, específicamente el exploit EternalBlue. Permite intentar la explotación utilizando exploits tanto para sistemas de 64 bits como para sistemas de 32 bits, y también ofrece la opción de proporcionar credenciales SMB para mejorar las posibilidades de éxito.

## Requisitos

- Python 3.x
- Metasploit Framework instalado y configurado
- Conexión a internet para descargar las últimas actualizaciones de Metasploit

## Instalación de Dependencias

1. **Python 3.x:** Si aún no tienes Python instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2. **Metasploit Framework:** La instalación de Metasploit puede variar según tu sistema operativo. Puedes encontrar instrucciones detalladas para la instalación en la [documentación oficial de Metasploit](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers).

## Uso

1. Clona este repositorio o descarga el script `exploit.py`.
2. Abre una terminal y navega hasta el directorio donde se encuentra el script.
3. Ejecuta el script escribiendo `python3 exploit.py` y presiona Enter.
4. Sigue las instrucciones en pantalla para ingresar la IP del objetivo, tu IP local y, opcionalmente, credenciales SMB si se desea.

## Importante

- Este script es únicamente con fines educativos y de prueba en entornos controlados. No debe utilizarse para actividades ilegales o maliciosas.
- El uso indebido de este script puede ser ilegal y está sujeto a sanciones legales.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error, tienes ideas para mejoras o deseas agregar nuevas características, por favor abre un problema o envía una solicitud de extracción.

## Descargo de responsabilidad

El autor y los contribuyentes de este script no se hacen responsables de ningún daño causado por el mal uso de este script. Utilízalo bajo tu propio riesgo y responsabilidad.
