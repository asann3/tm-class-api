import pandas as pd
import datetime as dt

fileName = "授業変更掲示板.csv"
df = pd.read_csv(fileName)
line_count = df.count()[0]  # 行数
df = df.fillna('')

# grade_list = []
# course_list = []
subjects_before_change = []
subjects_after_change = []
date_list = []
weekday_list = []
time_period_list = []
data_length = 0
# print(df)


def append_data(row, year, month, day, grade, course, grade_list, course_list,
                subjects_before_change, subjects_after_change, weekday_list):
    # date_list.append(year + month + day)
    weekday_list.append(dt.date(year, month, day).strftime('%a'))
    subjects_after_change.append(df['変更後科目'][row])
    subjects_before_change.append(df['変更前科目'][row])

    # 本科と専攻科の区別
    if grade == 'A':
        grade_list.append('AP')
        course_list.append(course)
    else:
        grade_list.append(grade)
        course_list.append(course)
    # print(grade_list)


def gen_changed_data():
    # 別の場所で関数を呼び出したとしても常に値が同じになるように初期化
    date_list = []
    grade_list = []
    course_list = []
    time_period_list = []
    subjects_before_change = []
    subjects_after_change = []
    weekday_list = []
    data_length = 0
    for row in range(line_count):
        date_list.append((df['日付'][row]).replace('/', ''))
        year = int(df['日付'][row][:4])
        month = int(df['日付'][row][5:7])
        day = int(df['日付'][row][8:10])
        grade = df['クラス'][row][0]
        course = df['クラス'][row][2]

        append_data(row, year, month, day, grade, course, grade_list,
                    course_list, subjects_before_change, subjects_after_change,
                    weekday_list)
        time_period_list.append(df['時限'][row][0])
        if len(str(df['時限'][row])) == 3:
            # print('a')
            # print(grade_list)
            append_data(row, year, month, day, grade, course, grade_list,
                        course_list, subjects_before_change,
                        subjects_after_change, weekday_list)
            time_period_list.append(df['時限'][row][2])
            date_list.append((df['日付'][row]).replace('/', ''))
            # print(time_period_list)
            # print(grade_list)
        # print(grade_list)
    # print(date_list)
    # print(type(time_period_list[0]))
    # for i in range(line_count):
    #     print(i, date_list[i], time_period_list[i])
    data_length = len(date_list)
    # print(grade_list)
    print(len(date_list), len(grade_list), len(course_list),
          len(time_period_list), len(subjects_after_change), data_length)
    return date_list, grade_list, course_list, time_period_list, subjects_after_change, data_length


# print(gen_changed_data)
# date_list, grades_list, course_list, time_period_list, subjects_after_change, data_length = gen_changed_data(
# )
gen_changed_data()
# print(len(date_list))
# print(grades_list)
# for i in range(line_count):
#     print(i, date_list[i], time_period_list[i])
# print(time_period_list)
