# Betsy Music Webshop

### To use the webshop:

1. Run the file setupdb.py. This will create our database (database.db).
Existing or not, the file database.db will be deleted and the application will create a new one based on the setupdb.py data.
```
if __name__ == "__main__":
    delete_database()
    populate_test_data()
    
[Running] python -u "c:\Users\Romulo\OneDrive\Documentos\Winc_Academy\Assignments Back-End\Betsy Webshop\setupdb.py"
Initializing database, please wait...
Database Successfully Created!

[Done] exited with code=0 in 5.223 seconds
```
2. Go to the file main.py, remove the comments from the functionality you want to perform and run the file.

```
Eg: ###### SEARCH FUNCTION by TERM ######

    # search('hammer')
    # search('bass')
    # search('drums')
    # search('keys')

    search('hammer')
    search('bass')
    search('drums')
    search('keys')
```
3. Have fun! ;)
