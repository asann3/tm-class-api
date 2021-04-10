from flask import Flask, jsonify, request
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False  # ソートをそのまま

# APP_ROOT = os.getenv("APP_ROOT")

@app.route('/', methods=['GET'])
def index():
    return "Hello Flask Test docker"


# 範囲外(7, 8などがない場合や, 9時間目以上)
# 教員名, apiのversion, 変更しやすさ
# ルートディレクトリに何を配置するか
# エラーハンドリング
# urlのフィールド
# エンドポイントのスラッシュ 有無

@app.route('/classes/4/5/<dayOfWeek>', methods=['GET'])
def foo(dayOfWeek):
    if request.method == 'GET':
        if dayOfWeek == "Mon":
            data = [{
                "time": 1,
                "subject": "応用物理i"
            }, {
                "time": 2,
                "subject": "応用物理i"
            }, {
                "time": 3,
                "subject": "ソフトウェア工学"
            }, {
                "time": 4,
                "subject": "ソフトウェア工学"
            }, {
                "time": 5,
                "subject": "ソフトウェアデザイン演習ii"
            }, {
                "time": 6,
                "subject": "ソフトウェアデザイン演習ii"
            }]

        if dayOfWeek == "Tue":
            data = [{
                "time": 1,
                "subject": "専門選択"
            }, {
                "time": 2,
                "subject": "専門選択"
            }, {
                "time": 3,
                "subject": "一般選択"
            }, {
                "time": 4,
                "subject": "一般選択"
            }, {
                "time": 5,
                "subject": "ビジネスi"
            }, {
                "time": 6,
                "subject": "ビジネスi"
            }]

        if dayOfWeek == "Wed":
            data = [{
                "time": 1,
                "subject": "英語ivC"
            }, {
                "time": 2,
                "subject": "英語ivC"
            }, {
                "time": 3,
                "subject": "ハードウェア総論"
            }, {
                "time": 4,
                "subject": "ハードウェア総論"
            }, {
                "time": 5,
                "subject": "応用数学i"
            }, {
                "time": 6,
                "subject": "応用数学i"
            }, {
                "time": 7,
                "subject": "HR"
            }]

        if dayOfWeek == "Thu":
            data = [{
                "time": 1,
                "subject": "回路理論ii"
            }, {
                "time": 2,
                "subject": "回路理論ii"
            }, {
                "time": 5,
                "subject": "情報科学・工学実験iii"
            }, {
                "time": 6,
                "subject": "情報科学・工学実験iii"
            }, {
                "time": 7,
                "subject": "情報科学・工学実験iii"
            }]
        if dayOfWeek == "Fri":
            data = [{
                "time": 1,
                "subject": "データベース"
            }, {
                "time": 2,
                "subject": "データベース"
            }, {
                "time": 3,
                "subject": "情報数学"
            }, {
                "time": 4,
                "subject": "情報数学"
            }]
        # else:
        #     data =
        result = {'status': 'OK', 'data': data}
    return jsonify(result), 200


@app.errorhandler(400)
@app.errorhandler(404)
def error_handler(error):
    return jsonify
    ({
        'error': {
            'code': error.description['code'],
            'message': error.description['message']
        }
    }), error.code


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
