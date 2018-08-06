import xml.etree.cElementTree as etree

from xml_utils import (
    calculate_level,
    strip_tag_name,
)

USE_EXTRA_ARTISTS = False

def parse_artists(pathXML):
    artist = None
    level = 0

    for event, elem in etree.iterparse(pathXML, events=('start', 'end')):
        try:
            tname = strip_tag_name(elem.tag)

            level = calculate_level(event, tname, level, 'artist')

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

def parse_genres(pathXML):
    artists = []
    artist = {}
    parsing_artist = False
    level = 0
    artist_tags = ['artists']

    for event, elem in etree.iterparse(pathXML, events=('start', 'end')):
        try:
            tname = strip_tag_name(elem.tag)

            level = calculate_level(event, tname, level, 'release')

            if event == 'start':
                if tname == 'artists':
                    artists = []
                elif tname == 'artist':
                    parsing_artist = True
                    artist = {'id': None, 'name': None, 'genres': set()}
                    artists.append(artist)

            # we might not wanna include the extraartists here
            if USE_EXTRA_ARTISTS:
                artist_tags.append('extraartists')

            if event == 'end' and tname in artist_tags:
                parsing_artist = False

            if parsing_artist and level == 4:
                if tname == 'id':
                    artist['id'] = elem.text

                if tname == 'name':
                    artist['name'] = elem.text

            # update all genre artists
            if event != 'end' and tname == 'genre':
                for artist in artists:
                    artist['genres'].add(elem.text)
            elif event == 'end' and tname == 'release':
                yield artists

        except etree.ParseError:
            print('>>>error parsing...continue')
        finally:
            elem.clear()
