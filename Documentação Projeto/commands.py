import subprocess

def ping(client):
    result = subprocess.run(f'ping {client}', shell=True, capture_output=True, text=True).stdout
    return result

def showing_ip_configuration():
    result = subprocess.run(f'ipconfig', shell=True, capture_output=True, text=True).stdout
    return result