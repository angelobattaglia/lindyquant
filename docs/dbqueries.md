# Queries for creating tables into the db


## Creating a Table using an SQL command to execute
To reference the `id` column in the `utenti` table as a foreign key in your `posts` table, you need to modify the FOREIGN KEY constraint part of your table creation statement. You should specify the table and column you are referencing after the `REFERENCES` keyword. Here's how you can do it:

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