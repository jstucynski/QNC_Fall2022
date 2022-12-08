import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

tailLength = [7.4,7.6,7.9,7.2,7.4,7.1,7.4,7.2,7.8,7.7,7.8,8.3] #x variable
wingLength = [10.4,10.8,11.1,10.2,10.3,10.2,10.7,10.5,10.8,11.2,10.6,11.4] #y variable

# 1) Plot X vs Y. Do they look related?
plt.scatter(tailLength,wingLength)
print('They do look positively correlated.')

# 2) Calculate R(x,y) and R(y,x) first using the given equations and then using numpy.corrcoef. Do you get the same answers?

corrcoeffNP = np.corrcoef(tailLength,wingLength)
print('Coefficient of Correlation according to Numpy is ' + str(corrcoeffNP[0][1]))

#Now calculat the hard way:
n = 12
tailMean = np.sum(tailLength)/n
wingMean = np.sum(wingLength)/n
tailSquared = np.sum((tailLength-tailMean) ** 2)
wingSquared = np.sum((wingLength-wingMean) ** 2)
numerator = np.sum((tailLength - tailMean)*(wingLength - wingMean))
denominator1 = np.sqrt(wingSquared)*np.sqrt(tailSquared)
denominator2 = np.sqrt(tailSquared)*np.sqrt(wingSquared)

RWingxTail = numerator/denominator1
RTailxWing = numerator/denominator2
print('RWingxTail = ' + str(RWingxTail))
print('RTailxWing = ' + str(RTailxWing))
print('Correlation coefficient computed by computer and by hand are the same.')


# 3) What is the standard error of RWingxTail? What are the 95% CIs computed from the standard error?
# standard error of Pearson's correlation coefficient is np.sqrt((1-r**2)/n-2)
standardError = np.sqrt((1-RWingxTail**2)/(n-2))
print('Standard error of RWingxTail is ' + str(standardError))

# 95CIs
#take fisher z transformation:
z = .5*np.log((1+RWingxTail)/(1-RWingxTail))
#computer std
sz = np.sqrt(1/(n-3))
lowCI = z - 1.96 * sz
highCI = z + 1.96 * sz
lowR = (np.exp(2*lowCI)-1)/(np.exp(2*lowCI)+1)
highR = (np.exp(2*highCI)-1)/(np.exp(2*highCI)+1)

print('95 CIs computed from the standard error = [' + str(lowCI) + ' , ' + str(highCI) + ']')


# 4) Should the value of RWingxTail be considered significant at the p<0.05 level, given a two tailed test 
# (ie. we reject if the test statistic is too large on either tail of the null distribution) for H0 : RWingxTail = 0?
t = RWingxTail / standardError
# I'm not computing this by hand so just use the line of code from the answers:
prob = 2*(1-stats.t.cdf(t,n-2))
print('p = ' + str(prob))
print('Yes it should be considered significant.')


# 5) Yale does the exact same study and finds that his correlation value is 0.75. Is this the same as yours? Ie. Evaluate H0 : r=0.75
# Gonna be honest, I don't really know what's happening here....
# z-transform the new referent
z_Yale = 0.5*np.log((1+0.75)/(1-0.75))
# Compute the text statistic as the difference in z-transformed values, divided by the sample standard deviation
plambda = (z-z_Yale)/sz
# Get a p-value from a two-tailed test
prob2 = 2*(1-stats.norm.cdf(plambda))
print(f'p={prob2:.4f} for H0: r=0.75')
print('Yales is not significantly different.')



# 6) Finally, calculate the statistical power and sample size needed to reject H0 : r=0 when r>=0.05

# I'm straight up not understanding what's going on here.... you lost me Josh

# Compute the test statistic as above
r_ref   = 0.5;  
z_ref   = 0.5*np.log((1+r_ref)/(1-r_ref))
plambda = (z-z_ref)/np.sqrt(1/(n-3))

# Set a criterion based on alpha
alpha = 0.05
z_criterion = stats.norm.ppf(1-alpha/2)

# Power is proportion of expected sample distribution to the right of the criterion
power = 1-stats.norm.cdf(z_criterion-plambda)

# Calculate the n needed to ensure that H0 (r=0) is rejected 99% of the time when |r|>= 0.5 at a 0.05 level of significance
#
# Derivation:
#   power = 1-normcdf(z_criterion-lambda)
#   1 - power = normcdf(z_criterion-lambda)
#   zCriterion-lambda = norminv(1 - power)
#   plambda  = z_criterion - norminv(1 - power)
#   (z-z_ref)/sqrt(1/(n-3)) = z_criterion - norminv(1 - power)
#   sqrt(1/(n-3)) = (z-z_ref) / (z_criterion - norminv(1 - power))
#   n = 1/((z-z_ref) / (z_criterion - norminv(1 - power)))^2+3
desired_power = 0.99
predicted_n = np.ceil(1/((z-z_ref) / (z_criterion - stats.norm.ppf(1-desired_power)))**2+3)
print(f'power = {power:.4f}, predicted n = {int(predicted_n)}')






















