import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pdb


# 1) Plot the relationship between age and wing length
age = [3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17]
wingLength = [1.4, 1.5, 2.2, 2.4, 3.1, 3.2, 3.2, 3.9, 4.1, 4.7, 4.5, 5.2, 5]

fig, ax = plt.subplots()
plt.scatter(age,wingLength)
plt.xlabel('Age')
plt.ylabel('Wing Length')
plt.title('Age vs Wing Length')

# 2) calculate and plot the regression line
regress = stats.linregress(age,wingLength)


slope = regress[0]
intercept = regress[1]
rval = regress[2]
pval = regress[3]
stderr = regress[4] #stderror of slope

# pdb.set_trace()

ax.axline((0, intercept), slope=slope)
print('Slope of regression line is ' + str(slope))
print('Intercept of regression line is ' + str(intercept))


#manually is as follows according to answers:
# Computing regession line predicted_wing_length = a + b * age.
# n=len(age) # alternatively, you can calculate n=len(wing_length)
# SumX=np.sum(age) # sum up all X values
# MeanX=np.mean(age) # find the mean X value
# SumX2=np.sum(np.square(age))  # the sum of each X squared
# Sumx2=SumX2-np.square(SumX)/n  # the sum of the square of the difference between (each X and mean X);

# SumY=np.sum(wing_length) #sum up all Y values
# MeanY=np.mean(wing_length) # find the mean Y value
# SumXY=np.inner(age, wing_length) # the sum of the product of each X and Y values
# Sumxy=SumXY-SumX*SumY/n # the sum of the product of the difference between each X value minus the
# SumY2=np.sum(np.square(wing_length)) # the sum of each Y squared

# pdb.set_trace()

# 3) can you reject H0: b = 0
print('r value of regression line is ' + str(rval))
print('with p val of ' + str(pval))
print('You can reject null hypothesis that slope is 0')

# 4) calculate and plot CIs on the slope of the regression --> Might be funky, double check
upperSlopeCI = slope+stderr
upperInterceptCI = intercept + regress.intercept_stderr
lowerSlopeCI = slope-stderr
lowerInterceptCI = intercept - regress.intercept_stderr

ax.axline((0, upperInterceptCI), slope=upperSlopeCI, ls='--', color='k')
ax.axline((0, lowerInterceptCI), slope=lowerSlopeCI, ls='--', color='k')

# 5) Calculate r**2
rSquared = rval**2
print('r squared is ' + str(rSquared))

# 6) Calculate pearson's r
pearsonR = np.corrcoef(age, wingLength)
print('Pearsons r is ' + str(pearsonR[0][1]))




































