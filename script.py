import os
import shutil
import subprocess

from memoize import memoize
from throttle import RateLimited

shutil.rmtree('rebrickable',ignore_errors=True)
command = ['java','-jar','swagger-codegen-cli-2.2.2.jar','generate','-l','python','-i','rebrickable.json','-o','rebrickable']
subprocess.call(command)

# import http.client
# http.client.HTTPConnection.debuglevel = 2
from rebrickable.swagger_client import ApiClient
from rebrickable.swagger_client import Configuration
from rebrickable.swagger_client import LegoApi
import pprint
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

config=Configuration()
config.host='https://rebrickable.com'
config.api_key=os.environ['REBRICKABLE_API_KEY']

api_client = ApiClient(header_name='Authorization',header_value='key '+config.api_key)
api = LegoApi(api_client)

api_client.call_api = memoize(RateLimited(2)(api_client.call_api))

themes = api.lego_themes_list()


def filter_theme(t,p):
    print(p.name)
    return p.name == "Harry Potter"

filtered_themes=[]
for result_theme in themes.results:
    if result_theme.parent_id is not None:
        theme = api.lego_themes_read(result_theme.id)
        parent_theme = api.lego_themes_read(theme.parent_id)

        if filter_theme(theme,parent_theme):
            print(parent_theme.name + ":" + theme.name)
            filtered_themes.append(theme)

theme_parts = {}
for theme in filtered_themes:
    sets = api.lego_sets_list(theme_id=theme.id)

    for set in sets.results:
        parts = api.lego_sets_parts_list(set_num=set)
        pass



pprint.pprint(theme)

