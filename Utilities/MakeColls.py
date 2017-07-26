#!/usr/bin/env python3

# This Python script was created to make collections in DocuShare, without the need to log into the actual
# DocuShare website.  This will allow the user a quicker method in which they can create collections.
# This script also allows the user to create a collection with a unique number as well name the collection appropriately.




# my modules
import Config as cf
import DCC




data_package = [['DP01.1 (__NAME). Level 2 Requirements',[]],
    ['DP01.2 (__NAME). Level 3 Requirements',[]],
    ['DP01.3 (__NAME). Specifications',[]],
    ['DP02.1 (__NAME). Interfaces',[]],
    ['DP03.1 (__NAME). Design Description (System, Hardware)',[]],
    ['DP03.2 (__NAME). Design Description (Software)',[]],
    ['DP04.1 (__NAME). Detailed Design (System/Hardware)',[]],
    ['DP04.2 (__NAME). Detailed Design (Software)',[]],
    ['DP04.3 (__NAME). Prototype Development',[]],
    ['DP05.1 (__NAME). CAD Models/Model Description',[]],
    ['DP05.2 (__NAME). Control Models/Model Description',[]],
    ['DP05.3 (__NAME). Design, Analysis, and Performance Reports',[]],
    ['DP06.1 (__NAME). Supplier ES&H Plan',[]],
    ['DP06.2 (__NAME). Hazard Risk Assessment',[]],
    ['DP07.1 (__NAME). FMEA',[]],
    ['DP07.2 (__NAME). Reliability Prediction Report',[]],
    ['DP08.1 (__NAME). Manufacturing Plan',[]],
    ['DP08.2 (__NAME). Assembly and Integration Plan',[]],
    ['DP09.1 (__NAME). Verification Plan',[]],
    ['DP09.2 (__NAME). Acceptance Test Procedures',[]],
    ['DP09.3 (__NAME). Compliance Matrix',[]],
    ['DP09.4 (__NAME). Verification Cross Reference Matrix',[]],
    ['DP09.5 (__NAME). Verification Procedures/Reports',[]],
    ['DP10.1 (__NAME). Operations/Maintenance Plan',[]],
    ['DP10.2 (__NAME). Shipping and Packaging Plan',[]],
    ['DP10.3 (__NAME). SOPS/Maintenance Procedures',[]],
    ['DP10.4 (__NAME). Spare List',[]],
    ['DP10.5 (__NAME). User Guides, Manuals, Handbooks',[]],
    ['DP11.1 (__NAME). Configuration Index Document',[]],
    ['DP12.1 (__NAME). Supplier QA Plan',[]],
    ['DP12.2 (__NAME). End Item Data Package',[]],
    ['DP13.1 (__NAME). Project Management Plan',[]],
    ['DP13.2 (__NAME). Schedule',[]],
    ['DP13.3 (__NAME). Cost Estimate',[]],
    ['DP13.4 (__NAME). Risk Register',[]]]

top_level = [['01 __NAME_Information and Logistics',[]],
    ['02 __NAME Data Package',data_package],
    ['03 __NAME Supporting Documents',[]],	
    ['04 __NAME Presentations',[]],
    ['05 __NAME Review Comments',[]],
    ['06 __NAME Review Board Report',[]],
    ['07 __NAME Response to Review Board Report',[]]]
    
    
cid_set = [['00. (__NAME) Configuration Index Document',[]],
    ['01. (__NAME) Requirements',[]],
    ['02. (__NAME) Interfaces',[]],
    ['03. (__NAME) Design Description',[]],
    ['04. (__NAME) Detailed Design',[]],
    ['05. (__NAME) Design Analysis and Modeling - MODELS',[]],
    ['06. (__NAME) Design Analysis and Modeling - REPORTS',[]],
    ['07. (__NAME) Safety',[]],
    ['08. (__NAME) Reliability',[]],
    ['09. (__NAME) Manufacturing',[]],
    ['10. (__NAME) Assembly and Integration',[]],
    ['11. (__NAME) Operations and Maintenance',[]],
    ['12. (__NAME) Verification',[]],
    ['13. (__NAME) Quality',[]],
    ['14. (__NAME) Management',[]]]
    
    
