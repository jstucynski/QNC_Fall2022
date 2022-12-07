import numpy as np
import pingouin as pg
import scipy.stats as stats
import os.path
import re
import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd
from functools import reduce
import sleepy
import pdb

'''
@Author: Joe
Plot unlimited number of conditions using any number of combinations of parameters. Uses pandas to create a dataframe then plots what you want based on the arguments you set.

    DISCLAIMER:: THERE ARE GOING TO BE SOME EDGE CASES OF SETTING COMBINATIONS THAT MIGHT CRASH. LET ME KNOW AND I'LL FIX THEM.

    Step 1: import conditions_stats.py
    Step 2: call in ipython like so:
    conditions_stats.plot(ppath, recFile = 'your_data.txt')

    @PARAMS
        ppath -- full path name of recording location. Path must include both control and experimental recordings
        
        controlRecordings + experimentalRecordings --  OPTIONALLY pass your files in as a list of strings. Can otherwise leave as empty strings.
        
        recordingFile -- OR make a text file and pass that in as a string <MyTextFile.txt>
            --THIS CAN HANDLE ANY NUMBER OF CONDITIONS OR DRUG DOSAGES

        plotLightvsDark -- If you have a recording that spans across the light AND dark period, will compare them if True. For regular recordings (Shorter recordings during only the light phase) set to False.
            --There's a hidden flag in the body of the script called plotLDPhaseTogether. If you enable plotLightvsDark you can also choose to plot all stats for the light phase on one graph, all stats for the dark phase
            on one graph. Alternatively it will each graph will be the Full, Light, Dark all next to each other for the given stat and given brain states.
            
        plotLDPhaseOnSameGraph -- if you're plotting light and dark periods, decide how you want the graph formatted.
                                -- True = for each brain state and statistic, plot all phases next to each other.
                                -- False = plot each brain state next to each other for each phase (eg. 1 graph for REM + NREM + WAKE percents for Light period, same for dark, etc.)
            
        plotPercents, plotFrequencies, plotDurations -- set to True if you want them to be plotted, false if you don't. You can use any combination you want.
        
        plotREM, plotWAKE, plotNREM, plotNREMtoREMTransition -- set to True if you want them to be plotted, false if you don't. You can use any combination you want.
        
        mouseLabels -- Plot individual mouse points over the bars.
        
        singleGraphs -- Everything will be plotted on individual graphs. Very good for simplifying making figures in illustrator
    
    @RETURN --- returns the full pandas data frame. 
    
    @Tips: 
        --I know the arguments can be confusing. But I've dummy proofed them so even if some of the switches are contradicting themselves it will still run.
            eg. It wouldn't make sense when you're plotting only light periods to have both plotLDPhaseOnSameGraph and singleGraphs both true. So it will end up just plotting singleGraphs.
            Stuff of that nature is not an issue.
        --To just get the dataframe to return without plotting anything, just set all of the plotPercents to false. 
        --You can run the script with lists instead of a text file. Just use paste in the optional list and label arguments directly under the main function arguments instead.
'''
def plot(mouseStats_csvToLoad = '', plotLightvsDark = False, plotLDPhaseOnSameGraph = False, mouseLabels = True, singleGraphs = False,
                           plotPercents = True, plotFrequencies = True, plotDurations = True,
                           REM = True, WAKE = True, NREM = True, NREMtoREMTransition = False):
    
    #############################################        
    #### O P T I O N A L   A R G U M E N T S ####
    #############################################
    #Choose start times (in seconds)  -- Used for non-24 hour recordings
    # tstart = 0
    # tend = -1
    # tend = 10800 #first 3 hours
    # tend = 21600 #first 6 hours
    
    tstart = 21600 #first 6 hours of dark period
    # tend = 43200


    # tstart = 43200
    tend = -1
    
    ma_thr = 10
        
    
    # 'Hard code' your control recordings and names. Otherwise will default to condition names in recordingFile 
    controlCondition = 'control' #String name of the control condition. Can name it anything you want. Will show up in the labels.
    controlRecordings=[]
    
    experimentalCondition = 'experimental' #String name of experimental condition.
    experimentalRecordings=[]
          
    
    #If instead of points for labeled mice, you want all of the data points overlayed on the bars.
    if mouseLabels: #This if statement doesn't actually do anything to the code, just make it clear that allMousePoints won't do anything if mouseLabels is not active.
        allMousePoints = False #must be off for bars to work. # When True and not singleGraphs, makes the dots black with no legend
        bars = True
        jitter = False
    
    
    #Choose which Phases to plot in lightVsDark
    if plotLightvsDark:
#        phaseList = ['Light Period','Dark Period'] #Default     
        phaseList = ['Full Recording','Light Period','Dark Period']        
#        phaseList = ['Full Recording','Light Period']        
#        phaseList = ['Full Recording','Dark Period']
#        phaseList = ['Light Period']
#        phaseList = ['Dark Period']

    #Can handle 9 conditions currently. Add more colors if you have more conditions.
    clrs = ['#808080', '#0504aa', '#040273', '#380282', '#0343df', '#1e488f', '#00035b', '#020035', '#040273'] 
    clrs = ['darkgreen','limegreen','darkgoldenrod','goldenrod']
    # clrs = ['darkgoldenrod','gold']
    # clrs = ['darkgreen','darkgoldenrod']
    # clrs = ['limegreen','gold']
