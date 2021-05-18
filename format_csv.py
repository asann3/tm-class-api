import pandas as pd
import datetime as dt

# ファイルが空(授業変更がない)の時の処理

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

    # return df, line_count


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
    # df, line_count = set_datas()
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
            append_data(row, year, month, day, grade, course, grade_list,
                        course_list, subjects_before_change,
                        subjects_after_change, weekday_list)
            time_period_list.append(df['時限'][row][2])
            date_list.append((df['日付'][row]).replace('/', ''))

    print(len(date_list))
    data_length = len(date_list)
    return date_list, grade_list, course_list, time_period_list, subjects_after_change, data_length


if __name__ == "__main__":
    gen_changed_data()
