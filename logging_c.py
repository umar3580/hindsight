import logging
import os
import sys

# logging.basicConfig(format="[%(asctime)s] %(levelname)s: %(filename)s:%(lineno)s | %(message)s", level=os.environ.get("LOGLEVEL", "DEBUG"))

log = logging.getLogger(__name__)
vLog= logging.getLogger("vBos")

stdout = logging.StreamHandler(stream=sys.stdout)
fmtOption = logging.Formatter("%(levelname)s: %(asctime)s  | %(filename)s>%(lineno)s | %(message)s")

stdout.setLevel(logging.DEBUG)
stdout.setFormatter(fmtOption)

def setDebugLevel(dLog='low'):
    if dLog == 'v':
        log.setLevel(logging.DEBUG)
        vLog.setLevel(logging.INFO)
        log.addHandler(stdout)
        vLog.addHandler(stdout)

    elif dLog == 'vv':
        log.setLevel(logging.DEBUG)
        vLog.setLevel(logging.DEBUG)
        log.addHandler(stdout)
        vLog.addHandler(stdout)
    
    elif dLog == 'l':
        log.setLevel(logging.INFO)
        log.addHandler(stdout)
    
    else:
        log.setLevel(logging.INFO)
        vLog.setLevel(logging.INFO)
        log.addHandler(stdout)
        vLog.addHandler(stdout)       
 
