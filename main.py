#!/usr/bin/env python

'''
File: main.py
Author: Dan Woodson
Description: Build api from database
'''

import sys
import argparse

class Main(object):
  """Main: Central class"""
  
  def __init__(self, arg): 

    # Setup command-line arguments
    parser = argparse.ArgumentParser(description='Generate API from database.')
    parser.add_argument('-hst', metavar='host', type=str, default='127.0.0.1', help='Where the database is hosted (default: "127.0.0.1")')
    parser.add_argument('-db', metavar='database', type=str, default='', help='The database the API is being created for', required=True)
    parser.add_argument('-u', metavar='username', type=str, default='root', help='Username to access the database (default: "root")')
    parser.add_argument('-p', metavar='password', type=str, default='', help='Password to access the database (default: "")')
     
    # Local variables
    args = parser.parse_args()
    self.db = {}
    self.db['host'] = args.hst
    self.db['database'] = args.db
    self.db['username'] = args.u
    self.db['password'] = args.p
   
    # Get database dictionary
    print self.CreateDatabaseDict()
  
  def CreateDatabaseDict(self):
    """CreateDatabaseDict: Returns a dictionary model of the database referenced in self.db"""
    
    # Local imports    
    import MySQLdb

    # Local vars
    db_dict = {}
    db_dict['tables'] = []
    db = None
    cursor = None

    # Connect to database
    db=MySQLdb.connect(host=self.db['host'],user=self.db['username'],db=self.db['database'],passwd=self.db['password'])
    cursor = db.cursor()
    
    # Get all the tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    # Move through all the tables, storing their information in db_dict
    for table in tables:
      # create structure for table
      cur_table = {}
      cur_table['name'] = table[0]
      cur_table['columns'] = []
      # get information about this table
      cursor.execute("DESCRIBE " + cur_table['name'])
      columns = cursor.fetchall()
      # move through all the columns in this table
      for column in columns:
        cur_column = {}
        cur_column['name'] = column[0]
        # check if type contains a length
        if '(' in column[1]:
          cur_column['type'] = column[1][:column[1].index('(')]
          cur_column['length'] = column[1][column[1].index('(')+1:column[1].index(')')]
        else:
          cur_column['type'] = column[0]
        cur_column['allow_null'] = column[2]
        cur_column['key'] = column[3]
        cur_column['default'] = column[4]
        cur_column['additional_instructions'] = column[5]
        # add this column to the list of columns for this table
        cur_table['columns'].append(cur_column)
      # add this table to the list of tables
      db_dict['tables'].append(cur_table)

    # Return
    return db_dict

  def CreateConfigFile(self):
    """CreateConfigFile: Creates a config file for connecting to database"""
    pass

  def LoadLanguageModule(self, requested_module):
    """LoadLanguageModule: Loads the requested language module"""
    pass

  def PrintError(self, message, kill=False):
    """PrintError: Prints an error message to the screen and terminates program if kill is set to true"""
    pass

if __name__ == '__main__':
  main = Main(sys.argv)

