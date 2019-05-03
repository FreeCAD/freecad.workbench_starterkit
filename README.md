# FreeCAD Workbench-Starterkit

This is a template for a FreeCAD workbench / module. As python-packaging and packaging for FreeCAD is not an easy task, this repository should give a overview of the things learned so far. If all you want is to create an extension for FreeCAD (module, additional gui-stuff, workbench), simple copy this repo and start replacing things.

To try the latest release of this template:
```bash
pip install freecad.workbench_starterkit
# pip uninstall freecad.workbench_starterkit # to remove
```

## Structure of a workbench:

### files:

- `init.py`: optional, is called at startup. With gui and without gui.
- `init_gui.py`: mandatory for modules adding new functionality to the GUI
- `__init__.py`: entry function for python. Called when you import your package: `from freecad import my_package`

### minimal structure of a namespace-package adding a workbench to FreeCAD

```
freecad/
├── __init__.py
└── workbench_starterkit/
    ├── __init__.py
    ├── init_gui.py
    └── (init.py)
```

`init.py` and `init_gui.py` are called at startup of FreeCAD. Do not put very time-intensive code in these files to reduce the start-up time.


## Naming of freecad modules

Several names are needed:
- repository-name   
eg.: `freecad.workbench_starterkit`

- the distribution-name  
This name is set in the [setup.py](setup.py) ->
eg.: `name='freecad.workbench_starterkit'`

- the package-name  
The name of the package which can be imported from python. Note that it's possible that there are several packages in one repository with only one setup.py. You simple specify all packages and modules in the `packages` section of the setup.py.
This name must not contain any python operator symbols like "-".
If the repository contains only one pthon-package it makes sense to choose the same names for the repository-name, python-package and the pypi-package.
eg.: `freecad.workbench_starterkit`


## rules

**The "freecad" namespace is not allowed to be used directly.** This means it is not allowed to set any variables in the `__init__.py` of freecad. (But as with python3 this `__init__.py` should not exist anyway, this isn't a problem.) Further it's not allowed to add variables to the freecad-namespace directly. This can introduce name-clashes.

not allowed: `freecad.myVariable = 10` allowed: `freecad.app.myVariable = 10`


## test your module/ workbench

If you want to work on your extension you have the following options:

- start FreeCAD from the root-directory you are working in (eg. workbench_starterkit)
- simple link the extension to a location where python can find it.
- pip install -e . adds the root-directory to easy_install.path.

## using pip (setuptool or distutlis)

Currently freecad has several ways to install packages [1], [2]. With pip and pypi a third option is introduced. Using pip will give advanced possebilities to install dependencies.

### setup file

The `setup.py` file located in the main directory is a minimal example to get a extension installed. There we are using setuptools. If you need advanced options to install your package, please have a look at the documentation of [setuptools](here: https://setuptools.readthedocs.io/en/latest/).

### versions

It's common practise to include a version-string in the python-package. The version should then be imported to the root-`__init__.py` to use it like this:

```python
import freecad.workbench_starterkit
freecad.workbench_starterkit.__version__
```

In the setup.py we do not have access to the library itself, so the `__vesion__` must be imported without the assumption that the package is installed. This can be done by running the file directly with `exec`.   
TODO: Is there any better way to do this?

### resources

Additional to the `setup.py` there is often the need for a `MANIFEST.in`[3] With this file it's possible to install data like icons, documentation files, ... (everything not directly connected to python).<br>
To tell setuptools to use the `MANIFEST.in` add this line to the setup function in the setup.py:

```
setup(..., include_package_data=True)
```

### dependencies

you can specify required packages by setting the `install_requires` in the setup-function of the `setup.py`

```
setup(..., install_requires=['required_package'], ...)
```

### install local

To install your extension locally with pip, do the following from a cmd (windows) or terminal (unix):

```
cd <path_to_your_package>
pip install .
```

### uploading your package to pypi

Please have a look at this [tutorial](https://pypi.python.org/pypi/twine)

Be carfully with version-numbering. It seems pypi doesn't allow to upload a package with a version smaller then the biggest version of the package uploaded. This seems to be true also for deleted packages and deleted versions.

Once uploaded the package can be installed with:

```
pip install <package-name>
```

## additional stuff

### Examples using this structure:

- [pyrate](https://github.com/mess42/pyrate)
- [OpenGlider](https://github.com/booya-at/OpenGlider)
- [FCGear](https://github.com/looooo/FCGear)
- [freecad_pipintegration](https://github.com/looooo/freecad_pipintegration)

### Some FreeCAD- and python related definitions:

- **module** : a Python source file, which can expose classes, functions and global variables
- **package** : a directory containing Python modules.
- **distribution** : the artifacts which are created by running the setup.py. Can contain multiple packages.
- **workbench** : a _graphical space_ inside the FreeCAD-Gui which adds functionality related to a specific task
- **namespace-package** : a package which add functionality to a specific namespace. For FreeCAD we are talking about packages which are importable with `from freecad import my_package`. (Sometimes it's also called new-style-module)
- **extension-module**: a library (.so / .dll) written in C/C++ which adds the possibility to import this library with python.

### Some definitions which are used in discussions, but will lead to confusion

- **freecad-module**: It's anything available through FreeCADs python interpretor and placed in FreeCADs directory structure. This can be a **module, package, workbench, namespace-package, extension-module**.
- **new_style_module**: This refers to **packages** which are added to FreeCAD as **namespace-packages**
- **old_style_module**: A **package** which is plugged into FreeCAD by adding it's base-directory to `sys.path` and uses `Init.py` and `InitGui.py` to get initialized by FreeCAD.

Due to the fact we are now using the pktutil-module to find extension of freecad, it's possible to use standard-python-paths to place the extension. This is any location which is included in the sys.path. To get a list of all the locations simple run this code in the FreeCAD-console:

```
import sys
sys.path
```

--------------------------------------------------------------------------------

[1] <https://github.com/FreeCAD/FreeCAD-addons><br>
[2] <https://github.com/microelly2/freecad-pluginloader><br>
[3] <https://docs.python.org/2/distutils/sourcedist.html#commands><br>
[4] <https://pypi.python.org/pypi/twine>
