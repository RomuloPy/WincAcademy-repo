# Three technical elements of my implementation:


1.	Double export of the data – The program exports the Stock and Products data into two files .xlsx and .csv so the user can use them in different purposes.


2. Read-friendly table – The module “beautifultable” allowed me to show the Products and Stock on an organized and read-friendly table. Another option could be the module “pandas”.

 
3. Using add_subparsers() method – The argparse module makes it easy to write user-friendly command-line interfaces. Using the add_subparsers() method allowed the program to give different results based on the different command-line inputs.