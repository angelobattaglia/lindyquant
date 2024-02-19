# Queries for creating SQL tables

The following if for creating a posts table with image set as a facultative value (could be NULL)
```sql
CREATE TABLE "posts" (
    "id"    INTEGER PRIMARY KEY,
    "nickname"    TEXT NOT NULL,
    "date"    INTEGER NOT NULL,
    "text"    TEXT NOT NULL,
    "immagine_post"    TEXT,
    "id_utente"    INTEGER NOT NULL,
    FOREIGN KEY("id_utente") REFERENCES "utenti"("id")
);
```

Whereas the following if for creating a posts table with image set as default value if NULL
```sql
CREATE TABLE "posts" (
    "id"    INTEGER PRIMARY KEY,
    "nickname"    TEXT NOT NULL,
    "date"    INTEGER NOT NULL,
    "text"    TEXT NOT NULL,
    "immagine_post"    TEXT DEFAULT 'img/default_image.png',
    "id_utente"    INTEGER NOT NULL,
    FOREIGN KEY("id_utente") REFERENCES "utenti"("id")
);
```
