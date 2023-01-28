'''
This is the utility file for the World of Games platform.
'''
from __future__ import print_function, unicode_literals

import os, time, datetime, re


def error_logging(error):
  path = "Data/error-log"
  now = str(datetime.datetime.now())
  os.makedirs(path, exist_ok=True)
  with open('Data/error-log/error.log', 'a') as f:
    f.write(now + ": " + error + "\n")
    f.close()

BAD_RETURN_CODE = {"2001": "Cannot install requirements!",
                   "3001": "cannot open playerdata.dat (scores file). check file exists/corrupted",
                   "4001": "Game module doesn't contain an appropriate about() function. cannot add to menu module: ",
                   "4002": "Failed importing game module. check that game module is in the correct python format.",
                   "4003": "Game module Play function is corrupted or doesnt exist. check game module: "}



if __name__ == "__main__":
    print("This file needs to be run from MainGame.py thank and have a nice day")
    input("Press Enter to continue...")
