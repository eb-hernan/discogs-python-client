import time
import os

from discogs_client import Client
from discogs_client.exceptions import HTTPError

user_token = os.environ.get('DISCOGS_TOKEN')

dgs_client = Client('EventbriteTest/1.2.1', user_token=user_token)

class DiscoGSError(RuntimeError):
    pass

def retryer(max_retries=10, timeout=5):
    def wraps(func):

        def inner(*args, **kwargs):
            for i in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                except HTTPError:
                    time.sleep(timeout)
                    continue
                else:
                    return result
            else:
                raise DiscoGSError
        return inner
    return wraps

@retryer(max_retries=10, timeout=10)
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
