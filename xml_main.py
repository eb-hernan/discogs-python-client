import sys
import time
import os

from utils import (
    hms_string,
)
from xml_parser import (
    parser,
)

def main(argv):
    # validate XML data
    if len(argv) < 1:
        print 'Missing XML file input'
        print 'xml_main.py <inputfile>'
        sys.exit(2)

    start_time = time.time()

    count_artist = 0

    pathXML = argv[0]

    print('Parsing file {}\n'.format(pathXML))

    for artist in parser(pathXML):
        count_artist += 1
        print(u'Artist {0}: {1}\n'.format(count_artist, artist))

    elapsed_time = time.time() - start_time

    print('Elapsed time: {}'.format(hms_string(elapsed_time)))
    print('Artists Parsed: {}'.format(count_artist))

if __name__ == '__main__':
   main(sys.argv[1:])
