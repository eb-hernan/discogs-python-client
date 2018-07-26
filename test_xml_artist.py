import sys
import time

from utils import (
    hms_string,
)
from xml_parser import (
    parse_artists,
)

def main(argv):
    if len(argv) < 1:
        print 'Missing XML file input'
        print 'test_xml_artist.py <inputfile>'
        sys.exit(2)

    start_time = time.time()

    count_artist = 0

    pathXML = argv[0]

    print('Parsing artist file {}\n'.format(pathXML))

    for artist in parse_artists(pathXML):
        count_artist += 1
        print(u'Artist {0}: {1}\n'.format(count_artist, artist))

    elapsed_time = time.time() - start_time

    print('Elapsed time: {}'.format(hms_string(elapsed_time)))
    print('Artists Parsed: {}'.format(count_artist))

if __name__ == '__main__':
   main(sys.argv[1:])
