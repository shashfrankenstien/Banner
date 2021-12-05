# Banner

Converts string to a banner that moves on the console from right to left

# Usage

```
$ python -m pip install -r requirements.txt
```
```
$ python moving_banner.py -h

usage: python moving_banner.py [-h] [--figlet FIGLET] [--figlet-list] [-x X] [-y Y] [--width WIDTH] [--speed SPEED] [--quiet] [message]

positional arguments:
  message               message to print as banner (default: None)

optional arguments:
  -h, --help            show this help message and exit
  --figlet FIGLET, -f FIGLET
                        select figlet font name (default: banner)
  --figlet-list, -fl    list available figlet fonts (default: False)
  -x X                  horizontal wall character (default: _)
  -y Y                  vertical wall character (default: |)
  --width WIDTH, -w WIDTH
                        width of the banner (default: 269)
  --speed SPEED, -s SPEED
                        speed of the banner (default: 50)
  --quiet, -q           don't print extra text (default: False)

```

# Change Log

### v1.0.0 - 2016-05-04
- Initial check-in
- Draw border


### v2.0.0 - 2021-12-04
- Convert to Python3
- Add CLI arguments


### v3.0.0 - 2021-12-04
- Switch to Figlet fonts using pyfiglet
