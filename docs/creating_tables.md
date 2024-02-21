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

Since I have to change the previous "commenti" table, I have to drop it, meaning deleting it,
before running the create table command

```sql
DROP TABLE "commenti";
```

The `immagine_commento` field as a TEXT type, which allows for storing the file path to the
image and also permits null values if an image is not present
```sql
CREATE TABLE "commenti" (
	"id"	INTEGER NOT NULL,
	"data_pubblicazione"	INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"testo"	TEXT NOT NULL,
	"id_post"	INTEGER NOT NULL,
	"id_utente"	INTEGER, -- This can be null if it is Anonymous
	"Valutazione"	INTEGER CHECK ("Valutazione" >= 1 AND "Valutazione" <= 5 OR "Valutazione" IS NULL),
	"immagine_commento"	TEXT,  -- This field stores the path to the image
	PRIMARY KEY("id"),
	FOREIGN KEY("id_utente") REFERENCES "utenti"("id"),
	FOREIGN KEY("id_post") REFERENCES "posts"("id")
);
```

## Examples of adding and removing rows into a table (beware the costraints(!))

Adding a row into commenti
```sql
INSERT INTO commenti (data_pubblicazione, testo, id_utente, id_post, Valutazione, immagine_commento)
VALUES ('2024-02-20', 'This is a new comment.', 1, 1, 5, NULL);

```

Deleting a row that is into commenti
```sql
DELETE FROM commenti WHERE data_pubblicazione = '2024-02-20' AND testo = 'This is a new comment.' AND id_utente = 1 AND id_post = 1 AND Valutazione = 5 AND immagine_commento = NULL;
```
