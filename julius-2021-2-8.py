import subprocess
import os

# Do not apply to patients' data, using module-mode(internet connection)!
# written by Takeshi Ohkubo

os.chdir('C:/Program Files (x86)/dictation-kit-4.5')
cmd1='./bin/windows/julius.exe -C main.jconf -C am-dnn.jconf -demo -charconv utf-8 sjis -dnnconf julius.dnnconf'

p1=subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in iter(p1.stdout.readline,b''):
    txt2=line.rstrip().decode("cp932", errors='ignore')
    print(txt2)