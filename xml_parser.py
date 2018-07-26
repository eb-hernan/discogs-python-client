import xml.etree.ElementTree as etree

from xml_utils import (
    calculate_level,
    strip_tag_name,
)

def parse_artists(pathXML):
    artist = None
    level = 0

    for event, elem in etree.iterparse(pathXML, events=('start', 'end')):
        try:
            tname = strip_tag_name(elem.tag)

            level = calculate_level(event, tname, level)

            if event == 'start' and tname == 'artist':
                artist = {
                    'id': None,
                    'biography': None,
                    'profile': None,
                    'social_media_links': [],
                }

            elif event != 'end' and level == 2:
                if tname == 'id':
                    artist['id'] = elem.text
                if tname == 'name':
                    artist['name'] = elem.text
                if tname == 'profile':
                    artist['profile'] = elem.text

            elif event != 'end' and level == 3:
                if tname == 'url':
                    artist['social_media_links'].append(elem.text)

            if event == 'end' and tname == 'artist':
                yield artist

        except etree.ParseError:
            print('>>>error parsing...continue')
        finally:
            elem.clear()
