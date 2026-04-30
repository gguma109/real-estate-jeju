CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    nickname TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS rentals (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    type TEXT,
    date TEXT,
    movein TEXT,
    address TEXT,
    room TEXT,
    deposit TEXT,
    premium TEXT,
    rent TEXT,
    yearly_rent TEXT,
    maintenance TEXT,
    inc_internet BOOLEAN DEFAULT 0,
    inc_tv BOOLEAN DEFAULT 0,
    inc_water BOOLEAN DEFAULT 0,
    structure TEXT,
    options TEXT,
    special_notes TEXT,
    phone TEXT,
    common_pwd TEXT,
    unit_pwd TEXT,
    business_name TEXT,
    exclusive_area TEXT,
    supply_area TEXT,
    land_area TEXT,
    total_floor_area TEXT,
    sale_price TEXT,
    current_loan TEXT,
    completion_date TEXT,
    building_config TEXT,
    total_deposit TEXT,
    total_monthly_income TEXT,
    loan_interest_rate TEXT,
    status TEXT DEFAULT '진행중',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS notes (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    title TEXT,
    content TEXT,
    is_shared BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS ads (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    category TEXT NOT NULL,
    data TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
