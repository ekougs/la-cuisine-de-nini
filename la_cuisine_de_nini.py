from la_cuisine_de_nini.data.menu_parser import MenuSchema
from la_cuisine_de_nini.data.menu_provider import MenuAsStrJsonEditorOnlineProvider

if __name__ == "__main__":
    menu_as_str = MenuAsStrJsonEditorOnlineProvider().get()
    print('valid', not bool(MenuSchema().validate(menu_as_str)))
