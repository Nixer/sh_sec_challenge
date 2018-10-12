from subprocess import Popen

processes = []

for counter in range(1):
    chrome_cmd = 'export BROWSER=chrome && pytest -s -v'
    firefox_cmd = 'export BROWSER=firefox && pytest -s -v'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))

for counter in range(1):
    processes[counter].wait()