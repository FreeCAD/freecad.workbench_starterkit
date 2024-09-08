set(Namespace_SRCS
        freecad/{{cookiecutter.workbench_module_name}}/init_gui.py
        freecad/{{cookiecutter.workbench_module_name}}/__init__.py
        freecad/{{cookiecutter.workbench_module_name}}/my_numpy_function.py
        freecad/{{cookiecutter.workbench_module_name}}/translate_utils.py
        freecad/{{cookiecutter.workbench_module_name}}/version.py
        freecad/{{cookiecutter.workbench_module_name}}/resources/cool.svg
        freecad/{{cookiecutter.workbench_module_name}}/resources/translations/{{cookiecutter.workbench_module_name}}_es-ES.qm
        freecad/{{cookiecutter.workbench_module_name}}/resources/translations/{{cookiecutter.workbench_module_name}}_es-ES.ts
)

SOURCE_GROUP("" FILES ${Namespace_SRCS})

ADD_CUSTOM_TARGET({{cookiecutter.workbench_project_name_uppercase}} ALL
        SOURCES ${Namespace_SRCS}
)

fc_copy_sources({{cookiecutter.workbench_project_name_uppercase}} "${CMAKE_BINARY_DIR}/Mod/{{cookiecutter.workbench_project_name}}" ${Namespace_SRCS})

INSTALL(
    FILES
        ${Namespace_SRCS}
    DESTINATION
        Mod/{{cookiecutter.workbench_project_name}}
)
