# TemplateExtension
template for a FreeCAD workbench / module

## basics
As python imports seems not that easy to understand, this template should show the way how extensions work in future versions of FreeCAD.

To due the fact we are using now the pktutil-module to find extension of freecad, it's possible to use standart-paths of pyton to place the extension. This is any location which is included in the sys.path. To get a list of all the locations simple run this code in the FreeCAD-console:

```
ìmport sys
sys.path
```

## structure
- init.py: optional, is called at startup. With gui and without gui. <insert the exact use case>
- init_gui.py: mandatory for modules adding new functionality to the gui

### minimal structure of a freecad-workbench/module for python2 and 3
```
freecad/
├── __init__.py
└── modules/
    ├── __init__.py
    └── my_extension/
        ├── __init__.py
        ├── init_gui.py
        └── (init.py)
```

### minimal structure of a freecad-workbench/module for python3 (only)
```
freecad/
└── modules/
    └── my_extension/
        ├── __init__.py
        ├── init_gui.py
        └── (init.py)
```

Do not place code into `freecad/__init__.py` and `freecad/modules/__init__.py`. These files are only used to let pkgutil find your extension with python2.

`init.py` and `init_gui.py` get called at startup of FreeCAD. Do not put very time-intensive code in these files to reduce the start-up time.

## using pip
Currently freecad has several ways to install packages [1], [2]. With pip and pypi a third option is introduced. While the former two have no dependency management, using the standart python package-manager will give advanced possebilities to install dependencies.

pip can be used on all platforms as a install tool. *1 The `setup.py` file located in the main directory is a minimal example to get a extension installed. There we are using setuptools. If you need advanced optionas to install your package, please have a look at the documentation of [setuptools](here: https://setuptools.readthedocs.io/en/latest/).

Additional to the `setup.py` there is often the need for a `MANIFEST.in`[3] With this file it's possible to install data like icons, documentation files, ... (everything not directly connected to python).

To tell setuptools to use the `MANIFEST.in` add this line to the setup function in the setup.py:

```
setup(..., include_package_data=True)
```
-------------------------------------------------------------------------------
To install your extension locally with pip, do the following from a cmd (windows) or terminal (unix):
```
cd path_to_TemplateExtension
pip install .
```

If you want to work on your extension you can use the following which installs a linked version of your package:
```
cd path_to_TemplateExtension
pip install -e .
```
### dependencies
you can specify required packages by setting the `install_requires` in the setup-function of the `setup.py`
```
setup(..., install_requires=['required_package'], ...)
```

### uploading your package to pypi
Please have a look at this nice  [tutorial](http://peterdowns.com/posts/first-time-with-pypi.html) Better use twine to upload the package [4] #TODO  
Be carfully with version-numbering. It seems pypi don't allow to upload a package with a version smaller then the biggest version of the package uploaded. This seems to be true also for deleted packages and deleted verions.#

### install this template
```
pip install template-extension
```

--------------------------------------------------------------------------------

*1 With python2 it's possible pip is not available on windows, because as of now we use not the std. compiler for compiling FreeCAD and therefor std. packages are not compatible with FreeCAD. But maybe there is a chance pip gets included in the libpack...

[1] https://github.com/FreeCAD/FreeCAD-addons  
[2] https://github.com/microelly2/freecad-pluginloader  
[3] https://docs.python.org/2/distutils/sourcedist.html#commands  
[4] https://pypi.python.org/pypi/twine
