CREATE TABLE ip_desc(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title STRING,
    Description TEXT
);

-- Locations Table
CREATE TABLE ip_locs(
    Id INTEGER,
    Location POINT,
    FOREIGN KEY(Id) REFERENCES ip_desc(Id)
);


CREATE TABLE images(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Caption TEXT,
    FsLocation STRING
);

CREATE TABLE img_locs(
    Id INTEGER,
    Location POINT,
    FOREIGN KEY(Id) REFERENCES images(Id)
);


INSERT INTO ip_desc (Title, Description) VALUES("Vindhya Canteen", "Shitty Food");
INSERT INTO ip_locs (Id, Location) VALUES(1, GeomFromText('POINT(1 1)'));
