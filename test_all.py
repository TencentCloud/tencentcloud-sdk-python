import os
import shutil
from subprocess import check_call

access_key_id = os.environ.get("TENCENTCLOUD_SECRET_ID")
access_key_secret = os.environ.get("TENCENTCLOUD_SECRET_KEY")


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


if access_key_id and access_key_secret:
    cur_path = os.path.abspath('.')
    temtest_dir = os.path.join(cur_path, "temtest")
    if os.path.exists(temtest_dir):
        shutil.rmtree(temtest_dir)
    os.mkdir(temtest_dir)
    try:
        for item in os.listdir(cur_path):
            if item.startswith("tencentcloud-sdk-python-"):
                generate_lib_src(os.path.join(cur_path, item), temtest_dir)

        os.environ.__setitem__('PYTHONPATH', temtest_dir)
        check_call('pytest tests/', shell=True)
    except Exception as e:
        print("something wrong: %s" % str(e))
    finally:
        if os.path.exists(temtest_dir):
            shutil.rmtree(temtest_dir)