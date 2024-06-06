## Requierments

- python3
    - csv, tkinter and xml libraries should be bundled with the latest python version
- MariaDB Connector/Python

### Installation

MariaDB:
- Follow the official mariadb documentation: <br>https://mariadb.com/docs/server/connect/programming-languages/python/install/#Install_from_PyPI
- the installation via PyPI requires the installation for the MariaDB Connector/C: <br> https://mariadb.com/docs/server/connect/programming-languages/c/install/

## Configuration

The scripts require a database connection, which needs to be confgured:

1. Create a copy of the `db_config_example.py` file in the db directory.
2. Rename the copy to: `db_config.py`.
3. Change the returned values of the `get_db_config()` function to fit your database (login, host, port etc.).
4. Additional settings can be added if needed.

## Usage

There are two sets of scripts, the `terminal_scripts` can be exectued directly in the terminal, while the scripts in the `scripts` directory are used by the main script called `21_dropdown-vorlage.py`, which offers a gui to interact with. The `21_dropdown-vorlage.py` script still has some feedback in the terminal. 