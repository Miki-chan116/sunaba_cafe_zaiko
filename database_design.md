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

# sunaba_cafe_zaiko データベース設計

## 概要
喫茶店の在庫管理を行うためのデータベース設計。

商品、カテゴリ、仕入先、在庫の入出庫履歴を管理する。

---

## ER図

```mermaid
erDiagram

    USERS {
        int id PK
        string name
        string email
        datetime created_at
    }

    CATEGORIES {
        int id PK
        string name
        datetime created_at
    }

    SUPPLIERS {
        int id PK
        string name
        string phone
        string address
        datetime created_at
    }

    ITEMS {
        int id PK
        string name
        int category_id FK
        int supplier_id FK
        int stock_quantity
        string unit
        datetime created_at
    }

    STOCK_LOGS {
        int id PK
        int item_id FK
        int user_id FK
        string type
        int quantity
        datetime created_at
    }

    CATEGORIES ||--o{ ITEMS : categorizes
    SUPPLIERS ||--o{ ITEMS : supplies
    ITEMS ||--o{ STOCK_LOGS : has
    USERS ||--o{ STOCK_LOGS : records