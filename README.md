# EternalBlue Automation Script

Este script de Python está diseñado para automatizar el proceso de prueba de la vulnerabilidad MS17-010, conocida como EternalBlue, en sistemas Windows.

## Advertencia

Este script es solo para propósitos educativos y de pruebas de penetración autorizadas. El uso de este script en redes o sistemas sin permiso explícito es ilegal y contrario a las prácticas éticas de ciberseguridad.

## Requisitos Previos

- Python 3.x
- Metasploit Framework
- pymetasploit3 (Python library)
- Acceso a una instancia de msfrpcd corriendo y accesible

## Configuración

1. Asegúrate de tener Metasploit Framework instalado y actualizado en tu sistema.
2. Inicia el servicio `msfrpcd` en Metasploit con el comando:
3. msfrpcd -P [password] -S -a 127.0.0.1
4. Donde `[password]` es una contraseña segura de tu elección.
3. Clona este repositorio o descarga el script en tu sistema Kali Linux.

## Instalación

Antes de ejecutar el script, instala las dependencias necesarias:

```bash
pip install pymetasploit3
Para ejecutar el script, navega a la carpeta que contiene eternalblue_automation.py y ejecuta:
python eternalblue_automation.py

Crear un archivo README.md es esencial para documentar el propósito y las instrucciones de uso de tu script. Aquí te proporciono una plantilla de README.md para el script que hemos discutido:

markdown
Copy code
# EternalBlue Automation Script

Este script de Python está diseñado para automatizar el proceso de prueba de la vulnerabilidad MS17-010, conocida como EternalBlue, en sistemas Windows.

## Advertencia

Este script es solo para propósitos educativos y de pruebas de penetración autorizadas. El uso de este script en redes o sistemas sin permiso explícito es ilegal y contrario a las prácticas éticas de ciberseguridad.

## Requisitos Previos

- Python 3.x
- Metasploit Framework
- pymetasploit3 (Python library)
- Acceso a una instancia de msfrpcd corriendo y accesible

## Configuración

1. Asegúrate de tener Metasploit Framework instalado y actualizado en tu sistema.
2. Inicia el servicio `msfrpcd` en Metasploit con el comando:
msfrpcd -P [password] -S -a 127.0.0.1

markdown
Copy code
Donde `[password]` es una contraseña segura de tu elección.
3. Clona este repositorio o descarga el script en tu sistema Kali Linux.

## Instalación

Antes de ejecutar el script, instala las dependencias necesarias:

```bash
pip install pymetasploit3
Uso
Para ejecutar el script, navega a la carpeta que contiene eternalblue_automation.py y ejecuta:

bash
Copy code
python eternalblue_automation.py
Sigue las instrucciones en la terminal para introducir la IP del objetivo y tu IP local.

Funcionamiento Interno
El script realizará las siguientes acciones:

Verificar e instalar la biblioteca pymetasploit3 si es necesario.
Actualizar la base de datos de Metasploit y el framework.
Pedir al usuario la dirección IP del objetivo y la IP local (LHOST).
Intentar explotar la vulnerabilidad utilizando diferentes módulos relacionados con MS17-010.
Si se requiere autenticación y un exploit falla, pedirá al usuario las credenciales del sistema objetivo.
Intentará otros exploits de la base de datos de Metasploit si los especificados no funcionan.
Contribuciones
Las contribuciones a este script son bienvenidas. Por favor, asegúrate de seguir las buenas prácticas de programación y documentación al hacer cambios o mejoras.

Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulte el archivo LICENSE para obtener más información.
Y aquí tienes un paso a paso para hacer funcionar el script:

1. **Instalación de Metasploit**: Asegúrate de que Metasploit Framework esté instalado en tu sistema Kali Linux. Puedes instalarlo con:

   ```bash
   sudo apt-get install metasploit-framework
Iniciar msfrpcd: Antes de ejecutar el script, necesitas tener el servicio msfrpcd corriendo. Ejecútalo con el siguiente comando:
msfrpcd -P yourpassword -S -a 127.0.0.1
Cambia yourpassword a una contraseña segura de tu elección.

Clonar el Repositorio/Descargar el Script: Obtén el script eternalblue_automation.py y guárdalo en tu sistema Kali Linux.

Instalar pymetasploit3: Si aún no tienes la biblioteca pymetasploit3 instalada, puedes hacerlo con pip:
pip install pymetasploit3
Ejecutar el Script: Abre una terminal, navega hasta el directorio donde se encuentra el script y ejecútalo con:
python eternalblue_automation.py
Sigue las indicaciones en la terminal para ingresar la IP del objetivo y tu IP local.

Seguir las Indicaciones: El script te guiará a través del proceso y realizará las pruebas automáticamente. Proporciona las credenciales cuando se te solicite si es necesario.
