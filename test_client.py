import sys
import time
import os

from utils import (
    hms_string,
)
from xml_parser import (
    parse_artists,
)
from dgs_client import (
    get_images,
    DiscoGSError,
)

user_token = os.environ.get('DISCOGS_TOKEN')

def main(argv):
    if len(argv) < 1:
        print 'Missing XML file input'
        print 'test_client.py <inputfile>'
        sys.exit(2)

    if not user_token:
        print 'Missing DISCOGS_TOKEN environment variable'
        sys.exit(2)

    start_time = time.time()

    count_artist = 0

    pathXML = argv[0]

    print('Parsing file {}\n'.format(pathXML))

    for artist in parse_artists(pathXML):
        count_artist += 1
        try:
            artist['images'] = get_images(artist['id'])
            print(u'Artist {0}: {1}\n'.format(count_artist, artist))
        except DiscoGSError:
            print(u'Cannot get images from Artist {0}: {1}\n'.format(count_artist, artist))

    elapsed_time = time.time() - start_time

    print('Elapsed time: {}'.format(hms_string(elapsed_time)))
    print('Artists Parsed: {}'.format(count_artist))

if __name__ == '__main__':
   main(sys.argv[1:])
