# import pickle

# with open("profile.pickle", "rb") as profile_file: # profile이라는 파일의 내용을 profile_file 이라는 변수로 저장
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
    # study_file.write("I'm studying hard Python.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())