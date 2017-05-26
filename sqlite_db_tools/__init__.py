
import sqlite3
import sys
import os


def copy_table(src_table, src_db, dest_table, dest_db):
    source = open_connection(src_db)
    dest = open_connection(dest_db)
    print('Copying data from db {} to db {}.'.format(src_db, dest_db))
    src_data = source.execute('select * from ' + src_table)
    for row in src_data.fetchall():
        cols = tuple([k for k in row.keys()])
        # Create basic insert statement that will be populated with values
        ins = 'INSERT OR REPLACE INTO {} {} VALUES ({})'.format(
            dest_table, cols, ','.join(['?'] * len(cols))
        )
        values = [row[c] for c in cols]
        dest.execute(ins, values)
    dest.commit()
    source.close()
    dest.close()


def open_connection(db_location):
    db = sqlite3.connect(db_location)
    # Let row be dict/tuple type
    db.row_factory = sqlite3.Row
    print('Opened database: {}'.format(db_location))
    return db


class Copier():

    def __init__(self, source, destination, table):
        self.source = source
        self.destination = destination
        self.source_table = table
        self.dest_table = table
