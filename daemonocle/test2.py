import os
import logging
import sys
import time

import daemonocle


def cb_shutdown(message, code):
    logging.info('Daemon is stopping')
    logging.debug(message)


def main():
    logging.basicConfig(
        filename=os.getcwd() + '/log/daemonocle_example.log',
        level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
    )
    logging.info('Daemon is starting')
    while True:
        logging.debug('Still running')
        time.sleep(10)


if __name__ == '__main__':
    print(os.getcwd() + '/log/daemonocle_example.log')
    daemon = daemonocle.Daemon(
        worker=main,
        # shutdown_callback=cb_shutdown,
        pidfile=os.getcwd() + '/daemonocle_example.pid',
    )
    daemon.do_action(sys.argv[1])
