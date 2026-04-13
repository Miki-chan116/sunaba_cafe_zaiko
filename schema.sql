-- USERS テーブル
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    created_at DATETIME
);

-- CATEGORIES テーブル
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_at DATETIME
);

-- SUPPLIERS テーブル
CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    address TEXT,
    created_at DATETIME
);

-- ITEMS テーブル
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category_id INTEGER,
    supplier_id INTEGER,
    stock_quantity INTEGER DEFAULT 0,
    unit TEXT,
    created_at DATETIME,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

-- STOCK_LOGS テーブル
CREATE TABLE stock_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER,
    user_id INTEGER,
    type TEXT,
    quantity INTEGER,
    created_at DATETIME,
    FOREIGN KEY (item_id) REFERENCES items(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

