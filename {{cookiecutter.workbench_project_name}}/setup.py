from setuptools import setup
import os
# from freecad.{{cookiecutter.workbench_module_name}}.version import __version__
# name: this is the name of the distribution.
# Packages using the same name here cannot be installed together

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 
                            "freecad", "{{cookiecutter.workbench_module_name}}", "version.py")
with open(version_path) as fp:
    exec(fp.read())

setup(name='freecad.{{cookiecutter.workbench_module_name}}',
      version=str(__version__),
      packages=['freecad',
                'freecad.{{cookiecutter.workbench_module_name}}'],
      maintainer="{{cookiecutter.workbench_maintainer_name}}",
      maintainer_email="{{cookiecutter.workbench_maintainer_email}}",
      url="{{cookiecutter.workbench_project_url}}",
      description="{{cookiecutter.workbench_description}}",
      install_requires=[{{cookiecutter.workbench_dependencies}}] , # should be satisfied by FreeCAD's system dependencies already
      include_package_data=True)