#    clrs = ['gray','blue']

    #############################################        
    ########## S C R I P T   S T A R T ##########
    #############################################

    # if recordingFile != '':
    #     controlRecordingsDict, experimentalRecordingsDict = load_dose_recordings(ppath, recordingFile) 
    #     keys = list(controlRecordingsDict.keys()) #get list of keys
    #     if keys[0]  == '':
    #         controlCondition = controlCondition
    #     else:
    #         controlCondition = keys[0] #assume we only have 1 condition marked as control in the text file.
    #     controlRecordings = controlRecordingsDict[keys[0]] #get list of recordings marked as control
    # else:
    #     #in the case where we just pass in lists, there will be only one experimental condition / dose so we can simply make a dictionary out of it.
    #     experimentalRecordingsDict = {experimentalCondition:experimentalRecordings}


    #Get stats list
    statsLabelList = []
    if plotPercents:
        statsLabelList.append('Percent')
    if plotDurations:
        statsLabelList.append('Duration')
    if plotFrequencies:
        statsLabelList.append('Frequency')
        
    #establish switching for plot brainstate flags
    brainStateList = []
    excludedBrainStateList = []
    if REM:
        brainStateList.append('REM')
    else:
        excludedBrainStateList.append('REM')
    if NREM:
        brainStateList.append('NREM')
    else:
        excludedBrainStateList.append('NREM')
    if WAKE:
        brainStateList.append('WAKE')
    else:
        excludedBrainStateList.append('WAKE')
    if NREMtoREMTransition:
        brainStateList.append('NREM to REM \n Transition')
    else:
        excludedBrainStateList.append('NREM to REM \n Transition')
        
    if len(brainStateList) == 0: #Handle case where some dummy forgets to plot a brain state.
        print('######## Select a Brain State to Analyze ########')
        return



    #Labels for data frame
    labels = ['Name','Percent', 'Duration', 'Frequency', 'Brain State', 'Condition', 'LDPhase']        
    mouseStats = pd.DataFrame(columns=labels)    
    
    controlMiceList = []
    experimentalMiceList = []
    
    #green baseline
    # controlRecordings = {'mouse1':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse1 SCORED, baseline per epoch frequency spectrum.csv', #green baseline
    #                       'mouse2':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse2 SCORED, baseline per epoch frequency spectrum.csv',
    #                       'mouse3':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse3 SCORED, baseline per epoch frequency spectrums.csv',
    #                       'mouse4':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse4 SCORED, baseline per epoch frequency spectrums.csv',
    #                       'mouse9':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse9 SCORED per epoch frequency spectrum.csv',
    #                       'mouse10':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse10 SCORED per epoch frequency spectrum.csv',
    #                       'mouse11':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse11 SCORED per epoch frequency spectrum.csv',
    #                       'mouse12':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse12 SCORED per epoch frequency spectrum.csv',
    #                       'mouse19':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse19 SCORED per epoch frequency spectrum.csv',
    #                       'mouse20':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse20 SCORED per epoch frequency spectrum.csv'}
    
    
        # #yellow baseline, excluding mouse 5
    # controlRecordings = {'mouse13':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse13 SCORED per epoch frequency spectrum.csv',
    #                       'mouse14':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse14 SCORED per epoch frequency spectrum.csv',
    #                       'mouse15':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse15 SCORED per epoch frequency spectrum.csv',
    #                       'mouse16':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse16 SCORED per epoch frequency spectrum.csv',
    #                       'mouse17':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse17 SCORED per epoch frequency spectrum.csv',
    #                       'mouse18':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse18 SCORED per epoch frequency spectrum.csv',
    #                       'mouse21':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse21 SCORED per epoch frequency spectrum.csv',
    #                       'mouse22':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse22 SCORED per epoch frequency spectrum.csv',
    #                       'mouse23':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse23 SCORED per epoch frequency spectrum.csv',
    #                       'mouse24':r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse24 SCORED per epoch frequency spectrum.csv'}
    
    #green recovery
    # controlRecordings = {'mouse1':r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse1 SCORED, recovery per epoch frequency spectrum.csv',
    #                       'mouse2':r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse2 SCORED, recovery per epoch frequency spectrum.csv',
    #                       'mouse3':r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse3 SCORED, recovery per epoch frequency spectrum.csv',
    #                       'mouse4':r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse4 SCORED, recovery per epoch frequency spectrum.csv',
    #                       'mouse9':r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse9 SCORED recovery per epoch frequency spectrum.csv',
    #                       'mouse10':r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse10 SCORED recovery per epoch frequency spectrum.csv',
    #                       'mouse11':r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse11 SCORED recovery per epoch frequency spectrum.csv',
    #                       'mouse12':r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse12 SCORED recovery per epoch frequency spectrum.csv',
    #                       'mouse19':r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse19 SCORED recovery per epoch frequency spectrum.csv',
    #                       'mouse20':r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse20 SCORED recovery per epoch frequency spectrum.csv'}
    
    
    #18 hour green baseline
    controlRecordings = {'mouse1':r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 1, 4711, green 18h baseline FFTs.csv', #green baseline
                          'mouse3':r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 3, 4713, green 18h baseline FFTs.csv',
                          'mouse4':r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 4, 4714, green 18h baseline FFTs.csv'}
    
    
    
    if mouseStats_csvToLoad == '': # if we don't pass in a csv to load, rerun the stats
    
        controlCondition = 'green baseline'
        # controlCondition = 'yellow baseline'
        # controlCondition = 'green recovery'
        
        for mouseName,recNameCSV in controlRecordings.items():
            print('Running ' + mouseName + ' ' + controlCondition)
            #Fill dataframe for just the full recordings
            controlPercents, controlDurations, controlFrequencies = sleep_stats(mouseName, recNameCSV, ma_thr = ma_thr, tstart = tstart, tend = tend, pplot=False)    
    
            # pdb.set_trace()
    
            data1 = [[mouseName, controlPercents[0][0], controlDurations[0][0], controlFrequencies[0][0], 'REM', controlCondition, 'Full Recording']]        
            tempDF1 = pd.DataFrame(data1, columns = labels)
            
            data2 = [[mouseName, controlPercents[0][1], controlDurations[0][1], controlFrequencies[0][1], 'WAKE', controlCondition, 'Full Recording']]        
            tempDF2 = pd.DataFrame(data2, columns = labels)
            
            data3 = [[mouseName, controlPercents[0][2], controlDurations[0][2], controlFrequencies[0][2], 'NREM', controlCondition, 'Full Recording']]        
            tempDF3 = pd.DataFrame(data3, columns = labels)
            
            data4 = [[mouseName, controlPercents[0][3], controlDurations[0][3], controlFrequencies[0][3], 'NREM to REM \n Transition', controlCondition, 'Full Recording']]        
            tempDF4 = pd.DataFrame(data4, columns = labels)
     
            mouseStats = mouseStats.append(tempDF1)
            mouseStats = mouseStats.append(tempDF2)
            mouseStats = mouseStats.append(tempDF3)
            mouseStats = mouseStats.append(tempDF4)
            
            if mouseName not in controlMiceList:
                controlMiceList.append(mouseName)
            
        # For comparing stats across conditions on the same graphs
        # experimentalRecordingsDict = {'green recovery':[['mouse1',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse1 SCORED, recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse2',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse2 SCORED, recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse3',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse3 SCORED, recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse4',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse4 SCORED, recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse9',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse9 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse10',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse10 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse11',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse11 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse12',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse12 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse19',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse19 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse20',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse20 SCORED recovery per epoch frequency spectrum.csv']],
                                      
        #                               'yellow baseline':[['mouse13',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse13 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse14',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse14 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse15',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse15 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse16',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse16 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse17',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse17 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse18',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse18 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse21',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse21 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse22',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse22 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse23',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse23 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse24',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse24 SCORED per epoch frequency spectrum.csv']],
                                      
        #                               'yellow recovery':[['mouse13',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse13 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse14',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse14 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse15',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse15 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse16',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse16 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse17',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse17 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse18',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse18 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse21',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse21 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse22',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse22 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse23',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse23 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse24',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse24 SCORED recovery per epoch frequency spectrum.csv']]}
    
        
        # For green baseline vs green recovery matching comparison on single graphs
        # experimentalRecordingsDict = {'green recovery':[['mouse1',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse1 SCORED, recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse2',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse2 SCORED, recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse3',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse3 SCORED, recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse4',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse4 SCORED, recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse9',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse9 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse10',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse10 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse11',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse11 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse12',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse12 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse19',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse19 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                 ['mouse20',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse20 SCORED recovery per epoch frequency spectrum.csv']]}
        
        # For yellow baseline vs yellow recovery matching comparison on single graphs
        # experimentalRecordingsDict = {'yellow recovery':[['mouse13',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse13 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse14',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse14 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse15',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse15 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse16',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse16 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse17',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse17 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse18',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse18 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse21',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse21 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse22',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse22 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse23',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse23 SCORED recovery per epoch frequency spectrum.csv'],
        #                                                   ['mouse24',r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse24 SCORED recovery per epoch frequency spectrum.csv']]}
        
        # experimentalRecordingsDict = {'yellow baseline':[['mouse13',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse13 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse14',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse14 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse15',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse15 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse16',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse16 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse17',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse17 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse18',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse18 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse21',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse21 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse22',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse22 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse23',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse23 SCORED per epoch frequency spectrum.csv'],
        #                                                   ['mouse24',r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse24 SCORED per epoch frequency spectrum.csv']]}
        
        #18 hour experimental recordings:
        experimentalRecordingsDict = {'green recovery':[['mouse1',r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 1, 4711, green 18h recovery FFTs.csv'],
                                                    ['mouse3',r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 3, 4713, green 18h recovery FFTs.csv'],
                                                    ['mouse4',r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 4, 4714, green 18h recovery FFTs.csv']], 
                                
                                  'yellow baseline':[['mouse14',r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 14, 4704, yellow18h baseline FFTs.csv'],
                                                      ['mouse15',r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 15, 4710, yellow18h baseline FFTs.csv'],
                                                      ['mouse16',r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 16, 4719, yellow18h baseline FFTs.csv']],
                                  
                                  'yellow recovery':[['mouse14',r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 14, 4704, yellow 18h recovery FFTs.csv'],
                                                      ['mouse15',r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 15, 4710, yellow 18h recovery FFTs.csv'],
                                                      ['mouse16',r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 16, 4719, yellow 18h recovery FFTs.csv']]}
        
        
        
        for key,value in experimentalRecordingsDict.items():
            # mouseName = value[0]
            # experimentalRecordings = value[1]
            experimentalCondition = key
            
    
            for eachMouse in value:
                mouseName = eachMouse[0]
                recNameCSV = eachMouse[1]
                # pdb.set_trace()
                
                print('Running ' + mouseName + ' ' + experimentalCondition)
                #fill dataframe for just experimental recordings
                experimentalPercents, experimentalDurations, experimentalFrequencies = sleep_stats(mouseName, recNameCSV, 10, tstart = tstart, tend = tend, pplot=False)        
                
                data1 = [[mouseName, experimentalPercents[0][0], experimentalDurations[0][0], experimentalFrequencies[0][0], 'REM', experimentalCondition, 'Full Recording']]        
                tempDF1 = pd.DataFrame(data1, columns = labels)
                
                data2 = [[mouseName, experimentalPercents[0][1], experimentalDurations[0][1], experimentalFrequencies[0][1], 'WAKE', experimentalCondition, 'Full Recording']]        
                tempDF2 = pd.DataFrame(data2, columns = labels)
                
                data3 = [[mouseName, experimentalPercents[0][2], experimentalDurations[0][2], experimentalFrequencies[0][2], 'NREM', experimentalCondition, 'Full Recording']]        
                tempDF3 = pd.DataFrame(data3, columns = labels)
                
                data4 = [[mouseName, experimentalPercents[0][3], experimentalDurations[0][3], experimentalFrequencies[0][3], 'NREM to REM \n Transition', experimentalCondition, 'Full Recording']]        
                tempDF4 = pd.DataFrame(data4, columns = labels)
         
                mouseStats = mouseStats.append(tempDF1)
                mouseStats = mouseStats.append(tempDF2)
                mouseStats = mouseStats.append(tempDF3)
                mouseStats = mouseStats.append(tempDF4)
    
                
                if mouseName not in experimentalMiceList:
                        experimentalMiceList.append(mouseName)
                        
        # if we're rerunning it, save it as new csv
        mouseStats.to_csv('D:\VeaseyLabMaterialsJoe\sleepRecs\mouseStats.csv')
    else: #if we're passing in a csv with mousestats saved already
        mouseStats = pd.read_csv(mouseStats_csvToLoad) #load that csv
            
       
 
    ##############################
    #### PLOT FULL RECORDINGS ####
    ############################## 
    
    #First suppress plotting exceptions spamming console
    import logging, sys
    logging.disable(sys.maxsize)
    
    if not plotLightvsDark:

        if mouseLabels: 
         
            if singleGraphs:
                for eachStat in statsLabelList:                 
                    for eachBrainState in brainStateList:
                        
                        dataToUse = mouseStats.loc[mouseStats['Brain State'] == eachBrainState]
         
                        #Get data for mouseLabels -- new dataframe with the averages of the stat instead of all of them.
                        mouseLabelsDF = pd.DataFrame(columns = labels)                              
                        mouseNames = dataToUse['Name'].unique()
                        for eachName in mouseNames:
                            #Get list of conditions
                            tempDF = dataToUse.loc[dataToUse['Name'] == eachName]    
                            conditions = tempDF['Condition'].unique()
                                                        
                            #Get mean across all numeric columns
                            tempDF0 = dataToUse.loc[dataToUse['Name'] == eachName]   #first slice rows by name, to get all rows for the current mouse
                            tempDF1 = tempDF0.loc[tempDF0['Brain State'] == eachBrainState] #then slice rows by brainstate. Necessary because if not, then df.mean averages across all brain states per mouse   

                            #Sort by condition and take means, then reconstruct the dataframe
                            for eachCondition in conditions:
                                
                                tempDF2 = tempDF1.loc[tempDF1['Condition'] == eachCondition]
                                tempDFMean = tempDF2.mean()  
                                
                                tempDFMeanPercent = tempDFMean['Percent']
                                tempDFMeanDuration = tempDFMean['Duration']
                                tempDFMeanFrequency = tempDFMean['Frequency']
                                                               
                                #Format the data to be used for the mean data frame
                                meanData = [[eachName, tempDFMeanPercent, tempDFMeanDuration, tempDFMeanFrequency, eachBrainState, eachCondition, 'Full Recording' ]]
                                #Reconstruct the mean data frame
                                mouseMeanDF = pd.DataFrame(data = meanData, columns = labels)
                                                        
                                #Add the new mean data frame to a bigger one line by line
                                #The resulting data frame is the same as the original mouseStats but instead of multiple rows per mouse, there's just one with the average values
                                mouseLabelsDF = mouseLabelsDF.append(mouseMeanDF)   
                                  
                        ##### Now actually plot everything ####
                        plt.figure()                        
                        #Plot barplots, which are averages of all data points   
                        ax = sns.barplot(y = eachStat, x = 'Condition', palette = clrs, data = dataToUse)  #ci = None for no error bars  
                        if allMousePoints:
                            sns.stripplot(y = eachStat, x = 'Condition', jitter=jitter, s=7, data=dataToUse, color = 'black', ax = ax)
                        else:
                            #Then plot individual mouse points, which are means per mouse
                            if not bars:
                                #pick one, not both
                                sns.stripplot(y = eachStat, x = 'Condition', hue = 'Name', jitter=jitter, s=7, data=mouseLabelsDF, color='black', ax = ax) #palette = 'bright' for when you want to plot the labels/legend
#                                sns.stripplot(y = eachStat, x = 'Condition', hue = 'Name', jitter=jitter, s=7, data=mouseLabelsDF, color = 'black', ax = ax)
                            if len(conditions) < 3 and bars:
                                #If you're plotting individual graphs with just 2 conditions and want lines between the bars instead of just points use this and disable stripplot!!
                                condition1 = mouseLabelsDF.loc[mouseLabelsDF['Condition'] == controlCondition]
                                condition1Stat = condition1[eachStat].tolist()
                                condition2 = mouseLabelsDF.loc[mouseLabelsDF['Condition'] == experimentalCondition]
                                condition2Stat = condition2[eachStat].tolist()
    #                            pdb.set_trace()
                                for (a,b) in zip(condition1Stat, condition2Stat): 
                                    plt.plot([0, 1], [float(a),float(b)], color='black')
                            elif len(conditions) > 2 and bars:
                                print('Can only have 2 conditions to display bars.')
                                return
                            
                        #Make Figure pretty
                        if eachStat == 'Percent':
                            if eachBrainState == 'REM':
                                ax.set_ylim(0,12)
                            elif eachBrainState == 'NREM to REM \n Transition':
                                ax.set_ylim(0,6)
                            else:
                                ax.set_ylim(0,100)
                        ax.set_title(eachBrainState + ' ' + eachStat)
                        # plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.5) #DEFAULT, USE FOR LEGEND
                        plt.legend([],[], frameon=False) #TURNS LEGEND OFF
                        plt.tight_layout() 
                        plt.show()   
            
            #################### PLOT SUBPLOTS VARIANT #####################
            else:
                dataToUse = mouseStats
                for eachExcludedBrainState in excludedBrainStateList:
                    dataToUse = mouseStats.loc[mouseStats['Brain State'] != eachExcludedBrainState]
                
                mouseLabelsDF = pd.DataFrame(columns = labels)
                
                figDimensions = (12,8)
                
#                if allMousePoints:
#                    figDimensions = (14,10) #fixes graphs so that the bars won't float above x-axis when allMousePoints enabled (for some reason...)
                
                for eachStat in statsLabelList:                  
                    #set up our subplots first
                    fig, axes = plt.subplots(1, len(brainStateList), sharex = True, sharey = True, figsize = figDimensions) #Be sure to set figsize to something that looks good      
                    numPlot = 0

                    for eachBrainState in brainStateList:                         
                        #Get labels to use in order to reconstruct the dataframe
                        #Get brain state
                        brainStateTemp = dataToUse['Brain State'].unique()
                        for state in brainStateTemp:
                            if state == eachBrainState:
                                brainState = state  
                                

                        #Get data for mouseLabels -- new dataframe with the averages of the stat instead of all of them.                                                  
                        mouseNames = dataToUse['Name'].unique()
                        for eachName in mouseNames:                                                          
                            #Get list of conditions
                            tempDF = dataToUse.loc[dataToUse['Name'] == eachName]    
                            conditions = tempDF['Condition'].unique()
                                                        
                            #Get mean across all numeric columns
                            tempDF0 = dataToUse.loc[dataToUse['Name'] == eachName]   #first slice rows by name, to get all rows for the current mouse
                            tempDF1 = tempDF0.loc[tempDF0['Brain State'] == eachBrainState] #then slice rows by brainstate. Necessary because if not, then df.mean averages across all brain states per mouse   

                            #Sort by condition and take means, then reconstruct the dataframe
                            for eachCondition in conditions:
                                
                                tempDF2 = tempDF1.loc[tempDF1['Condition'] == eachCondition]
                                tempDFMean = tempDF2.mean()  
                                
                                tempDFMeanPercent = tempDFMean['Percent']
                                tempDFMeanDuration = tempDFMean['Duration']
                                tempDFMeanFrequency = tempDFMean['Frequency']
                                                               
                                #Format the data to be used for the mean data frame
                                meanData = [[eachName, tempDFMeanPercent, tempDFMeanDuration, tempDFMeanFrequency, brainState, eachCondition, 'Full Recording' ]]
                                #Reconstruct the mean data frame
                                mouseMeanDF = pd.DataFrame(data = meanData, columns = labels)
                                                        
                                #Add the new mean data frame to a bigger one line by line
                                #The resulting data frame is the same as the original mouseStats but instead of multiple rows per mouse, there's just one with the average values
                                mouseLabelsDF = mouseLabelsDF.append(mouseMeanDF)                  
    
                        ##### Now actually plot everything ####
                        
                        #Plot barplots, which are averages of all data points 
#                        pdb.set_trace()
                        if len(brainStateList) != 1:
                            sns.barplot(y = eachStat, x = 'Condition', palette = clrs, data = dataToUse.loc[dataToUse['Brain State'] == eachBrainState], ax = axes[numPlot]) 
                        else:
                            sns.barplot(y = eachStat, x = 'Condition', palette = clrs, data = dataToUse.loc[dataToUse['Brain State'] == eachBrainState]) 
                        
                        if allMousePoints:
                            if len(brainStateList) != 1:
                                sns.stripplot(y = eachStat, x = 'Condition', jitter=jitter, s=7, data = dataToUse.loc[dataToUse['Brain State'] == eachBrainState], color = 'black', ax = axes[numPlot]) 
                            else:
                                sns.stripplot(y = eachStat, x = 'Condition', jitter=jitter, s=7, data = dataToUse.loc[dataToUse['Brain State'] == eachBrainState], color = 'black') 
                        else:
                            #Then plot individual mouse points, which are means per mouse
                            if len(brainStateList) != 1:
                                sns.stripplot(y = eachStat, x = 'Condition', hue = 'Name', jitter=jitter, s=7, data = mouseLabelsDF.loc[mouseLabelsDF['Brain State'] == eachBrainState], palette = 'bright', ax = axes[numPlot]) 
                            else:
                                sns.stripplot(y = eachStat, x = 'Condition', hue = 'Name', jitter=jitter, s=7, data = mouseLabelsDF.loc[mouseLabelsDF['Brain State'] == eachBrainState], palette = 'bright') 
                        #Fix up the plots
                        if len(brainStateList) != 1:
                            axes[numPlot].set(xlabel = eachBrainState)   #Instead of 'Condition' under each subplot, plot brain state instead. 
                        else: 
                            plt.xlabel(eachBrainState)
                        plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.5)
                        
                        sns.despine()
                        if numPlot != 0:
                            axes[numPlot].get_yaxis().set_visible(False) #get rid of y-axis ticks
                            axes[numPlot].set(ylabel = '') #get rid of y-axis label if its not the first one.     
                            sns.despine(left = True, ax = axes[numPlot])
                            for eachGraph in range(len(brainStateList) - 1):
                                if eachGraph != 0:
                                    sns.despine(left = True, ax = axes[eachGraph])
                            
                        if not allMousePoints: #only do this with regular mouse labels.
                            if numPlot != len(brainStateList) - 1: #only put legend on last subplot
                                axes[numPlot].get_legend().remove()
                            
                        fig.suptitle(eachStat)                                       
                        plt.tight_layout() 
                        plt.show()
                        numPlot += 1
            
        #### NORMAL PLOTTING FOR FULL RECORDINGS, NO MOUSE LABELS ####       
        else: 
            ##Slice out brain state rows based on brain state flags in arguments
            dataToUse = mouseStats
            for eachExcludedBrainState in excludedBrainStateList:
                dataToUse = mouseStats.loc[mouseStats['Brain State'] != eachExcludedBrainState]
            if singleGraphs:        
                for eachStat in statsLabelList: 
                    for eachBrainState in brainStateList:
                        plt.figure()
                        sns.barplot(y = eachStat, x = 'Brain State', hue = 'Condition', palette = clrs, data = dataToUse.loc[dataToUse['Brain State'] == eachBrainState])
                        plt.title(eachStat)
                        plt.tight_layout()
                        plt.show()
            else:
                for eachStat in statsLabelList:   
                    plt.figure()
                    sns.barplot(y = eachStat, x = 'Brain State', hue = 'Condition', palette = clrs, data = dataToUse) #ci = None is to turn off error bars
                    plt.title(eachStat)
                    plt.tight_layout()
                    plt.show()
       
    #############################################        
    #### PLOT LIGHT AND DARK DATA IF ENABLED ####
    #############################################
    else:    

        if plotLDPhaseOnSameGraph:
            if not singleGraphs and len(phaseList) > 1: #only makes sense to do this if singleGraphs is disabled or phase list has more than one phase
                
                if mouseLabels:
                    
                    dataToUseTemp = mouseStats
                    for eachExcludedBrainState in excludedBrainStateList:
                        dataToUseTemp = mouseStats.loc[mouseStats['Brain State'] != eachExcludedBrainState]
                    
                    for eachBrainState in brainStateList:   
                        dataToUse = dataToUseTemp.loc[dataToUseTemp['Brain State'] == eachBrainState]
                        
                        mouseLabelsDF = pd.DataFrame(columns = labels)
                        
                        for eachStat in statsLabelList:                  
                            #set up our subplots first
                            fig, axes = plt.subplots(1, len(phaseList), sharex = True, sharey = True, figsize = (10, 6)) #Be sure to set figsize to something that looks good
                            numPlot = 0
                           
                            for eachLDPhase in phaseList:        
                                #Get data for mouseLabels -- new dataframe with the averages of the stat instead of all of them.                                                  
                                mouseNames = dataToUse['Name'].unique()
                                for eachName in mouseNames:                                                            
                                    #Get labels to use in order to reconstruct the dataframe
                                    #Get brain state
                                    LDPhaseTemp = dataToUse['LDPhase'].unique()
                                    for eachPhase in LDPhaseTemp:
                                        if eachPhase == eachLDPhase:
                                            LDPhase = eachPhase                   
                                   
                                    #Get list of conditions
                                    tempDF = dataToUse.loc[dataToUse['Name'] == eachName]    
                                    conditions = tempDF['Condition'].unique()
                                                                
                                    #Get mean across all numeric columns
                                    tempDF0 = dataToUse.loc[dataToUse['Name'] == eachName]   #first slice rows by name, to get all rows for the current mouse
                                    tempDF1 = tempDF0.loc[tempDF0['Brain State'] == eachBrainState] #then slice rows by brainstate. Necessary because if not, then df.mean averages across all brain states per mouse   
        
                                    #Sort by condition and take means, then reconstruct the dataframe
                                    for eachCondition in conditions:
                                        
                                        tempDF2 = tempDF1.loc[tempDF1['Condition'] == eachCondition] #slice by condition
                                        tempDF3 = tempDF2.loc[tempDF2['LDPhase'] == eachLDPhase] #slice again by phase before taking mean
                                        tempDFMean = tempDF3.mean()  
                                        
                                        tempDFMeanPercent = tempDFMean['Percent']
                                        tempDFMeanDuration = tempDFMean['Duration']
                                        tempDFMeanFrequency = tempDFMean['Frequency']
                                                                       
                                        #Format the data to be used for the mean data frame
                                        meanData = [[eachName, tempDFMeanPercent, tempDFMeanDuration, tempDFMeanFrequency, eachBrainState, eachCondition, LDPhase ]]
                                        #Reconstruct the mean data frame
                                        mouseMeanDF = pd.DataFrame(data = meanData, columns = labels)
                                                                
                                        #Add the new mean data frame to a bigger one line by line
                                        #The resulting data frame is the same as the original mouseStats but instead of multiple rows per mouse, there's just one with the average values
                                        mouseLabelsDF = mouseLabelsDF.append(mouseMeanDF)   
            
                                ##### Now actually plot everything ####
                                
                                #Plot barplots, which are averages of all data points   
                                sns.barplot(y = eachStat, x = 'Condition', palette = clrs, data = dataToUse.loc[dataToUse['LDPhase'] == eachLDPhase], ax = axes[numPlot])                     
                                if allMousePoints:
                                    sns.stripplot(y = eachStat, x = 'Condition', jitter=jitter, s=7, data = dataToUse.loc[dataToUse['LDPhase'] == eachLDPhase], color = 'black', ax = axes[numPlot])
                                else:
                                    #Then plot individual mouse points, which are means per mouse                                  
                                    sns.stripplot(y = eachStat, x = 'Condition', hue = 'Name', jitter=jitter, s=7, data = mouseLabelsDF.loc[mouseLabelsDF['LDPhase'] == eachLDPhase], palette = 'bright', ax = axes[numPlot]) 
                                
                                #Fix up the plots
                                axes[numPlot].set(xlabel = eachLDPhase)   #Instead of 'Condition' under each subplot, plot brain state instead.                  
                                plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.5)
                                
                                sns.despine()
                                if numPlot != 0:
                                    axes[numPlot].get_yaxis().set_visible(False) #get rid of y-axis ticks
                                    axes[numPlot].set(ylabel = '') #get rid of y-axis label if its not the first one.     
                                    sns.despine(left = True, ax = axes[numPlot])
                                    for eachGraph in range(len(phaseList) - 1):
                                        if eachGraph != 0:
                                            sns.despine(left = True, ax = axes[eachGraph])
            
                                if not allMousePoints:
                                    if numPlot != len(phaseList) - 1: #only put legend on last subplot
                                        axes[numPlot].get_legend().remove()
                                                                                                            
                                plt.tight_layout() 
                                fig.suptitle(eachBrainState + ' ' + eachStat)
                                plt.show()                   
                                numPlot += 1
   
                else: #if plotLDPhaseOnSameGraph = True and singleGraphs = False and mouseLabels = False
                    for eachStat in statsLabelList:            
                        for eachBrainState in brainStateList: #Should generate 9 graphs   
                            dataToUse = mouseStats.loc[mouseStats['Brain State'] == eachBrainState]
                            plt.figure()
                            ax = sns.barplot(y = eachStat, x = 'LDPhase', hue = 'Condition', palette = clrs, data = dataToUse)                    
                            plt.title(eachBrainState + ' ' + eachStat)
                            plt.show()
                            
            #If single graphs True and/or len(phaseList) == 1, just redirect the script to plot single graphs so it doesn't error out
            else:   
#                print('%%%%%% WARNING %%%%%')
#                print('Current arguments incompatible due to only one LD phase selected. Rerunning to produce single graphs.')
                # plot(ppath = ppath, recordingFile=recordingFile, plotLightvsDark = plotLightvsDark, plotLDPhaseOnSameGraph = False, mouseLabels = mouseLabels, singleGraphs = singleGraphs,
                #            plotPercents = plotPercents, plotFrequencies = plotFrequencies, plotDurations = plotDurations,
                #            REM = REM, WAKE = WAKE, NREM = NREM, NREMtoREMTransition = NREMtoREMTransition)
                return
         
        #plotLDPhaseOnSameGraph = False
        #Mode for plotting all brain stats for full, then light, then dark on the same graph or singles            
        else:            
            if mouseLabels: 
                if singleGraphs:
                    
                    dataToUseTemp = mouseStats
                    for eachExcludedBrainState in excludedBrainStateList:
                        dataToUseTemp = mouseStats.loc[mouseStats['Brain State'] != eachExcludedBrainState]
                    
                    for eachBrainState in brainStateList: 
                        dataToUse = dataToUseTemp.loc[dataToUseTemp['Brain State'] == eachBrainState]
                        
                        mouseLabelsDF = pd.DataFrame(columns = labels)
                        
                        for eachStat in statsLabelList:                  
                            for eachLDPhase in phaseList:        
                                #Get data for mouseLabels -- new dataframe with the averages of the stat instead of all of them.                                                  
                                mouseNames = dataToUse['Name'].unique()
                                for eachName in mouseNames:                                         
                                    #Get labels to use in order to reconstruct the dataframe
                                    #Get brain state
                                    LDPhaseTemp = dataToUse['LDPhase'].unique()
                                    for eachPhase in LDPhaseTemp:
                                        if eachPhase == eachLDPhase:
                                            LDPhase = eachPhase  
                                            
                                    #Get list of conditions
                                    tempDF = dataToUse.loc[dataToUse['Name'] == eachName]    
                                    conditions = tempDF['Condition'].unique()
                                                                
                                    #Get mean across all numeric columns
                                    tempDF0 = dataToUse.loc[dataToUse['Name'] == eachName]   #first slice rows by name, to get all rows for the current mouse

                                    #Sort by condition and take means, then reconstruct the dataframe
                                    for eachCondition in conditions:
                                        tempDF1 = tempDF0.loc[tempDF0['LDPhase'] == eachLDPhase]
                                        tempDF2 = tempDF1.loc[tempDF1['Condition'] == eachCondition]
                                        tempDFMean = tempDF2.mean()  
                                        
                                        tempDFMeanPercent = tempDFMean['Percent']
                                        tempDFMeanDuration = tempDFMean['Duration']
                                        tempDFMeanFrequency = tempDFMean['Frequency']
                                                                       
                                        #Format the data to be used for the mean data frame
                                        meanData = [[eachName, tempDFMean['Percent'], tempDFMean['Duration'], tempDFMean['Frequency'], eachBrainState, eachCondition, LDPhase ]]
                                        #Reconstruct the mean data frame
                                        mouseMeanDF = pd.DataFrame(data = meanData, columns = labels)
                                                                
                                        #Add the new mean data frame to a bigger one line by line
                                        #The resulting data frame is the same as the original mouseStats but instead of multiple rows per mouse, there's just one with the average values
                                        mouseLabelsDF = mouseLabelsDF.append(mouseMeanDF)  
                            
                            ##### Now actually plot everything ####
                            for eachPhase in phaseList:
                                plt.figure()
                                #Plot barplots, which are averages of all data points   
                                ax = sns.barplot(y = eachStat, x = 'Condition', palette = clrs, data = dataToUse.loc[dataToUse['LDPhase'] == eachPhase])   
                                if allMousePoints:
                                    sns.stripplot(y = eachStat, x = 'Condition', jitter=jitter, s=7, data=dataToUse.loc[dataToUse['LDPhase'] == eachPhase], color = 'black', ax = ax)
                                else:
                                    #Then plot individual mouse points, which are means per mouse
                                    sns.stripplot(y = eachStat, x = 'Condition', hue = 'Name', jitter=jitter, s=7, data=mouseLabelsDF.loc[mouseLabelsDF['LDPhase'] == eachPhase], palette = 'bright', ax = ax) 
                                #Make Figure pretty
                                ax.set_title(eachBrainState + ' ' + eachPhase + ' ' + eachStat)
                                plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.5)                  
                                plt.tight_layout() 
                                plt.show()        
                          
                    
                #Not singleGraphs
                else:
                    
                    if len(brainStateList) == 1:
#                        print('%%%%%% WARNING %%%%%')
#                        print('singleGraphs set to False but only one brain state selected.')
#                        print('Rerunning with singleGraphs set to True.')
                        plot(plotLightvsDark = plotLightvsDark, plotLDPhaseOnSameGraph = plotLDPhaseOnSameGraph, mouseLabels = mouseLabels, singleGraphs = True,
                             plotPercents = plotPercents, plotFrequencies = plotFrequencies, plotDurations = plotDurations,
                             REM = REM, WAKE = WAKE, NREM = NREM, NREMtoREMTransition = NREMtoREMTransition)
                        return
                    
                    dataToUseTemp = mouseStats
                    for eachExcludedBrainState in excludedBrainStateList:
                        dataToUseTemp = mouseStats.loc[mouseStats['Brain State'] != eachExcludedBrainState]
                        
                    for eachLDPhase in phaseList:   
                        dataToUse = dataToUseTemp.loc[dataToUseTemp['LDPhase'] == eachLDPhase]
                        
                        mouseLabelsDF = pd.DataFrame(columns = labels)
                        
                        for eachStat in statsLabelList:                  
                            #set up our subplots first
                            fig, axes = plt.subplots(1, len(brainStateList), sharex = True, sharey = True, figsize = (10, 6)) #Be sure to set figsize to something that looks good
                            numPlot = 0

                            for eachBrainState in brainStateList:        
                                #Get data for mouseLabels -- new dataframe with the averages of the stat instead of all of them.                                                  
                                mouseNames = dataToUse['Name'].unique()
                                for eachName in mouseNames:                        
                                    #Get list of conditions
                                    tempDF = dataToUse.loc[dataToUse['Name'] == eachName]    
                                    conditions = tempDF['Condition'].unique()
                                                                
                                    #Get mean across all numeric columns
                                    tempDF0 = dataToUse.loc[dataToUse['Name'] == eachName]   #first slice rows by name, to get all rows for the current mouse
                                    tempDF1 = tempDF0.loc[tempDF0['Brain State'] == eachBrainState] #then slice rows by brainstate. Necessary because if not, then df.mean averages across all brain states per mouse   
        
                                    #Sort by condition and take means, then reconstruct the dataframe
                                    for eachCondition in conditions:
                                        
                                        tempDF2 = tempDF1.loc[tempDF1['Condition'] == eachCondition]
                                        tempDFMean = tempDF2.mean()  
                                        
                                        tempDFMeanPercent = tempDFMean['Percent']
                                        tempDFMeanDuration = tempDFMean['Duration']
                                        tempDFMeanFrequency = tempDFMean['Frequency']
                                                                       
                                        #Format the data to be used for the mean data frame
                                        meanData = [[eachName, tempDFMeanPercent, tempDFMeanDuration, tempDFMeanFrequency, eachBrainState, eachCondition, eachLDPhase ]]
                                        #Reconstruct the mean data frame
                                        mouseMeanDF = pd.DataFrame(data = meanData, columns = labels)
                                                                
                                        #Add the new mean data frame to a bigger one line by line
                                        #The resulting data frame is the same as the original mouseStats but instead of multiple rows per mouse, there's just one with the average values
                                        mouseLabelsDF = mouseLabelsDF.append(mouseMeanDF)                
            
                                ##### Now actually plot everything ####
                                
                                #Plot barplots, which are averages of all data points   
                                sns.barplot(y = eachStat, x = 'Condition', palette = clrs, data = dataToUse.loc[dataToUse['Brain State'] == eachBrainState], ax = axes[numPlot])                      
                                if allMousePoints:
                                    sns.stripplot(y = eachStat, x = 'Condition', jitter=jitter, s=7, data = dataToUse.loc[dataToUse['Brain State'] == eachBrainState], color = 'black', ax = axes[numPlot]) 
                                else:
                                    #Then plot individual mouse points, which are means per mouse                   
                                    sns.stripplot(y = eachStat, x = 'Condition', hue = 'Name', jitter=jitter, s=7, data = mouseLabelsDF.loc[mouseLabelsDF['Brain State'] == eachBrainState], palette = 'bright', ax = axes[numPlot]) 
        
                                #Fix up the plots
                                axes[numPlot].set(xlabel = eachBrainState)   #Instead of 'Condition' under each subplot, plot brain state instead.                  
                                plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.5)
                                
                                sns.despine()
                                if numPlot != 0:
                                    axes[numPlot].get_yaxis().set_visible(False) #get rid of y-axis ticks
                                    axes[numPlot].set(ylabel = '') #get rid of y-axis label if its not the first one.     
                                    sns.despine(left = True, ax = axes[numPlot])
                                    for eachGraph in range(len(brainStateList) - 1):
                                        if eachGraph != 0:
                                            sns.despine(left = True, ax = axes[eachGraph])
      
                                if not allMousePoints:
                                    if numPlot != len(brainStateList) - 1: #only put legend on last subplot
                                        axes[numPlot].get_legend().remove()
                                    
                                fig.suptitle(eachLDPhase + ' ' + eachStat)                                        
                                plt.tight_layout()                                
                                plt.show()                   
                                numPlot += 1

            else:               
                #Slice out brain state rows based on brain state flags in arguments  
                dataToUse = mouseStats #So the first iteration of the for loop knows what dataToUse is.
                for eachExcludedBrainState in excludedBrainStateList:
                    dataToUse = dataToUse.loc[dataToUse['Brain State'] != eachExcludedBrainState]

                if singleGraphs:                
                    for eachStat in statsLabelList:
                        
                        for eachPhase in phaseList:                              
                            dataToUse2 = dataToUse.loc[dataToUse['LDPhase'] == eachPhase]  
                            
                            for eachBrainState in brainStateList:
                                dataToUse3 = dataToUse2.loc[dataToUse2['Brain State'] == eachBrainState] #To get single graphs, slice rows by brain state and create a plotting for loop to plot each brain state separately                                
                                plt.figure()
                                ax = sns.barplot(y = eachStat, x = 'Brain State', hue = 'Condition', palette = clrs, data = dataToUse3)
                                plt.title(eachPhase + ' ' + eachBrainState + ' ' + eachStat)
                                plt.show()
                else:
                    for eachStat in statsLabelList:
                        for eachPhase in phaseList:                              
                            dataToUse2 = dataToUse.loc[dataToUse['LDPhase'] == eachPhase]       
                            plt.figure()
                            ax = sns.barplot(y = eachStat, x = 'Brain State', hue = 'Condition', palette = clrs, data = dataToUse2)
                            plt.title(eachPhase + ' ' + eachStat)
                            plt.show()

    return mouseStats






###################### S T A T S ##############################################
###############################################################################


#Modified to handle the NREM to REM transition state, which is marked by pressing 'T' in the new sleep_annotation_qt.py and is included here as brain state '6'
#Also handles light and dark period
def sleep_stats(mouseName, recNameCSV, ma_thr=10.0, tstart=0, tend=-1, pplot=False):
    """
    Calculate average percentage of each brain state,
    average duration and average frequency
    plot histograms for REM, NREM, and Wake durations
    @PARAMETERS:
    ppath      -   base folder
    recordings -   single string specifying recording or list of recordings

    @OPTIONAL:
    ma_thr     -   threshold for wake periods to be considered as microarousals
    tstart     -   only consider recorded data starting from time tstart, default 0s
    tend       -   only consider data recorded up to tend s, default -1, i.e. everything till the end
    pplot      -   generate plot in the end; True or False
    csv_file   -   file where data should be saved as csv file (e.g. csv_file = '/home/Users/Franz/Documents/my_data.csv')

    @RETURN:
        ndarray of percentages (# mice x [REM,Wake,NREM,NREMtoREMTransitions])
        ndarray of state durations
        ndarray of transition frequency / hour
    """
    # if type(recNameCSV) != list:
        # recNameCSV = [recNameCSV]

    Percentage = {}
    Duration = {}
    Frequency = {}
    mice = []
    for rec in recNameCSV:
        idf = mouseName
        if not idf in mice:
            mice.append(idf)
        Percentage[idf] = {1:[], 2:[], 3:[], 4:[]}
        Duration[idf] = {1:[], 2:[], 3:[], 4:[]}
        Frequency[idf] = {1:[], 2:[], 3:[], 4:[]}
    nmice = len(Frequency)
    
    # nmice=1 #hardcode because we're doing this one at a time
    
    # Percentage = {1:[], 2:[], 3:[], 4:[]}
    # Duration = {1:[], 2:[], 3:[], 4:[]}
    # Frequency = {1:[], 2:[], 3:[], 4:[]}
    
    # idf = mouseName

    for rec in recNameCSV:
        # #idf is the mouse ID
        # SR = sleepy.get_snr(ppath, rec)
        SR = 250 # hardcoded
        NBIN = np.round(4*SR) #length of epochs is 4 seconds
        dt = NBIN * 1/SR

        # # load brain state
        # M, K = sleepy.load_stateidx(ppath, rec)
        # kcut = np.where(K >= 0)[0]
        # M = M[kcut]
        
        # Load each CSV, extract stage list and convert to numbered format to work with sleepy functions
        data = pd.read_csv(recNameCSV)
        
        # pdb.set_trace()
        epochs = data['Stage'].tolist()
        M = np.asarray(epochs)
        
        
        M[M == 'R'] = 1
        M[M == 'W'] = 2
        M[M == 'NR'] = 3

        M = M.astype(np.float)

        # pdb.set_trace()
        
        
        # polish out microarousals
        # M[np.where(M==5)] = 2                
        # seq = sleepy.get_sequences(np.where(M==2)[0])
        # for s in seq:
        #     if len(s)*dt <= ma_thr:
        #         M[s] = 3
        
        ########### CALCULATE ISTART AND IEND ################
        if type(tstart) == int: #If we pass in an integer, proceed as normal
            istart = int(np.round((1.0 * tstart) / dt))
            if tend==-1:
                iend = len(M)-1
            else:
                iend = int(np.round((1.0*tend) / dt))
    
            midx = np.arange(istart,iend+1) #Generate integers for the range from istart to iend, +1 because iarange isn't inclusive of the last value so we force it
            Mcut = M[midx] #Cut M, which is the actual full recording, with the range we specify with istart and iend
            nm = len(Mcut)*1.0 #Get the length of that range
            
                # get percentage of each state
            for s in [1,2,3,4]:
                # pdb.set_trace()
                Percentage[idf][s].append(len(np.where(Mcut==s)[0]) / nm)
                
            # get frequency of each state
            for s in [1,2,3,4]:
                Frequency[idf][s].append( len(sleepy.get_sequences(np.where(Mcut==s)[0])) * (3600. / (nm*dt)) )
                
            # get average duration for each state
            for s in [1,2,3,4]:
                seq = sleepy.get_sequences(np.where(Mcut==s)[0])
                Duration[idf][s] += [len(i)*dt for i in seq] 
                
#if we pass in a list of start times and a list of end times in the case of multiple light periods for instance, account for multiple periods to run stats on                        
        else: 
            istart = []
            iend = []
            for eachValue in tstart: #create istart and iend values from tstart and tend values
                istartTemp = int(np.round((1.0 * eachValue) / dt))
                istart.append(istartTemp)
            for eachValue in tend:
                iendTemp = int(np.round((1.0*eachValue) / dt))
                iend.append(iendTemp)
            
            #generate list of cuts
            #method 1
            midx = []
            for i in range(len(istart)):
#                midx.append(np.arange(istart[i],iend[i]+1)) #for each value in istart (and implicitly iend), generate the range of numbers between istart and iend for each pair of them 
                midx.append(np.arange(istart[i],iend[i]))
                
            Mcut = [] 
            nm = 0
            for eachRange in midx:
                McutSub = M[eachRange]
                Mcut.append(McutSub)
                nm += len(eachRange) #accumulate lenghts of full range
            #Mcut is now a list of ranges in M (which is the full recording range)
            
             # get percentage of each state
            for s in [1,2,3,4]:
                numState = 0
                for eachRange in Mcut:
                    eachRangeNumState = len(np.where(eachRange==s)[0])
                    numState += eachRangeNumState
                Percentage[idf][s].append(numState / nm)
            
            # get frequency of each state
            for s in [1,2,3,4]:
                numSequences = 0
                for eachRange in Mcut:
                    eachRangeNumSequences = len(sleepy.get_sequences(np.where(eachRange==s)[0]))
                    numSequences += eachRangeNumSequences                
                Frequency[idf][s].append( numSequences * (3600. / (nm*dt)) )

            
             # get average duration for each state
            for s in [1,2,3,4]:
                for eachRange in Mcut: #for the first light period and the 2nd light period
                    eachRangeSeq = sleepy.get_sequences(np.where(eachRange==s)[0])
                    Duration[idf][s] += [len(i)*dt for i in eachRangeSeq]
                    
    #proceed as normal    
    PercMx = np.zeros((nmice,4))
    i=0
    for k in mice:
        for s in [1,2,3,4]:
            if s == 4:
                PercMx[i,3] = np.array(Percentage[k][4]).mean()
            else:
                PercMx[i,s-1] = np.array(Percentage[k][s]).mean()
        i += 1
    PercMx *= 100
        
    FreqMx = np.zeros((nmice,4))
    i = 0
    for k in mice:
        for s in [1,2,3,4]:
            if s == 6:
                FreqMx[i,3] = np.array(Frequency[k][4]).mean()
            else:
                FreqMx[i,s-1] = np.array(Frequency[k][s]).mean()
        i += 1
    
    DurMx = np.zeros((nmice,4))
    i = 0
    for k in mice:
        for s in [1,2,3,4]:
            if s == 4:
                DurMx[i,3] = np.array(Duration[k][4]).mean()
            else:
                DurMx[i,s-1] = np.array(Duration[k][s]).mean()
        i += 1
        
    DurHist = {1:[], 2:[], 3:[], 4:[]}
    for s in [1,2,3,4]:
        DurHist[s] = np.squeeze(np.array(reduce(lambda x,y: x+y, [Duration[k][s] for k in Duration])))

    return PercMx, DurMx, FreqMx

