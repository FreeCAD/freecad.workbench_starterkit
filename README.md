# FreeCAD Workbench Starter Kit

Template for generating FreeCAD workbenches.

## Dependencies

* python3
* [cookiecutter](https://cookiecutter.readthedocs.io)

## Quick Start

### Create a workbench

Launch cookiecutter and point it at the template repo:

```bash
$ cookiecutter https://github.com/FreeCAD/freecad.workbench_starterkit.git
```

Answer the questions:

```bash
  [1/13] workbench_project_name (cool_wb): 
  [2/13] workbench_module_name (cool_wb): 
  [3/13] workbench_class_name (CoolWorkbench): 
  [4/13] workbench_menu_text (cool workbench): 
  [5/13] workbench_tooltip (FreeCAD workbench to make cool parametric objects): 
  [6/13] workbench_icon (cool.svg): 
  [7/13] workbench_translation_context (cool): 
  [8/13] maintainer_name (me): 
  [9/13] maintainer_email (me@foobar.com): 
  [10/13] project_url (https://foobar.com/me/coolWB): 
  [11/13] description (The cool WB creates cool parametric objects): 
  [12/13] dependencies ('numpy',): 
  [13/13] version (0.1.0): 
```

Voila, the workbench has been created:

```bash
$ find cool_wb/
```

Shows...

```bash
cool_wb/
cool_wb/setup.py
cool_wb/docs
cool_wb/docs/HISTORICAL_README.md
cool_wb/docs/commands.md
cool_wb/MANIFEST.in
cool_wb/freecad
cool_wb/freecad/cool_wb
cool_wb/freecad/cool_wb/init_gui.py
cool_wb/freecad/cool_wb/TranslateUtils.py
cool_wb/freecad/cool_wb/version.py
cool_wb/freecad/cool_wb/__init__.py
cool_wb/freecad/cool_wb/my_numpy_function.py
cool_wb/freecad/cool_wb/resources
cool_wb/freecad/cool_wb/resources/cool.svg
cool_wb/freecad/cool_wb/resources/translations
cool_wb/freecad/cool_wb/resources/translations/workbench_starterkit_es-ES.ts
cool_wb/freecad/cool_wb/resources/translations/update_translation.sh
cool_wb/freecad/cool_wb/resources/translations/workbench_starterkit_es-ES.qm
cool_wb/README.md
cool_wb/LICENSE
```

### Install the workbench

The easiest way (I've found) to install a newly created workbench is to just symlink it into the `Mod` directory.

```bash
# cd to the Mod directory of your FreeCAD installation]
cd [FreeCAD installation directory]/Mod
ln -s [path to the created workbench] CoolWB
cd ..
./bin/FreeCAD
```

Look for the workbench in the FreeCAD toolbar, it should be there.

## Documentation

For much deeper documentation, see the generated docs/HISTORICAL_README.md.

## Maintainer

TODO: who's the maintainer for this?
