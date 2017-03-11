# PyDCC

This is a set of Python tools for automating tasks on Docushare.

The [Python Procedure Manual](https://docushare.tmt.org/docushare/dsweb/Get/Document-50424/Python%20Docushare%20Procedure_REL02%20FINAL.pdf) 
is on TMT Docushare. This document describes how to install and use the procedures.

# Upgrading from previous GitHub repository
For users converting from using the previous GitHub projects, the following steps will 
be needed to use this new repository.

## Config Files
* Copy pyDCC/Config/Config_example.py to Config.py
* Edit Config.py per the instructions in the file
* If you are migrating to the PyDCC project you will have to copy over and edit your 
Config.py file for the location of: 
    - tracetreefilepath
    - dccfilepath
    - reportfilepath

## Secrets file
* Copy PyDCC/Secrets/secrets_example.py to secrets.py
* Edit secrets.py per the instructions in the file
* If you are migrating to the PyDCC project should be able to just copy over your existing 
secrets.py file (if you had one)


## PYTHONPATH
* Set the PYTHONPATH to point to the PyDCC/Config, PyDCC/Secrets, and PyDCC/Library directories.  
See the Python Procedure Manual (link above) for details of how to do this.