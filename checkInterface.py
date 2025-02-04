import os
import subprocess

def get_interfaces():
    result = subprocess.run(['ip', 'link', 'show'], capture_output=True, text=True)
    interfaces = []
    for line in result.stdout.split('\n'):
        if ': ' in line:
            interface = line.split(': ')[1].split('@')[0]
            interfaces.append(interface)
    return interfaces

if __name__ == "__main__":
    interfaces = get_interfaces()
    print("Available network interfaces:")
    for interface in interfaces:
        print(interface)