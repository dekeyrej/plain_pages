# 🌕 Moon Clock Example

This example demonstrates how to use `plain_pages` to build a simple lunar microservice and display pipeline using only:

- `MoonServer` — a subclass of `ServerPage` that fetches sun/moon data from MET Norway
- `MoonDisplay` — a subclass of `DisplayPage` that renders a BMP image of the current moon phase and events
- SQLite — as the backing database (no Postgres or Redis required)

## 🛠️ Quick Start

1. Clone the repo, create a python virtual environment, and install dependencies:

```bash
pip install -r requirements.txt
```

- Configure for reading your secrets with SecretManager:

```python
secretcfg = {"SOURCE": "FILE"}

secretdef = {
    "file_name": "secrets.json",
    "file_type": "json"
}
```

And create secrets.json:  (updating latitude, longitude, and timezone - if you like)
```json
{
    "db_type":   "sqlite",
    "db_params": {
                    "db_path": "moon_clock.db",
                    "db_name": "moon_clock",
                    "tbl_name": "moon_data"
                },
    "met_no_email":     "use_your@email.com", // Update this with your real email!
    "latitude":  34.90161,
    "longitude": -117.02705,
    "timezone": "America/Los_Angeles",
    "rhost":    false
}
```

- Run the demo:
python run_demo.py

This will:
- Fetch lunar data from MET Norway
- Write it to a local SQLite file
- Render a moon_glance.bmp image in the static/ directory

## 🖼️ Output
The resulting image includes:
- Current moon phase icon (from img/moon/moonXX.bmp)
- Illumination percentage
- Current time and date
- Next sunrise and moonrise/set events


## 📁 File Structure
```
moon_clock/
├── moonserver.py
├── moondisplay.py
├── run_demo.py
├── devconfig.py
├── fonts/
├── img/moon/
└── static/moon.bmp
```

## 💡 Notes
- This example runs without Redis or RGB matrix hardware.
- For full matrix display support, see clientdisplay.py (not included in this minimal demo).

## 🧪 Next Steps
- Add Redis pub/sub for real-time updates
- Integrate with clientdisplay.py for LED matrix output
- Extend to other data types (weather, AQI, etc.)

### Install rpi-rgb-led-matrix

- clone it from https://github.com/hzeller/rpi-rgb-led-matrix.git
- cd rpi-rgb-led-matrix && run make
- cd bindings/python && sudo make install
- create a link to rpi-rgb-led-matrix _inside_ your python project directory