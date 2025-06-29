# examples/moon_clock/run_demo.py

from moonserver import MoonServer
from moondisplay import MoonDisplay
from datasourcelib import Database
import arrow

from secret_config import secretcfg, secretdef

# Run the server to populate data
MoonServer(False, 0, secretcfg, secretdef).update()  # one-shot update

# Now load and render the display
dba = Database('sqlite', {"db_path": "moon_clock.db", "db_name": "moon_clock", "tbl_name": "moon_data"})
mdisplay = MoonDisplay(dba)
mdisplay.update()
mdisplay.display()
print("Rendered moon_glance.bmp")