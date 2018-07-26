# discogs-python-client
DiscoGS Python client

## Requirements

1. Verify python 2.7 version `python --version`

2. Verify pip 9 version `pip2 --version`

3. Verify virtualenv 15 version `virtualenv --version`

Note: If one missed install it via `brew` or `easy_install` (install global packages like `virtualenv`) and `pip` (install python packages in a local environment)

## Virtual Environment

1. Create a virtual environment `mkvirtualenv discogs-python-client`

2. `cd discogs-python-client`

3. Activate the virtual environment `workon discogs-python-client`

4. Install the dependencies `pip2 install -r requirements.txt`

5. Deactivate virtual environment once done `deactivate`

## XML Parser

1. Test XML Parser `python xml_main.py artist_test.xml`
