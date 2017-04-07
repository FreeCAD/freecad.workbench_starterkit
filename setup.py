from setuptools import setup
from freecad.template_extension import __version__
# name: this is the name pip is using.
# Packages using the same name here cannot be installed together

setup(name='template-extension',
      version=str(__version__),
      packages=['freecad',
                'freecad.template_extension'],
      maintainer="looooo",
      maintainer_email="sppedflyer@gmail.com",
      url="https://github.com/looooo/TemplateExtension",
      description="template for freecad extensions, installable with pip",
      install_requires=['numpy'],
      include_package_data=True)
