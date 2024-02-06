## Interaction with the Database (SQLite)

To open an SQLite database file (.db) from the command line, 
you can use the sqlite3 command-line tool.

```shell
sqlite3 /full/path/to/example.db
```

You can use the .schema command to display the schema (table structure) 
of the currently connected database. This command will display the schema
for all tables in the connected database.

```SQL
.schema
```

the .schema command shows the structure of the tables, 
while the SELECT * FROM table_name; command shows the 
actual data in the table. To see the schema for a specific
table, you can use:
```SQL
.schema table_name
```

Additionally, if you want to see the actual data in a table,
you can use a SELECT statement:

```SQL
SELECT * FROM table_name;
```

Once you are in the SQLite shell (sqlite> prompt), 
enter the following command to list all tables:

```SQL
.tables
```

For each table listed, use the DROP TABLE statement to delete it:

```SQL
DROP TABLE table_name;
```

Empty Table: The table might be empty. You can check this by running:

```SQL
SELECT COUNT(*) FROM users;
```
If the result is 0, the table is empty.



# Cannot add a non null column with default value null

SQLite doesn't allow altering a column to add a NOT NULL constraint directly. You would need to create a new table with the desired structure, copy the data from the old table to the new table, drop the old table, and then rename the new table to the original name. This process is a bit involved and requires careful handling to avoid data loss.

