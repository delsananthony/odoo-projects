
Errors encountered in dealing with Odoo 14:

* During pip install -r requirements, prompt to install Microsoft Visual C++ 2014 or higher
solution: download and install visual studio build tools 2017

* psutil, python-stdnum, passlib prompt a vague error
solution: install a higher version of the packages

* psycopg2 prompt an error when trying to run odoo
solution: install psycopg-binary

* odoo prompt an error related to psycopg2
solution: close existing window or launch a new then run odoo there. this problem most likely occurs when dealing with different odoo versions on a machine.

MP: brua-2at8-2uta