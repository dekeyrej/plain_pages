import os
from pathlib import Path

from datasourcelib import Database

def main():
    from .moonserver import MoonServer
    from .moondisplay import MoonDisplay
    from .secret_config import secretcfg, secretdef

    HERE = Path(__file__).parent.resolve()
    secretdef['file_name'] = str(HERE / secretdef['file_name'])

    MoonServer(False, 0, secretcfg, secretdef).update()  # one-shot update

    dba = Database('sqlite', {"db_path": "moon_clock.db", 
                              "db_name": "moon_clock", 
                              "tbl_name": "moon_data"})
    mdisplay = MoonDisplay(dba)
    mdisplay.update()
    mdisplay.display()
    print("🌕 moon_glance.bmp generated.")