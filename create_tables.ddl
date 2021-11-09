CREATE TABLE categories (
    codename CHAR (10) PRIMARY KEY,
    name     CHAR (10),
    type     CHAR (10),
    included TEXT
);

CREATE TABLE costs (
    cost_id            INTEGER   PRIMARY KEY AUTOINCREMENT,
    sum_of_money_co    INT,
    descrip_co         TEXT,
    category           CHAR (10),
    view_date          CHAR (10),
    who_posted_co_id   INT,
    who_posted_co_nick CHAR (10),
    created            DATETIME,
    FOREIGN KEY (
        category
    )
    REFERENCES categories (codename) ON UPDATE CASCADE
                                     ON DELETE CASCADE
);

CREATE TABLE income (
    income_id          INTEGER   PRIMARY KEY AUTOINCREMENT,
    sum_of_money_in    INT,
    descrip_in         TEXT,
    category           CHAR (10),
    view_date          CHAR (10),
    who_posted_in_id   INT,
    who_posted_in_nick CHAR (10),
    created            DATETIME,
    FOREIGN KEY (
        category
    )
    REFERENCES categories (codename) ON UPDATE CASCADE
                                     ON DELETE CASCADE
);
