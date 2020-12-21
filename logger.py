"""
Customized logger implementation
"""
import os,sys,logging

log = logging.getLogger('')
log.setLevel(logging.DEBUG)
format = logging.Formatter("%(asctime)s - %(levelname)s (%(module)s - %(funcName)s): %(message)s",
                           datefmt="%Y-%m-%d %H:%M:%S"
                           )


def log_capture(file_name):
    logs_dir = "TTL_MAP\\reports\\logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    if os.path.exists(os.path.join(logs_dir, file_name + ".log")):
        os.remove(os.path.join(logs_dir, file_name + ".log"))
    fh = logging.FileHandler(os.path.join(logs_dir, file_name + ".log"), mode='w')
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(format)
    fh.setFormatter(format)
    log.addHandler(ch)
    log.addHandler(fh)
    log.info('Tests execution started')


def end_capture():
    log.info('Test execution ended')
    handlers = log.handlers[:]
    for handler in handlers:
        handler.close()
        log.removeHandler(handler)
