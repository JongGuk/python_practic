# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))

# import os
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())
print('\033c')

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print("Today is", datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)
print("From now, after 100 days is", today+td)
