import json

import requests


class MenuAsStrProvider:
    def get(self):
        raise NotImplementedError


class MenuAsStrJsonEditorOnlineProvider(MenuAsStrProvider):
    def __init__(self, menu_json_id="9459a6c670078e035243a242a642963c"):
        self.menu_json_id = menu_json_id

    def get(self):
        cuisine_de_nini_response = requests.get(f"http://api.jsoneditoronline.org/v1/docs/{self.menu_json_id}")
        cuisine_de_nini_content_dict = \
            json.loads(s=cuisine_de_nini_response.content, encoding=cuisine_de_nini_response.encoding)
        cuisine_de_nini_dict = json.loads(cuisine_de_nini_content_dict["data"])
        return cuisine_de_nini_dict
