PyDCC
=====
This is a set of Python tools for automating tasks on Docushare.

Upgrading from previous GitHub repository
-----------------------------------------
For users converting from using the previous GitHub projects, the following steps will 
be needed to use this new repository.

* Config Files
** Copy pyDCC/Config/Config_example.py to Config.py
** Edit Config.py per the instructions in the file
** If you are migrating to the PyDCC project you will have to edit your Config.py file for the location of 
- tracetreefilepath
- dccfilepath
- reportfilepath

* Copy pyDCC/Secrets/Secrets_example.py to Secrets.py
** Edit Secrets.py per the instructions in the file

* Set the PYTHONPATH to point to the PyDCC/Config, PyDCC/Secrets, and PyDCC/Library directories