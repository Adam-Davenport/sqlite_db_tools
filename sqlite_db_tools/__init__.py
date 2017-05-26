
import sqlite3
import sys
import os


def copy_table(src_table, src_db, dest_table, dest_db):
    source = open_connection(src_db)
    dest = open_connection(dest_db)
    print('Copying data from db {} to db {}.'.format(src_db, dest_db))
    src_data = source.execute('select * from ' + src_table)
    dest_data = dest.cursor()
    for row in src_data.fetchall():
        
        cols = tuple([k for k in row.keys() if k != 'id'])
        ins = 'INSERT OR REPLACE INTO %s %s VALUES (%s)' % (
            dest_table, cols, ','.join(['?'] * len(cols))
        )
        print('INSERT stmt = ' + ins)

        # values = ','.join(str(c) for c in row)
        # print(values)
        # ins = 'insert into {} values ({})'.format(
        #   dest_table, values
        # )
        # dest.execute(ins)


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
