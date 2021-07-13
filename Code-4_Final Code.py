import math
import numpy as np

# This function test whether the function is ALL or AML

# Like for first example which we have shown below
# For Gene 1, Gene 2, Gene 3
# We have chosen data as 2284, 836, 528
# Which we know is the AML but we will check it using our function if it gives correct output or not
# We know likelihood for each gene from the normal distribution and graphs we have plotted
# For Gene_x(2284) we have likelihood for ALL 0.0001236702223506501 as and AML as 6.754422196150098e-05
# For Gene_x(836) we have likelihood for ALL 6.121893992602794e-05 as and AML as 0.0008327978318480205
# For Gene_x(528) we have likelihood for ALL 0.0002758983645538475 as and AML as 0.0007959980498689425
# Similarly for all three cases we have done the same and we end up with all correct results!

# A posterior is the probability of assigning observations to groups given the data.
# A prior is the probability that an observation will fall into a group before you collect the data.
# we know that the prior for AML is (No. of AML /total) and same for AML

prior_ALL = 47/72
prior_AML = 25/72

def test_All():
    # Posterior_ALL = prior_ALL * likelihood1* likelihood2 * likelihood3
    # Posterior_ALL = p*l1*l2*l3, we calculate the posterior by the formula we have

    # taking log on both side is important because it ensures that the maximum value of the log
    # of the probability occurs at the same point as the original probability function.
    # Therefore we can work with the simpler log-likelihood instead of the original likelihood
    # Also computer can not identify very small value and it considers a very non zero number as zero if done directly,
    # hence log ensure that such calculation error should not occur
    # that's why taking log is necessary if values are very small.


    # CASE1

    x1_ALL = 0.0001236702223506501
    x1_AML = 6.754422196150098e-05

    y1_ALL = 6.121893992602794e-05
    y1_AML = 0.0008327978318480205

    z1_ALL = 0.0002758983645538475
    z1_AML = 0.0007959980498689425

    Posterior_ALL_1 = np.log(prior_ALL) + np.log(x1_ALL) + np.log(y1_ALL) + np.log(z1_ALL)
    Posterior_AML_1 = np.log(prior_AML) + np.log(x1_AML) + np.log(y1_AML) + np.log(z1_AML)

    # Converting posterior of log to power of exponential so that we could identify which is smaller and greater

    Final_post_ALL_1 = math.exp(Posterior_ALL_1)
    Final_post_AML_1 = math.exp(Posterior_AML_1)

    # from earlier we know that output must be AML so the posterior of AML must be greater than that of ALL
    # Hence if true then test passed!

    print(" ")

    if(Final_post_ALL_1 < Final_post_AML_1):
        print("Test PASSED for case1, we desired for AML and got AML!")
    else:
        print("Test FAILED for case1!, we desired for AML and got ALL!")
    # print(Posterior_ALL)
    # print(Posterior_AML)

    # And it worked out posterior of AML is greater, test passed

    print("The Final Posterior of ALL in Case1:", Final_post_ALL_1)
    print("The Final Posterior of AML in Case1:", Final_post_AML_1)

    print(" ")

    # As the example explained above we have performed exactly same step in Case2 also
    # Only data of ALL is chosen for this case, and we want resultant output as ALL

    # CASE2

    x2_ALL = 0.0001316661996689176
    x2_AML = 3.182638784121011e-05

    y2_ALL = 0.00012095596892315033
    y2_AML = 8.911799272192873e-06

    z2_ALL = 0.0004263025451999851
    z2_AML = 5.138832283451263e-09

    Posterior_ALL_2 = np.log(prior_ALL) + np.log(x2_ALL) + np.log(y2_ALL) + np.log(z2_ALL)
    Posterior_AML_2 = np.log(prior_AML) + np.log(x2_AML) + np.log(y2_AML) + np.log(z2_AML)

    Final_post_ALL_2 = math.exp(Posterior_ALL_2)
    Final_post_AML_2 = math.exp(Posterior_AML_2)

    # from earlier we know that output must be AML so the posterior of AML must be greater than that of ALL
    # Hence if true then test passed!

    if (Final_post_ALL_2 > Final_post_AML_2):
        print("Test PASSED for case2!, we desired for ALL and got ALL!")
    else:
        print("Test FAILED for case2! we desired for ALL and got AML!")
    # print(Posterior_ALL)
    # print(Posterior_AML)

    print("The Final Posterior of ALL in Case2:", Final_post_ALL_2)
    print("The Final Posterior of AML in Case2:",Final_post_AML_2)

    print(" ")

    #CASE3
    # Data of AML is chosen for this case, and we want resultant output as AML

    x3_ALL = 8.326706793379737e-05
    x3_AML = 0.0006192919524104828

    y3_ALL = 8.014712527251667e-05
    y3_AML = 0.0006326959552129256

    z3_ALL = 0.00014996693080720745
    z3_AML = 0.0012561944935007604

    Posterior_ALL_3 = np.log(prior_ALL) + np.log(x3_ALL) + np.log(y3_ALL) + np.log(z3_ALL)
    Posterior_AML_3 = np.log(prior_AML) + np.log(x3_AML) + np.log(y3_AML) + np.log(z3_AML)

    Final_post_ALL_3 = math.exp(Posterior_ALL_3)
    Final_post_AML_3 = math.exp(Posterior_AML_3)

    # from earlier we know that output must be AML so the posterior of AML must be greater than that of ALL
    # Hence if true then test passed!

    if (Final_post_ALL_3 < Final_post_AML_3):
        print("Test PASSED for case3!, we desired for AML and got AML!")
    else:
        print("Test FAILED for case3! we desired for AML and got ALL!")

    print("The Final Posterior of ALL in Case3:", Final_post_ALL_3)
    print("The Final Posterior of AML in Case3:", Final_post_AML_3)

    #we reached the end where we got the all the three cases passed!

test_All()

