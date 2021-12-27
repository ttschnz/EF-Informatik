CREATE DATABASE Konzern;
\c konzern

CREATE TABLE Artikeltyp(
    TypId INTEGER PRIMARY KEY,
    Bezeichnung VARCHAR(100),
    Preis NUMERIC(10,2)
);

CREATE TABLE Lieferant(
    LId INTEGER PRIMARY KEY,
    Name VARCHAR(50),
    Land VARCHAR(50)
);

CREATE TABLE Filiale(
    FId INTEGER PRIMARY KEY,
    Filialleiter VARCHAR(50),
    Adresse VARCHAR(100)
);

CREATE TABLE Kunde(
    KId INTEGER PRIMARY KEY,
    Steuerreferenz VARCHAR(50) 
);

CREATE TABLE bietetan(
    TypId INTEGER,
    LId INTEGER,
    Angebotspreis NUMERIC(10,2),
    FOREIGN KEY (TypId) REFERENCES Artikeltyp(TypId),
    FOREIGN KEY (LId) REFERENCES Lieferant(LId)
);

CREATE TABLE Artikel(
    AId INTEGER PRIMARY KEY,
    FId INTEGER,
    TypId INTEGER,
    LId INTEGER,
    FOREIGN KEY (FId) REFERENCES Filiale(FId),
    FOREIGN KEY (TypId) REFERENCES Artikeltyp(TypId),
    FOREIGN KEY (LId) REFERENCES Lieferant(LId)
);

CREATE TABLE kauft(
    AId INTEGER,
    KId INTEGER,
    Datum TIMESTAMP,
    FOREIGN KEY (AId) REFERENCES Artikel(AId),
    FOREIGN KEY (KId) REFERENCES Kunde(KId)
);

