## MacOS

### Setup
Install Python 3, you can use Brew:

```console
$ brew install python3
```

Then continue to install and set up Printrun:

```console
$ git clone 
```

### Start virtual environment

```console
$ cd watertight_3d_printing  # change to directory
$ python3 -m venv venv  # create an virtual environment
$ . venv/bin/activate  # activate the virtual environment (notice the space after the dot)
(venv) $ python -m pip install -r requirements.txt  # install the rest of dependencies
(venv) $ python test_printcore.py # or python printcore.py PORT GCODE_PATH
```