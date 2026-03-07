import sys
from os.path import (
    abspath,
    dirname,
)

# Make sure plexapi is in the systempath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
