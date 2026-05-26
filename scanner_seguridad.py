import socket
from datetime import datetime

def scan_ports(target, ports):
    print(f"\nIniciando escaneo de seguridad en: {target}")
    print(f"Hora de inicio: {datetime.now()}\n")
    print("-" * 50)
    
    for port in ports:
        # Creamos un socket (AF_INET para IPv4, SOCK_STREAM para TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Establecemos un tiempo de espera corto para el escaneo
        s.settimeout(0.5)
        
        # Intentamos conectar con el puerto
        result = s.connect_ex((target, port))
        
        if result == 0:
            # Si el resultado es 0, el puerto está abierto
            print(f"ALERTA: Puerto {port} está ABIERTO.")
            # Aquí podrías añadir lógica para identificar servicios comunes
            if port == 80: print("  --> Posible servicio HTTP (Web) sin cifrar.")
            if port == 21: print("  --> Posible servicio FTP (Transferencia de archivos).")
            if port == 445: print("  --> Posible servicio SMB (Vulnerable a ataques tipo Ransomware).")
        
        s.close()
    
    print("-" * 50)
    print("Escaneo finalizado.")

if __name__ == "__main__":
    # Se puede probar con '127.0.0.1' (tu propia máquina) o una web de pruebas legal
    objetivo = input("Introduce la IP o dominio a escanear: ")
    # Puertos comunes que suelen ser vectores de ataque - añadir más puertos según cliente
    puertos_a_testear = [21, 22, 23, 80, 443, 445, 3389]
    
    scan_ports(objetivo, puertos_a_testear)
