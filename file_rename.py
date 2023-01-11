import os
import fileinput
import sys
import shutil
## 파일들의 이름을 바꾼후 하나의 폴더로 이동 ##
path = '/home/jml/바탕화면/EMB_v2/kj/' #


for target in os.listdir(path):
    for file in os.listdir(f"{path}{target}/"):
        rename = f"{target}_{file}"
        print(f"{path}{target}/{file}",' -> ',f"{path}{target}/{rename}", '==> ',f"{path}{rename}")
        os.rename(f"{path}/{target}/{file}",f"{path}/{target}/{rename}")
        shutil.move(f"{path}/{target}/{rename}", f"{path}{rename}")
    if os.path.isdir(f"{path}{target}/"):
        os.rmdir(f"{path}{target}/")