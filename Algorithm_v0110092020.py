#CONFIDENTIALITY NOTE: The information contained, including attachments, is intended only for the person(s) or entity to which it is addressed and may contain confidential and/or privileged material. Any review, retransmission, dissemination or other use of, or taking of any action in reliance upon this information by persons or entities other than the intended recipient is prohibited. Although we use virus scanning software, we deny all liability for viruses or alike in any message or attachment. If you received this in error, please contact the sender and destroy any copies of this information.
#This algorithm takes in the final accepted values from the API and returns a score.

import math

agecoeff = -0.014491068
gendercoeff = 1.812284806
pkm2coeff = 2.0
igfpb2coeff = 0.5
bdnfcoeff = 1.812284806
timp1coeff = 0.5
dkk3coeff = 0.5
threshold1 = 1.5
threshold2 = 3.5
threshold3 = 1.5

#This function calculates the risk score based on the coefficients chosen
def riskcalculator(gender, age, bm1, bm2, bm3, bm4, bm5):
    risk = gendercoeff*gender + agecoeff*(age) + dkk3coeff*math.log10(bm3) + bdnfcoeff*math.log10(bm2) + pkm2coeff*math.log10(bm1) + igfpb2coeff*math.log10(bm4) + timp1coeff*math.log10(bm5);

#We need to figure out what a table of comparison means. Different thresholds or values surrounding the threshold?
    if (risk > threshold2):
        risk = 3; #HIGH
    elif ((threshold2 - 0.5) < risk < (threshold2 + 0.5)):
        risk = 2; #Inconclusive
    else:
        risk = 1; #LOW

    return risk;

#additional information can be requested - including test performance indicator and likelihood (percentage/numeric)



