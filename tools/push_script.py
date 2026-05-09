import subprocess
from pathlib import Path
repo = Path(r'C:\Users\zdxzh\Desktop\aws-saa-c03-study-notes')
log = repo / 'gitpush-output.txt'
cmd = ['git', '-C', str(repo), 'push', '-u', 'origin', 'main']
proc = subprocess.run(cmd, capture_output=True, text=True)
log.write_text(proc.stdout + proc.stderr, encoding='utf-8')
print('EXIT', proc.returncode)
