'''
Quiz7) You have to make weekly report one a week.
Reports are always configured in the following form.

- X th weekly report -
Department:
Name:
Summary:

Make a program that produces weekly report from 1st week to 50th week.

Condition: Make the file name '1st_week.txt', '2nd_week.txt', ...
'''

for i in range(1,51):
    with open(str(i) + "th_week.txt", "w", encoding="utf8") as report_file:
        report_file.write("- " + str(i) + " th weekly report -\nDepartment:\nName:\nSummary:")


