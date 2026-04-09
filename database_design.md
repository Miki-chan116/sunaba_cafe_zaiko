# sunaba_cafe_zaiko データベース設計

## items（商品テーブル）

| カラム | 型 | 説明 |
|------|------|------|
| id | INTEGER | 商品ID |
| name | TEXT | 商品名 |
| category | TEXT | カテゴリ |
| stock | INTEGER | 在庫数 |
| unit | TEXT | 単位 |
| created_at | DATETIME | 登録日 |

---

## stock_logs（入出庫履歴）

| カラム | 型 | 説明 |
|------|------|------|
| id | INTEGER | 履歴ID |
| item_id | INTEGER | 商品ID |
| type | TEXT | 入庫 / 出庫 |
| quantity | INTEGER | 数量 |
| date | DATETIME | 日付 |