import numpy as np
import scipy.stats as stats
import pdb


#Compute confidence/credible intervals based on the four methods above 
#for simulated data sampled from a population that is Gaussian distributed 
#with mean=10 and standard deviation=2, for n=5, 10, 20, 40, 80, 160, 1000 at a 95% confidence level


# STEP 1: Get a normal distribution:

mu = 10 #mean of distribution
sigma = 2 #standard deviation
N = [5,10,20,40,80,160,1000]
alpha=0.95 #95 percent confidence interval


for n in N:
    samples = np.random.normal(mu, sigma, n)
    sample_mean = np.mean(samples)
    print('##########')
    print('N = ' + str(n) + ' Mean = ' + str(sample_mean))
    
    #Method 1:
    Z = -stats.norm.ppf((1-alpha)/2) #The method norm.ppf() takes a percentage and returns a standard deviation multiplier for what value that percentage occurs at.
    SEM = sigma/np.sqrt(n) # OR if you didn't know the standard deviation you'd use np.std(samples) instead of sigma
    CI95 = [sample_mean-SEM*Z, sample_mean+SEM*Z] #1.96 is the z
    print('Method 1 Zscore: ' + '95CI = [' + str(CI95[0]) + ' , ' + str(CI95[1]) + ']')

    #Method 2: Use T distribution
    T = -stats.t.ppf((1-alpha)/2, df=n-1)  #use t score instead of z score
    SEM = sigma/np.sqrt(n)
    CI95 = [sample_mean-SEM*T, sample_mean+SEM*T]
    print('Method 2 Tscore: ' + '95CI = [' + str(CI95[0]) + ' , ' + str(CI95[1]) + ']')
    
    #Method 3: Bootstrap
    numBoot = 1000
    bootMeans = []
    for i in range(1000):
        #generate a new sample distribution by randomly picking values with replacement from the samples
        bootSampleMean = np.mean(np.random.choice(samples, size=n))
        bootMeans.append(bootSampleMean) 
    CI95 = [np.percentile(bootMeans, 100*(1-alpha)/2),np.percentile(bootMeans, 100*(alpha+(1-alpha)/2))]
    print('Method 3 Bootstrap: ' + '95CI = [' + str(CI95[0]) + ' , ' + str(CI95[1]) + ']')
    print('\n')
                

    
    
    
    
    
    
    
    
    
    
    
    
    