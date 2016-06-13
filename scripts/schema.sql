-- Interest Point Information
CREATE TABLE ip_desc(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title STRING,
    Description TEXT
);

-- Interest Point Locations
CREATE TABLE ip_locs(
    Id INTEGER,
    Location POINT,
    FOREIGN KEY(Id) REFERENCES ip_desc(Id)
);

-- Images Information
CREATE TABLE images(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Caption TEXT,
    FsLocation STRING
);

-- Image Locations
CREATE TABLE img_locs(
    Id INTEGER,
    Location POINT,
    FOREIGN KEY(Id) REFERENCES images(Id)
);