sub_test_set = [['__NAMEtest coll 3',[]]]

test_set = [['__NAMEtest coll 1',[]],
        ['__NAMEtest coll 2',sub_test_set]
        ]
# This function creates review collections using a top-level collection number, a name for the new collection to be made, 
# as well as user ID to create collections. the User will be set to the owner of the top level collection selected.
def createReviewColls(s,handleParent, collNames, revName, userName): 
    for collName,subColl in collNames:
        collName = collName.replace('__NAME',revName)
        print('Creating:',handleParent,'->',collName)
        handleChild = DCC.make_collection(s, handleParent, collName, '', Usrdata = userName)
        if len(subColl) > 0:
            createReviewColls(s, handleChild, subColl, revName, userName)

def reviewColls():
    
    #variable set to determine what will be created when making collections for reviews
    
    ans = ''
    while (True):
        print('Create Collections for Design Review (enter D) or CID (enter C)?',end="")
        ans = input()
        if ans.upper() == 'D':
            set = top_level
            print('Will create collections for Design Review')
            break
        elif ans.upper() == 'C':
            print('Will create collections for CID')
            set = cid_set
            break
        else:
            Print("Enter 'D' or 'C'")
            

    #creates sets that define the user choice to cover miscellaneous cases
    prod = ['prod', 'production', 'p', ' ']
    tes = ['test', 'tes', 't']
    checker = False
    print("Would you like to log into the production site or the test site?")
    print("Valid Inputs are as follows: Production, prod, p, test, t :", end="")
    print("*** Input is not case sensitive ***")
    print(" ")
    choice = input().lower()
    #while loop to continue asking the user for input until a correct input has been entered
    while (checker == False):
        #Production site login choice
        if(choice in prod):
            print("You are now logging into the Production version of DocuShare")
            s = DCC.login(Site ='Production')
            checker = True
        #test site login choice
        elif(choice in tes):
            print("You are now logging into the test VM DocuShare")
            s = DCC.login(Site ='Test')
            checker = True
            #cf.dcc_url + cf.dcc_login 
        #error message alerting user to enter a valid choice
        else:
            print("Please enter a valid choice, (P)roduction or (T)est")
            print("*** Input is not case sensitive ***")
            print(" ")
            choice = input().lower()
    yes = ['yes', 'y', 'ye']
    #creates a new boolean variable to allow user to break from loop
    checker1 = False
    print("Please enter a collection number that you would like to create a sub-collection under")
    #checker1 only true when user enters correct information 
    while(checker1 == False):
        #takes user input and stores into variable col which is the collection number that will
        #be used when creating the review collection
        col = input()
        parent = 'Collection-' + col
        #uses function prop_get to display collection information
        fd = DCC.prop_get(s, parent , InfoSet = 'CollData', Print = True)
        print("Please enter the Subsystem or Design Review Name to associate with this new collection (Example 'CID IRIS' or 'STR FDRP3':")
#         print("*** Specific input is case sensitive ***")
#         print(" ")
        name = input()
        # double checks user to make sure that they would like to create this collection
        print("*** Input is not case sensitive ***")
        print("Are you sure that you want to create: " + name + " under " + parent)
        print("Valid Inputs are as follows: Yes, Y, No, N:")
        ans = input().lower()
        # checks that user input is correct, if the answer is a valid form of yes
        # then the collection will be made and the user will break from the loop
        if(ans in yes):
            print("You are now making a collection named: " + name + " under " + parent )
            checker1 = True
            createReviewColls(s, parent, set, name, fd['owner-userid'])
        else:
            print("Please re-enter a Collection number followed by a Collection name")



if __name__ == '__main__':
    print("Running module test code for",__file__)
    reviewColls()
    
