import getopt
import sys


def usage():
    """帮助信息"""
    print('Usage: ')
    print('-h --help : show help messages ')
    print('-a --action : input action ,such as \'collect_data\', \'storage_data\'')
    print('-l --label : input corresponding label')


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ha:l:', ['help', 'action=', 'label='])
        action = None
        label = None
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                usage()
                exit()
            elif opt in ('-a', '--action'):
                action = arg
                break
        # 如果-a 参数为collect_data 执行数据采集程序
        if action == 'collect_data':
            for opt, arg in opts:
                if opt in ('-l', '--label'):
                    label = arg
            # start_collect_data(label=label)
    except Exception as e:
        print('Error', e)


if __name__ == '__main__':
    main()
