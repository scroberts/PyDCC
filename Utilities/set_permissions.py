#!/usr/bin/env python3

# external modules

# my modules
import DCC
import Config as CF
import Tree
import FileSys
import PERM_DEFS as PD
import Match
import PERM
import MyUtil


def main():
    # Login to DCC
    s = DCC.login(CF.dcc_url + CF.dcc_login) 
    
    #****** SET Flag for asking about changes ******
    ask_flag = MyUtil.get_yn('Ask about changes to files ***  BE CAREFUL !!! *** (Y/N)? ')
    print()
        
    #****** Choose SET ******
    
    ### Safe to run without checking ###
    set = PD.SET_REMOVE_WFOS_IRIS_MANAGERS
  
    ### Don't Run without checking ###
#     set = PD.SET_SE_READERSHIP    


    ### Identify the top level collection
    Published = 'Collection-8277'
    
    Test = 'Document-27819'
    
    handle = Published
    
    #******!!!  Run !!! ******
    tr = Tree.return_tree(s, handle, 'Tree_' + handle)
    handles = Tree.get_flat_tree(tr)
    PERM.check_perms(s, set, handles, Ask = ask_flag)

if __name__ == '__main__':
    print("Running permissions for ",__file__)
    
    main()