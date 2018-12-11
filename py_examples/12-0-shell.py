import os
from os import path
import shutil #shell utilities
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("10-1-testfile.txt"):
        src = path.realpath("10-1-testfile.txt")
        # (head,tail) = path.split(src)
        # print("path: %s" % str(head))
        # print("file: %s" %  str(tail))

        #make a backup of file
        dst = src + ".bak"
        shutil.copy(src,dst)
        shutil.copystat(src,dst) #copy statistics - creation date, access time, etc
        os.rename("10-1-testfile.txt", "12-1-testfile2.txt")

        root_dir,tail = path.split(src)
        shutil.make_archive("12-3-archive","zip",root_dir)

        with ZipFile("10-1-testfile.txt", "w") as newzip:
            newzip.write("12-4-nextfile.txt")
            newzip.write("10-1-testfile.txt.bak")

main()