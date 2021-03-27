# Openclassrooms Project 4

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This project goal is to make an application to manage chess tournament

## To start

### Requirements

- Python 3

### Installation

- Clone or download this repository, extract it inside a folder if necessary, then open a command prompt inside this folder.

- In the command prompt, create a new environment for the python project :

##### (You need the venv package from PiP to do it, if you don't have it, please write `pip install venv` to install it)

To create a new environment, write this command :

`virtualenv env`

Then you need to activate it :

### Windows :

```bash
cd env/Scripts

activate

cd ../..
```

### Linux/Mac Os:

```bash
source env/Scripts/activate
```

And finally, you can install the required packages for the project :

`pip install -r requirements.txt`

## Usage

Inside the project folder run the command :

`py main.py`

## Generate Flake8 report

Inside the project folder run the command:

`flake8 --html-dir ./flake-report/ --format=html ./`


## Built with

- [Python](https://www.python.org/)
- [TinyDB](https://pypi.org/project/tinydb/)
- [Colorama](https://pypi.org/project/colorama/)
- [flake8](https://pypi.org/project/flake8/)
- [flake8-html](https://pypi.org/project/flake8-html/)