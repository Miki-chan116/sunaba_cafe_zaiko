from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# DB接続
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# 一覧表示
# =========================
@app.route("/")
def index():
    search = request.args.get("search", "")

    conn = get_db()

    if search:
        items = conn.execute(
            "SELECT * FROM items WHERE name LIKE ?",
            ('%' + search + '%',)
        ).fetchall()
    else:
        items = conn.execute("SELECT * FROM items").fetchall()

    conn.close()
    return render_template("index.html", items=items)


# =========================
# 商品追加
# =========================
@app.route("/add_item", methods=["POST"])
def add_item():
    name = request.form["name"]

    conn = get_db()
    conn.execute(
        "INSERT INTO items (name, stock_quantity) VALUES (?, 0)",
        (name,)
    )
    conn.commit()
    conn.close()

    return redirect("/")


# =========================
# 在庫追加
# =========================
@app.route("/add_stock/<int:item_id>")
def add_stock(item_id):
    conn = get_db()

    conn.execute(
        "UPDATE items SET stock_quantity = stock_quantity + 1 WHERE id = ?",
        (item_id,)
    )

    # 履歴追加
    conn.execute(
        "INSERT INTO history (item_id, action, amount) VALUES (?, ?, ?)",
        (item_id, "add", 1)
    )

    conn.commit()
    conn.close()

    return redirect("/")


# =========================
# 在庫減少
# =========================
@app.route("/remove_stock/<int:item_id>")
def remove_stock(item_id):
    conn = get_db()

    item = conn.execute(
        "SELECT stock_quantity FROM items WHERE id = ?",
        (item_id,)
    ).fetchone()

    if item and item["stock_quantity"] > 0:

        conn.execute(
            "UPDATE items SET stock_quantity = stock_quantity - 1 WHERE id = ?",
            (item_id,)
        )

        # 履歴追加
        conn.execute(
            "INSERT INTO history (item_id, action, amount) VALUES (?, ?, ?)",
            (item_id, "remove", 1)
        )

    conn.commit()
    conn.close()

    return redirect("/")


# =========================
# 商品削除
# =========================
@app.route("/delete_item/<int:item_id>")
def delete_item(item_id):
    conn = get_db()

    conn.execute(
        "DELETE FROM items WHERE id = ?",
        (item_id,)
    )

    # 履歴
    conn.execute(
        "INSERT INTO history (item_id, action, amount) VALUES (?, ?, ?)",
        (item_id, "delete", 0)
    )

    conn.commit()
    conn.close()

    return redirect("/")


# =========================
# 履歴表示
# =========================
@app.route("/history")
def history():
    conn = get_db()

    logs = conn.execute("""
        SELECT * FROM history
        ORDER BY created_at DESC
    """).fetchall()

    conn.close()

    return render_template("history.html", logs=logs)


# =========================
# サーバー起動
# =========================
if __name__ == "__main__":
    app.run(debug=True, port=5001)