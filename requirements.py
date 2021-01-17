import sys
import subprocess
import pkg_resources

required = {'numpy','pandas','tkinter','openpyxl','seaborn','matplotlib'} 
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',*missing])