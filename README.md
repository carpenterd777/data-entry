# data-entry

A script to assist me in entering data into a database.

## Setup

```
source .venv/bin/activate
```

## Running

```
python3 ./data-entry [path]
```

## Building

```
pyinstaller --onefile __main__.py
mv dist/__main__ dist/data-entry
```