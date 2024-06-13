# Script to convert database table to csv file(s)

This python script(s) will convert a database table(s) to csv file(s).

the main.py file accepts the name of the table to be converted as a command line argument and then generate the a csv file with the same name as the table.

create a .env file using the .env.example file as a template or supply the values for the following variables in the.env file in the running environment.

create a virtual environment and install the required packages

```bash
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

```

run the main.py script

```python

   python3 main.py  <table_name>

 ```

You can also run option2.py

```python
 python3 option2.py

 ```
