# Makefile for string replacement tasks
# Replace values from starterkit to your workbench name

# Define replacements as variables
WORKBENCH_DIR_NAME = my_cool_wb
WORKBENCH_CLASS_NAME = CoolWorkbench
WORKBENCH_MENUTEXT = Cool workbench
WORKBENCH_TOOLTIP = FreeCAD workbench to make cool parametric objects
WORKBENCH_ICON = cool.svg
WORKBENCH_TRANSLATION_CONTEXT = cool
MAINTAINER = me
EMAIL = me@foobar.com
URL = https://foobar.com/me/coolWB
DESCRIPTION = The cool WB creates cool parametric objects
DEPENDENCIES_LIST = []

.PHONY: all replace_strings

all: replace_strings

replace_strings:
	@echo -e "\033[1;34mReplacing strings\033[0m"
	@# Update instances of 'workbench_starterkit' on different files
	sed -i 's/workbench_starterkit/$(WORKBENCH_DIR_NAME)/g' MANIFEST.in
	sed -i 's/workbench_starterkit/$(WORKBENCH_DIR_NAME)/g' freecad/workbench_starterkit/init_gui.py
	sed -i 's/workbench_starterkit/$(WORKBENCH_DIR_NAME)/g' freecad/workbench_starterkit/resources/translations/update_translation.sh
	sed -i 's/workbench_starterkit/$(WORKBENCH_DIR_NAME)/g' freecad/workbench_starterkit/resources/translations/workbench_starterkit_es-ES.ts
	sed -i 's/workbench_starterkit/$(WORKBENCH_DIR_NAME)/g' setup.py
	@# Rename workbench class name
	sed -i 's/TemplateWorkbench/$(WORKBENCH_CLASS_NAME)/g' freecad/workbench_starterkit/init_gui.py
	@# Rename workbench class properties
	sed -i 's/template workbench/$(WORKBENCH_MENUTEXT)/g' freecad/workbench_starterkit/init_gui.py
	sed -i 's/a simple template workbench/$(WORKBENCH_TOOLTIP)/g' freecad/workbench_starterkit/init_gui.py
	sed -i 's/template_resource.svg/$(WORKBENCH_ICON)/g' freecad/workbench_starterkit/init_gui.py
	@# Rename workbench icon
	mv freecad/workbench_starterkit/resources/template_resource.svg freecad/workbench_starterkit/resources/$(WORKBENCH_ICON)
	@# Rename context string for translation of workbench name
	sed -i 's/starterkit/$(WORKBENCH_TRANSLATION_CONTEXT)/g' freecad/workbench_starterkit/init_gui.py
	sed -i 's/starterkit/$(WORKBENCH_TRANSLATION_CONTEXT)/g' freecad/workbench_starterkit/resources/translations/workbench_starterkit_es-ES.ts
	@# Rename workbench directory
	mv freecad/workbench_starterkit freecad/$(WORKBENCH_DIR_NAME)
	@# Update setup.py file
	sed -i 's/looooo/$(MAINTAINER)/g' setup.py
	sed -i 's/sppedflyer@gmail.com/$(EMAIL)/g' setup.py
	sed -i 's|https://github.com/FreeCAD/Workbench-Starterkit|$(URL)|g' setup.py
	sed -i 's/template for a freecad extensions\, installable with pip/$(DESCRIPTION)/g' setup.py
	sed -i "s/\['numpy'\]/$(DEPENDENCIES_LIST)/g" setup.py

self-destruction:
	echo "Remove Makefile"
	rm Makefile
