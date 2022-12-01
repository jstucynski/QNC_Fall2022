import scipy.stats as stats
import numpy as np
import pdb

# the statsmodels package has a built in function that allows us to use multiple methods for FDR correction
import statsmodels.stats.multitest as smt


# In this exercise we will run through an example of correcting for multiple comparisons with both the Benjamini-Hochberg procedure 
# and the more conservative Bonferroni correction.

# First, simulate multiple (say, 1000) t-tests comparing two samples with equal means and standard deviations,
# and save the p-values. Obviously, at p<0.05 we expect that ~5% of the simulations to yield a "statistically significant" result
# (of rejecting the NULL hypothesis that the samples come from distributions with equal means).

# Second, once you have the simulated p-values, apply both methods to address the multiple comparisons problem.

# Third, set the sample 1 and sample 2 means to be 1 and 2 respectively, and re-run the exercise. What do you notice? What if you make the difference between means even greater?



# problem 1
#set up some normal distributions

numTests = 1000

mean1 = 1
std1 = 2
numSamples1 = 100

mean2 = 1
std2 = 2
numSamples2 = 100

pValues = []
for i in range(numTests):
    normal1 = np.random.normal(mean1,std1,numSamples1)
    normal2 = np.random.normal(mean1,std1,numSamples1)
      
    pValue = stats.ttest_ind(normal1,normal2)
    pValues.append(pValue[1])
    
#now determine how many are significant
numSignificant = 0
for p in pValues:
    if p < 0.05:
        numSignificant +=1
        
print('Problem 1: Finding false positives when doing many ttests')
print('Out of ' + str(numTests) + ' ttests from normal distributions with identical means and stds, found ' + str(numSignificant) + ' tests < 0.05')  


# Problem 2: Utilize bonferroni + Benjamini Hochberg mutliple comparison corrections
# Bonferroni
numSignificantBonf = 0
bonfAlpha = 0.05 / numTests
bonfAlpha = smt.multipletests(pValues, alpha = 0.05, method = 'bonferroni')[2] # perform B&H procedure
# pdb.set_trace()
for p in pValues:
    if p < bonfAlpha:
        numSignificantBonf += 1
print('Problem 2: Bonferroni correction')
print('Out of ' + str(numTests) + ' ttests after Bonferroni correction, found ' + str(numSignificantBonf) + ' tests < ' + str(bonfAlpha))

#Benjamini Hochberg
# order p values in ascending order
pValuesAscending = np.sort(pValues)
#Calculate critical value (i/n)/Q where i is rank, n is numTests, Q is false discovery rate 0.05
criticalVals = []
for rank,pVal in enumerate(pValuesAscending):
    # pdb.set_trace()
    rank+=1
    criticalVal = (rank/numTests) * 0.05
    criticalVals.append(criticalVal)

# pdb.set_trace()
# find smallest pValue that is smaller than it's critical val
for i in range(len(criticalVals)):
    # pdb.set_trace()
    if pValuesAscending[i] < criticalVals[i]:
        BHCorrectedAlpha = pValuesAscending[i]
        
# pdb.set_trace()
    
BHCorrectedAlpha = smt.multipletests(pValues, alpha = 0.05, method = 'fdr_bh')[2] # perform bonferroni
# pdb.set_trace()
#now determine number of pvals less than this new corrected pval
numBHSignificant = 0
for p in pValues:
    if p < BHCorrectedAlpha:
        numBHSignificant +=1
print('Problem 2: Benjamini-Hochberg correction')
print('Out of ' + str(numTests) + ' ttests after BH correction, found ' + str(numBHSignificant) + ' tests < ' + str(BHCorrectedAlpha))    
    
    
# Problem 3: Do the same thing but this time set the means of the 2 distributions to be different.
numTests = 1000

mean1 = 1
std1 = 2
numSamples1 = 100

mean2 = 2
std2 = 2
numSamples2 = 100

pValues = []
for i in range(numTests):
    normal1 = np.random.normal(mean1,std1,numSamples1)
    normal2 = np.random.normal(mean1,std1,numSamples1)
      
    pValue = stats.ttest_ind(normal1,normal2)
    pValues.append(pValue[1])
    
#now determine how many are significant
numSignificant = 0
for p in pValues:
    if p < 0.05:
        numSignificant +=1
print('\n')
print('Problem 3: Finding false positives when doing many ttests')
print('Out of ' + str(numTests) + ' ttests from normal distributions with different means but same stds, found ' + str(numSignificant) + ' tests < 0.05')  


# Problem 2: Utilize bonferroni + Benjamini Hochberg mutliple comparison corrections
# Bonferroni
numSignificantBonf = 0
bonfAlpha = 0.05 / numTests
for p in pValues:
    if p < bonfAlpha:
        numSignificantBonf += 1
print('Problem 3: Bonferroni correction')
print('Out of ' + str(numTests) + ' ttests after Bonferroni correction, found ' + str(numSignificantBonf) + ' tests < ' + str(bonfAlpha))

#Benjamini Hochberg
# order p values in ascending order
pValuesAscending = np.sort(pValues)
#Calculate critical value (i/n)/Q where i is rank, n is numTests, Q is false discovery rate 0.05
criticalVals = []
for rank,pVal in enumerate(pValuesAscending):
    criticalVal = (rank/numTests) * 0.05
    criticalVals.append(criticalVal)
    
# find smallest pValue that is smaller than it's critical val
for pVal,criticalVal in zip(pValuesAscending,criticalVals):
    if pVal < criticalVal:
        BHCorrectedAlpha = pVal
        break
    

BHCorrectedAlpha = smt.multipletests(pValues, alpha = 0.05, method = 'fdr_bh')[2] # perform bonferroni
#now determine number of pvals less than this new corrected pval
numBHSignificant = 0
for p in pValues:
    if p < BHCorrectedAlpha:
        numBHSignificant +=1
print('Problem 3: Benjamini-Hochberg correction')
print('Out of ' + str(numTests) + ' ttests after BH correction, found ' + str(numBHSignificant) + ' tests < ' + str(BHCorrectedAlpha)) 
    
    

print('\n')
print('For whatever reason I cant get the stupid Benjamini Hochberg correction to work, Im not sure why, and I spent way too much time on this')
print('but i understand that the point of this exercise is that the BH correction is less strict than the bonferroni correction.')

        








































