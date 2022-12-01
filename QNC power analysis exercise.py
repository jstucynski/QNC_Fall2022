import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.stats.power import TTestIndPower
import pdb

#NOTES:
    
#power = probability that study will not produce a type 2 error  (false negative) / obtain a true positive, 1-Beta
#based on:
# 1) effect size
# 2) sample size
# 3) significance level
# 4) power you wish to obtain, ie probability of a true positive. Usually accepted at 80%

#   The key point is that a 
#   power analysis describes a relationship between the effect size and the 
#   power -- so we can define a particular power to compute the effect size.

# To show that this is the case, let's try a bunch of sems and find the 
#   value that corresponds to when 80% of the effect distribution is >= the 
#   p=0.05 cutoff for the null distribution



# EXERCISE:
#Do a post-hoc power analysis to determine the number of data samples (partial spearman's correlation coefficients between pupil diameter and LC spike rate)
# needed to achieve 80% power for a series of possible effect sizes.

#Steps:
# Obtain a null distribution of these partial spearman's correlation coefficients between pupil diameter and LC spike rate in each trial
# Do this by computing correlation coefficients on simulated data
# There are 2 simulated datasets: 1 is Poisson spike data to stand in for LC, 2 is Gaussian pupil diameter distribution


#Then plot n number of corellation coefficients needed for 80% power as a function of effect sizes
# ie n for 80% power on yaxis, effect sizes based on mean correlation on xaxis


### CODE ###
numTrials = 200
numExperiments = 1000
# Simulate Poisson spike data for LC
mu = 2
spikeLC = stats.poisson.rvs(mu, size=(numTrials, numExperiments)) #rvs is random variates metod of poisson
# Simulate gaussian distribution of pupil diameter
mean = 0
std = 1
pupilDilation = np.random.normal(mean,std,(numTrials,numExperiments))

# Get all of the correlations
correlations = np.zeros(numExperiments)
for i in np.arange(numExperiments):
    correlations[i], _ = stats.spearmanr(spikeLC[:,i], pupilDilation[:,i])

#plot null distribtution of correlations
plt.hist(correlations, bins=50)
plt.xlabel('Correlation coefficients')
plt.ylabel('Count')

# Now calculate effect sizes
# effect size is calculated by dividing the difference between the means of 2 distributions divided by their standard deviation
# in the case of null distribution, it has same standard deviation as real distribution but with mean centered at 0
# so formula will be (mean - 0)/std
# and in order to generate a list of effect sizes, we'll vary the mean of our hypothetical experimental distribution and compare it against the null mean 0 distribution
# so we can do this in steps of our hypothetical mean from 0 to the max of the null distribution

# eg.
minMean = .01 #cannot be 0 because there cannot be an effect size of 0
maxMean = 0.2
effectSizes = np.arange(minMean, maxMean, 0.01)/np.std(correlations)

#Now we want to know for each effect size, what our N has to be to get a power of 80%.
power = .8
Ns = []
for effectSize in effectSizes:
    obj = TTestIndPower()
    N = obj.solve_power(effect_size=effectSize, alpha=.05, power=power)
    Ns.append(N)
    
    
plt.figure()
plt.plot(effectSizes,Ns)
