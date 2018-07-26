import os

from discogs_client import Client

user_token = os.environ.get('DISCOGS_TOKEN')

dgs_client = Client('EventbriteTest/1.2.1', user_token=user_token)


def get_images(artist_id):
    artist = dgs_client.artist(artist_id)
    images = []

    if artist.images:
        images = [
        {
            'image': {
                'url': image['resource_url'],
                'width': image['width'],
                'height': image['height'],
                'thumb_width': 150,
                'thumb_height': 150,
                'thumb_url': image['uri150'],
                'image_type': image['type'],
            }
        }
        for image in artist.images
        ]

    return images
