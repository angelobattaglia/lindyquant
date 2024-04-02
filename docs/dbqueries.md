# Queries for creating tables into the db

## Creating a Table using an SQL command to execute
To reference the `id` column in the `utenti` table as a foreign key in your `posts` table, you need to modify the FOREIGN KEY constraint
part of your table creation statement. You should specify the table and column you are referencing after the `REFERENCES` keyword.
Here's how you can do it:

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
)

CREATE TABLE "posts" (
    "id"    INTEGER PRIMARY KEY,
    "nickname"    TEXT NOT NULL,
    "date"    INTEGER NOT NULL,
    "text"    TEXT NOT NULL,
    "immagine_post"    TEXT,
    "id_utente"    INTEGER NOT NULL,
    FOREIGN KEY("id_utente") REFERENCES "utenti"("id")
)

```sql
CREATE TABLE "posts" (
	"id"	INTEGER NOT NULL,
	"nickname"	TEXT NOT NULL,
	"date"	INTEGER NOT NULL,
	"text"	TEXT NOT NULL,
	"immagine_post"	TEXT NOT NULL,
	"id_utente"	INTEGER NOT NULL,
	FOREIGN KEY("id_utente") REFERENCES "utenti"("id"),
	PRIMARY KEY("id")
);
```
In this statement, `FOREIGN KEY("id_utente") REFERENCES "utenti"("id")` establishes a foreign key relationship between the `id_utente` column in the `posts` table and the `id` column in the `utenti` table. This means that every value in the `id_utente` column must also exist in the `id` column of the `utenti` table, ensuring referential integrity between these two tables.

```sql
CREATE TABLE "commenti" (
	"id"	INTEGER NOT NULL,
	"data_pubblicazione"	INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"testo"	TEXT NOT NULL,
	"id_post"	INTEGER NOT NULL,
	"id_utente"	INTEGER, -- Could be null if Anonymous
	"Valutazione"	INTEGER CHECK ("Valutazione" >= 1 AND "Valutazione" <= 5 OR "Valutazione" IS NULL),
	"immagine_commento"	TEXT,  -- This field stores the path to the image
	PRIMARY KEY("id"),
	FOREIGN KEY("id_utente") REFERENCES "utenti"("id"),
	FOREIGN KEY("id_post") REFERENCES "posts"("id")
);
```
In this modified schema, whenever a new row is inserted into the posts table without specifying a value for the immagine_post column, 'default_image.png' will be used as the default value for that column.

```sql
CREATE TABLE "utenti" (
	"id"	INTEGER NOT NULL,
	"nickname"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"immagine_profilo"	INTEGER NOT NULL,
	PRIMARY KEY("id")
)
```

