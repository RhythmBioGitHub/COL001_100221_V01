#CONFIDENTIALITY NOTE: The information contained, including attachments, is intended only for the person(s) or entity to which it is addressed and may contain confidential and/or privileged material. Any review, retransmission, dissemination or other use of, or taking of any action in reliance upon this information by persons or entities other than the intended recipient is prohibited. Although we use virus scanning software, we deny all liability for viruses or alike in any message or attachment. If you received this in error, please contact the sender and destroy any copies of this information.

#This InputAPI merely takes in information from an external source - 3rd Party Consuming software ("Our wrapper") - and then passes it to the algorithm. The algorithm then sends it back.
#This may end up being a function within a function. Input API function.

#Note that if a value is read that is greater than the maximum or 'ADL' then it will be set to the chosen maximum (shown here in errors)


import pandas as pd

from Algorithm_v01100221 import riskcalculator

#Here we read the output from the plate reader (this may take any form)
Biometrics = pd.read_excel('TestInput_Biomarkers.xlsx')
for i in range(Biometrics.shape[0]):

    #Here we assign the values to the required parameters
    id = Biometrics.columns[0]
    age = Biometrics.columns[1]
    gender = Biometrics.columns[2]
    bm1 = Biometrics.columns[3] #PKM2
    bm2 = Biometrics.columns[4] #BDNF
    bm3 = Biometrics.columns[5] #DKK3
    bm4 = Biometrics.columns[6] #IGFBP2
    bm5 = Biometrics.columns[7] #TIMP1

    #Converting gender into integer equivalent
    if(gender == 'Male'):
        gender = 1.1
    elif (gender == 'Female'):
        gender = 1.0
    else:
        ...

    #As defined in the ICD, these two flags are preset.
    err = 1;
    noerr = 0;

    #Here we set up a looping mechanism to work through the possible errors. If an error is flagged, the loop and therefore software exits
    go = True;
    while go:
        #define first what patient information pertains to - no date of birth, no initials, no surnames etc. completely random.
        if(len(id) > 15) or (len(id) < 15):
            print("Error ST 02.1: Incorrect number of digits in sample ID format");
            go = False;
            break;
        elif id.isalnum() == False:
            print("Error ST 02.3,4: Check sample ID format");
            go = False;
            break;
        elif(gender != 1.0 and gender != 1.1):
            print("Error ST 02.5: Sample gender error");
            go = False;
            break;
        elif(age < 15 or age > 115):
            print("Error ST 02.6: Check age format");
            go = False;
            break;
        elif(isinstance(age,int)==False):
            print("Error ST 02.7: Check age format");
            go = False;
            break;
        #Here ranges for biomarkers need to be set. Values outside of this range will need to be checked, maybe biomarker order problem?
        elif(bm1 > 1082 or bm1 < 104 or isinstance(bm1,float)==False):
            print("Error ST 02.8, 13: Check bm1 reading");
            go = False;
            break;
        elif (bm2 > 16 or bm2 < 2 or isinstance(bm2,float)==False):
            print("Error ST 02.9, 13: Check bm2 reading");
            go = False;
            break;
        elif (bm3 > 53 or bm3 < 9 or isinstance(bm3,float)==False):
            print("Error ST 02.10, 13: Check bm3 reading");
            go = False;
            break;
        elif (bm4 > 1254 or bm4 < 102 or isinstance(bm4,float)==False):
            print("Error ST 02.11, 13: Check bm4 reading");
            go = False;
            break;
        elif (bm5 > 906 or bm5 < 211 or isinstance(bm5,float)==False):
            print("Error ST 02.12, 13: Check bm5 reading");
            go = False;
            break;

        else:
            ...
        break

    if go == False:
        print("Fail");
    else:
        err = 0;
        noerr = 1;
        print("we are go for liftoff!");

        # Is this going to be the variables or an array christian? What would be the benefit of an array? Must change ICD if you are not going to end up using an array. Arrays are usually for large sets of data.
        risk = riskcalculator(gender, age, bm1, bm2, bm3, bm4, bm5)

        #Output errors
        #If not integer
        #If not 3, 2 or 1
        #If likelihood is outside of range
        #If test performance indicator is outside of range -- maybe send specificity/sensitivity of result?


        if risk == 3:
            print("High");
        elif risk == 2:
            print("Inconclusive");
        else:
            print("Low");

    ### IF ALL TESTS SUCCEED THEN SEND "noerr" integer out. If a single test fails - send "err" integer flag.

