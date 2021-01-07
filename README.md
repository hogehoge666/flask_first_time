
# 簡単なFlask Todoアプリ

Flaskで作成する簡単なTodoアプリの写経です。

---

## tag v0.1
- flaskの最小アプリ作成
- 初歩的なルーティング
- Jinja2の基本的なTemplate機能
- コンバーター
- favicon.co表示

---

## tag v0.2
- Todoアプリ（オンメモリ）作成
- View関数から外部モジュール参照
- form取得
- Jinja2の分岐、繰り返し機能
- CSS
- PyCharm CEでFlaskのデバッグ構成
- READMEの追加

---

## tag v0.3
- Todoアプリをsqlite3でPersistent化
- UI変更

---

## その他

### flaskの実行

```
export FLASK_APP=app.py
flask run
```

---

### favcon

下記のサイトで作成。

http://www.xiconeditor.com/

---

### Debug構成

Run / Edit Configuration

Module name : flask
Parameters : run
Environmental variable : PYTHONUNBUFFERED=1;FLASK_APP=app.py;FLASK_DEBUG=1

---

### sqlite3

DB初期化

```
export FLASK_APP=app.py
flask shell
from todo import db
db
db.create_all()
exit()
```

DBへ接続

```
sqlite3 ./db/todoitems.db
.table
.schema
select * from todoitems;
.quit
```

