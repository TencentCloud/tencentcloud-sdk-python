# -*- coding: UTF-8 -*-
import os
import shutil
import sys
import argparse


README = '''============================
Tencent Cloud SDK for Python
============================

Tencent Cloud Python %s SDK is the official software development kit, which allows Python developers to write software that makes use of Tencent Cloud services like CVM and CBS.
The SDK works on Python versions:

   * 2.7 and greater, including 3.x

Quick Start
-----------

First, install the library:

.. code-block:: sh

    $ pip install tencentcloud-sdk-python-common
    $ pip install tencentcloud-sdk-python-%s

or download source code from github and install:

.. code-block:: sh

    $ git clone https://github.com/tencentcloud/tencentcloud-sdk-python.git
    $ cd tencentcloud-sdk-python
    $ python package.py --components common %s

'''

SETUP = '''#!/usr/bin/env python
import os
from setuptools import setup, find_packages

import tencentcloud

ROOT = os.path.dirname(__file__)

setup(
    name='tencentcloud-sdk-python-%s',
    version=tencentcloud.__version__,
    description='Tencent Cloud %s SDK for Python',
    long_description=open('README.rst').read(),
    author='Tencent Cloud',
    url='https://github.com/TencentCloud/tencentcloud-sdk-python',
    maintainer_email="tencentcloudapi@tencent.com",
    scripts=[],
    packages=find_packages(exclude=["tests*"]),
    license="Apache License 2.0",
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
'''

SETUPCFG = '''[bdist_wheel]
universal=1
'''


def exec_cmd(cmd):
    try:
        if sys.version_info.major < 3:
            import commands
            (ret, output) = commands.getstatusoutput(cmd)
        else:
            import subprocess
            (ret, output) = subprocess.getstatusoutput(cmd)
        return ret, output

    except Exception as err:
        print("err_mark:%s" % str(err))
    return None


def build_and_install_package(mod, upload):
    cmd = 'cd temp-directory && python setup.py sdist bdist_wheel'
    ret, output = exec_cmd(cmd)
    if ret != 0:
        print("%s build failed because %s" % (mod, output))
        return

    if upload is True:
        cmd = 'cd temp-directory && twine upload dist/*'
        ret, output = exec_cmd(cmd)
        print(output)
        if ret != 0:
            print("%s upload failed because %s" % (mod, output))
        cmd = 'cd temp-directory && rm dist/*'
        exec_cmd(cmd)
        return

    cmd = "cd temp-directory && cd dist && pip install tencentcloud-sdk-python-%s-*.tar.gz" % mod
    ret, output = exec_cmd(cmd)
    if ret != 0:
        print("%s install failed because %s" % (mod, output))
        return


def mk_config_file(temp_dir, mod):
    with open(os.path.join(temp_dir, 'setup.py'), 'w') as f:
        f.write(SETUP % (mod, mod.capitalize()))
    with open(os.path.join(temp_dir, 'README.rst'), 'w') as f:
        f.write(README % (mod.capitalize(), mod, mod))
    with open(os.path.join(temp_dir, 'setup.cfg'), 'w') as f:
        f.write(SETUPCFG)


def mk_dir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)
    return dir


def copy_file(src, dst):
    shutil.copy(src, dst)


def generate_lib_src(src, dst):
    for item in os.listdir(src):
        src_name = os.path.join(src, item)
        dst_name = os.path.join(dst, item)
        if os.path.isfile(src_name):
            shutil.copy(src_name, dst_name)
        else:
            if not os.path.isdir(dst_name):
                os.makedirs(dst_name)
            generate_lib_src(src_name, dst_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='python sdk package tool.')
    parser.add_argument('--services', nargs='+', help='service name, such as --services cvm --services common')
    parser.add_argument('--upload', action='store_true', default=False, help='upload to pypi or not.')
    args = parser.parse_args()
    root_path = os.path.dirname(os.path.abspath(__file__))
    # 创建打包的临时目录
    temp_dir = os.path.join(root_path, "temp-directory")
    tx_path = os.path.join(root_path, "tencentcloud")
    try:
        for item in sorted(os.listdir(tx_path)):
            if not os.path.isdir(os.path.join(tx_path, item)):
                continue
            # __pycaches__
            if "__" in item:
                continue
            if args.services and item not in args.services:
                continue
            print("processing %s" % item)
            mk_dir(temp_dir)
            mk_config_file(temp_dir, item)
            tx_dir_in_temp = mk_dir(os.path.join(temp_dir, "tencentcloud"))
            copy_file(os.path.join(tx_path, "__init__.py"),
                      os.path.join(tx_dir_in_temp, "__init__.py"))
            mod_dir_in_temp = mk_dir(os.path.join(tx_dir_in_temp, item))
            generate_lib_src(os.path.join(tx_path, item), mod_dir_in_temp)
            build_and_install_package(item, args.upload)
            shutil.rmtree(temp_dir)
    except Exception as e:
        print("something wrong: %s" % str(e))
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
    print("finish")
