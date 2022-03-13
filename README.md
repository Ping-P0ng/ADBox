
![ADBox](./screenshot/AD.png "ADBox")

ADBox is a viewer for active directory objects.


# Installation

```bash
pip3 install ADBox
```
#### or
```bash
python3 setup.py install
```

# Usage

- #### dump - module for extracting AD objects (users/computers/groups) and saving to the database (sqlite3)
```bash
    python3 -m ADBox -m dump -srv 192.168.1.100 -usr TEST\user -passwd TestPassword
```
- #### gui - graphical interface for viewing objects
```bash
    python3 -m ADBox -m gui
```

# Screenshots

![Example](./screenshot/Example.png?raw=true "Example")