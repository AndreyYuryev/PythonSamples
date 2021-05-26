import shutil
import os
import stat
import time
import datetime
import sys
import argparse
import tempfile


def main(prmtr):
    parser = attr_parser()
    namespace = parser.parse_args(prmtr)
    if namespace.l is not None:
        # Open a file with access mode 'a'
        file_log = open(namespace.l, 'a+')
        print('Copy base KeepassX ', datetime.datetime.now(), file=file_log)
    #  srcfile = '/home/andrey/Documents/mybase.kdbx'
    #  path = '/home/andrey/Downloads'
    if namespace.f is not None and namespace.d is not None:
        modificationTime = get_date(namespace.f, file_log)
        dstpath = os.path.join(namespace.d, modificationTime)
        if create_folder(dstpath, file_log):
            copy_file(namespace.f, dstpath, file_log)
    else:
        print("File or directory is not supplied", file=file_log)
    file_log.close()

def attr_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', '--file', help='File have to copy')
    parser.add_argument('--d', '--directory', help='Directory for copy of current file')
    parser.add_argument('--l', '--log', nargs='?', help='File for log', default=os.path.join(tempfile.gettempdir(),'keepassx.log'))
    return parser

def copy_file(srcfile, dstpath, log):
    # Copy file if exist
    if os.path.exists(srcfile) and os.path.isfile(srcfile):
        dstfile = shutil.copy(srcfile, dstpath)
        print("File ", dstfile, " created ", file=log)
    else:
        print("File ", srcfile, " doesn't exits ", file=log)


def get_date(srcfile, log):
    # Convert seconds since epoch to Date only
    if os.path.exists(srcfile) and os.path.isfile(srcfile):
        prefix = time.strftime('%Y.%m.%d', time.localtime(os.path.getmtime(srcfile)))
    else:
        print("File ", srcfile, " doesn't exits ", file=log)
        prefix = 'Tmp'
    return prefix

def create_folder(dirpath, log):
    # Create target Directory if don't exist
    if not os.path.exists(dirpath):
        try:
            # Create target Directory
            os.mkdir(dirpath)
            print("Directory ", dirpath, " created ", file=log)
            return True
        except FileExistsError:
            print("Directory ", dirpath, " already exists", file=log)
            return False
    else:
        print("Directory ", dirpath, " already exists", file=log)
        return False


if __name__ == '__main__':
    main(sys.argv[1:])
