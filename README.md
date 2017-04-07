# template extension
template for a FreeCAD workbench / module

## basics
As python imports seems not that easy to understand, this template should show the way how extensions work in future versions of FreeCAD.

Due to the fact we are now using the pktutil-module to find extension of freecad, it's possible to use standart-paths of pyton to place the extension. This is any location which is included in the sys.path. To get a list of all the locations simple run this code in the FreeCAD-console:

```
import sys
sys.path
```

## structure
- init.py: optional, is called at startup. With gui and without gui. <insert the exact use case>
- init_gui.py: mandatory for modules adding new functionality to the gui

#### minimal structure of a freecad-workbench/module for python2 and 3
```
freecad/
├── __init__.py
└── modules
    └── template_extension/
        ├── __init__.py
        ├── init_gui.py
        └── (init.py)
```

#### minimal structure of a freecad-workbench/module for python3 (only)
```
freecad/
└── modules/
    └── template_extension/
        ├── __init__.py
        ├── init_gui.py
        └── (init.py)
```

Do not place code into `freecad/__init__.py`. These files are only used to let pkgutil find your extension with python2.

`init.py` and `init_gui.py` get called at startup of FreeCAD. Do not put very time-intensive code in these files to reduce the start-up time.


## test your module/ workbench
If you want to work on your extension you have the following options:

- start FreeCAD from the root-directory you are working in (eg. TemplateExtension)
- simple link the extension to a location where python can find it.
- pip install -e . adds the root-directory to easy_install.path.

## using pip (setuptool or distutlis)
Currently freecad has several ways to install packages [1], [2]. With pip and pypi a third option is introduced. Using pip  will give advanced possebilities to install dependencies.

#### setup file
The `setup.py` file located in the main directory is a minimal example to get a extension installed. There we are using setuptools. If you need advanced options to install your package, please have a look at the documentation of [setuptools](here: https://setuptools.readthedocs.io/en/latest/).

#### resources
Additional to the `setup.py` there is often the need for a `MANIFEST.in`[3] With this file it's possible to install data like icons, documentation files, ... (everything not directly connected to python).  
To tell setuptools to use the `MANIFEST.in` add this line to the setup function in the setup.py:

```
setup(..., include_package_data=True)
```

#### dependencies
you can specify required packages by setting the `install_requires` in the setup-function of the `setup.py`  
```
setup(..., install_requires=['required_package'], ...)
```  

#### install local
To install your extension locally with pip, do the following from a cmd (windows) or terminal (unix):
```
cd <path_to_your_package>
pip install .
```

#### uploading your package to pypi
Please have a look at this [tutorial](https://pypi.python.org/pypi/twine)
- `python setup.py sdist`
- login to pypi  https://pypi.python.org/pypi
- PackageIndex->Package Submission
- choose the PKG-INFO in <pkg-name>.egg-info
- press "add package info"
- `twine upload dist/<package>`

Be carfully with version-numbering. It seems pypi doesn't allow to upload a package with a version smaller then the biggest version of the package uploaded. This seems to be true also for deleted packages and deleted verions.

Once uploaded the package can be installed with:
```
pip install <package-name>
```
--------------------------------------------------------------------------------

[1] https://github.com/FreeCAD/FreeCAD-addons  
[2] https://github.com/microelly2/freecad-pluginloader  
[3] https://docs.python.org/2/distutils/sourcedist.html#commands  
[4] https://pypi.python.org/pypi/twine
