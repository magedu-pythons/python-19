import shutil
import os

# 使用Python copy一个文件，从a目录,copy文件到b目录


def cpfile(src, dst):
    abs_src = os.path.exists(os.path.abspath(src))
    dst_src = os.path.exists(os.path.abspath(dst))
    if not abs_src:
        raise Exception('{} not extist'.format(src))
    if not dst_src:
        raise Exception('{} not extist'.format(dst))
    shutil.copy2(abs_src, dst_src)