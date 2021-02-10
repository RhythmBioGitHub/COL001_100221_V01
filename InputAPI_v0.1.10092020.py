#CONFIDENTIALITY NOTE: The information contained, including attachments, is intended only for the person(s) or entity to which it is addressed and may contain confidential and/or privileged material. Any review, retransmission, dissemination or other use of, or taking of any action in reliance upon this information by persons or entities other than the intended recipient is prohibited. Although we use virus scanning software, we deny all liability for viruses or alike in any message or attachment. If you received this in error, please contact the sender and destroy any copies of this information.

#This InputAPI merely takes in information from an external source - 3rd Party Consuming software ("Our wrapper") - and then passes it to the algorithm. The algorithm then sends it back.
#This may end up being a function within a function. Input API function.

import pandas as pd

from Algorithm_v0110092020 import riskcalculator

#Here we read the output from the plate reader (this may take any form)
Biometrics = pd.read_excel('TestInput_Biomarkers.xlsx')

#Here we assign the values to the required parameters
id = Biometrics.columns[0]
age = Biometrics.columns[1]
gender = Biometrics.columns[2]
bm1 = Biometrics.columns[3] #PKM2
bm2 = Biometrics.columns[4] #BDNF
bm3 = Biometrics.columns[5] #DKK3
bm4 = Biometrics.columns[6] #IGFBP2
bm5 = Biometrics.columns[7] #TIMP1

if(gender == 'Male'):
    gender = 1.1
elif (gender == 'Female'):
    gender = 1.0
else:
    ...


#Here we check the data integrity - ALL ERROR MESSAGES FROM Verification Test Spreadsheet ('COL001_XXXX ....)
if(isinstance(age,int)):
    print('it is an integer')
else:
    print("wrong")

if(age > 115) or (age < 15):
    print("Unnaceptable")

    #...



### IF ALL TESTS SUCCEED THEN SEND "noerr" integer out. If a single test fails - send "err" integer flag.

risk = riskcalculator(gender, age, bm1, bm2, bm3, bm4, bm5)

if risk == 3:
    print("High");
elif risk == 2:
    print("Inconclusive");
else:
    print("Low");

