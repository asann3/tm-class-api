from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False  # ソートをそのまま

# url =


@app.route('/', methods=['GET'])
def index():
    return "Hello Flask Test docker"


# 範囲外(7, 8などがない場合や, 9時間目以上)


@app.route('/classes/1/<dayOfWeek>', methods=['GET'])
def foo(dayOfWeek):
    if request.method == 'GET':
        if dayOfWeek == "Mon":
            data = {
                1: "応用物理i",
                2: "応用物理i",
                3: "ソフトウェア工学",
                4: "ソフトウェア工学",
                5: "ソフトウェアデザイン演習ii",
                6: "ソフトウェアデザイン演習ii"
            }
        if dayOfWeek == "Tue":
            data = {
                1: "専門選択",
                2: "専門選択",
                3: "一般選択",
                4: "一般選択",
                5: "ビジネスi",
                6: "ビジネスi"
            }
        if dayOfWeek == "Wed":
            data = {
                1: "英語ivC",
                2: "英語ivC",
                3: "ハードウェア総論",
                4: "ハードウェア総論",
                5: "応用数学i",
                6: "応用数学i",
                7: "HR"
            }
        if dayOfWeek == "Thu":
            data = {1: "回路理論ii", 2: "回路理論ii", 5: "情報科学・工学実験", 6: "情報科学・工学実験"}
        if dayOfWeek == "Fri":
            data = {1: "データベース", 2: "データベース", 3: "情報数学", 4: "情報数学"}
        # else:
        #     data =

    return jsonify({'status': 'OK', 'body': data})


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
