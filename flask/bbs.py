from flask import *
import json, os, datetime
DATA_FILE = "bbs.json"

# Flaskオブジェクトの生成 --- (*1)
app = Flask(__name__)

# ルート( / )へアクセスがあった時の処理 --- (*2)
@app.route("/")
def root():
    # 掲示板データを読み出してHTMLを生成 --- (*3)
    body = ""
    for i in load_data():
        body += f'<li>{i[0]}: {i[1]} ({i[2]})</li>'
    return html_frame("<ul>"+body+"</ul>")

# 投稿があった時の処理 --- (*4)
@app.route("/write", methods=["post"])
def write():
    # パラメータの取得 --- (*5)
    name = request.form.get("name")
    comment = request.form.get("comment")
    if (name is None) or (comment is None) or (comment == ""):
        return redirect("/")
    if name == "": name = "名無し"
    # データファイルに書き込みを追記 --- (*6)
    data = load_data()
    now_s = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data.insert(0, [tohtml(name), tohtml(comment), now_s])
    save_data(data)
    return redirect('/')

# 保存と読み込み
def load_data():
    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rt", encoding="utf-8") as fp:
            data = json.load(fp)
    return data
def save_data(data):
    with open(DATA_FILE, "wt", encoding="utf-8") as fp:
        json.dump(data, fp)

# HTMLの大枠を表示する --- (*7)
def html_frame(body):
    return f"""
    <!DOCTYPE html><html><meta charset="utf-8"><body>
    <h1>掲示板</h1>
    <div><form action="/write" method="post">
    名前:<input name="name" size="8">
    発言:<input name="comment" size="30">
    <input type="submit" value="投稿"></form></div>
    <div>{body}</div></body></html>"""
def tohtml(s):
    return s.replace('&', '&amp;').replace('<', '&lt;') \
            .replace('>', '&gt;')

# サーバーを起動 --- (*8)
if __name__ == "__main__":
    app.run(debug=True, port=8888, host='0.0.0.0')