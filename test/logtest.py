import logging
import os
# log.Log_Info('nihaohaohao')  
# 设置log的存储文件  
import sys
import time

import daemonocle

# logging.basicConfig(filename=os.path.join(os.getcwd(), 'report_log.txt'), level=logging.DEBUG)
# logging.info('可以了吗嗷嗷嗷！')
logging.basicConfig(
        filename=os.getcwd() + '/log/daemonocle_example.log',
        level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
    )


def main():

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
