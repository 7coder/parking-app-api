DROP TABLE IF EXISTS permits;

CREATE TABLE permits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    licensePlateNumber TEXT NOT NULL,
    plateIssuerCountry TEXT NOT NULL,
    startDate TIMESTAMP,
    endDate TIMESTAMP,
    ownerName TEXT
);