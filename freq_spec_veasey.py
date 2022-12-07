import pdb
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
import pingouin as pg

numRawEpochs = 5400
# numRawEpochs = 16200

baseline = ['baseline'] * numRawEpochs
recovery = ['recovery'] * numRawEpochs
green = ['green'] * numRawEpochs
yellow = ['yellow'] * numRawEpochs
mouse1 = ['mouse1'] * numRawEpochs
mouse2 = ['mouse2'] * numRawEpochs
mouse3 = ['mouse3'] * numRawEpochs
mouse4 = ['mouse4'] * numRawEpochs
mouse5 = ['mouse5'] * numRawEpochs
mouse6 = ['mouse6'] * numRawEpochs
mouse7 = ['mouse7'] * numRawEpochs
mouse8 = ['mouse8'] * numRawEpochs
mouse9 = ['mouse9'] * numRawEpochs
mouse10 = ['mouse10'] * numRawEpochs
mouse11 = ['mouse11'] * numRawEpochs
mouse12 = ['mouse12'] * numRawEpochs
mouse13 = ['mouse13'] * numRawEpochs
mouse14 = ['mouse14'] * numRawEpochs
mouse15 = ['mouse15'] * numRawEpochs
mouse16 = ['mouse16'] * numRawEpochs
mouse17 = ['mouse17'] * numRawEpochs
mouse18 = ['mouse18'] * numRawEpochs
mouse19 = ['mouse19'] * numRawEpochs
mouse20 = ['mouse20'] * numRawEpochs
mouse21 = ['mouse21'] * numRawEpochs
mouse22 = ['mouse22'] * numRawEpochs
mouse23 = ['mouse23'] * numRawEpochs
mouse24 = ['mouse24'] * numRawEpochs

# baseline = ['baseline'] * numRawEpochs
# recovery = ['recovery'] * numRawEpochs
# green = ['green'] * numRawEpochs
# yellow = ['yellow'] * numRawEpochs
# mouse1 = ['mouse1'] * numRawEpochs
# mouse3 = ['mouse3'] * numRawEpochs
# mouse4 = ['mouse4'] * numRawEpochs
# mouse14 = ['mouse14'] * numRawEpochs
# mouse15 = ['mouse15'] * numRawEpochs
# mouse16 = ['mouse16'] * numRawEpochs


#Load baseline recordings
mouse1Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse1 SCORED, baseline per epoch frequency spectrum.csv'
mouse1BaselineDF = pd.read_csv(mouse1Baseline)
mouse1BaselineDF['sleepCondition'] = baseline
mouse1BaselineDF['foodCondition'] = green
mouse1BaselineDF['mouseNum'] = mouse1


mouse2Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse2 SCORED, baseline per epoch frequency spectrum.csv'
mouse2BaselineDF = pd.read_csv(mouse2Baseline)
mouse2BaselineDF['sleepCondition'] = baseline
mouse2BaselineDF['foodCondition'] = green
mouse2BaselineDF['mouseNum'] = mouse2

mouse3Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse3 SCORED, baseline per epoch frequency spectrums.csv'
mouse3BaselineDF = pd.read_csv(mouse3Baseline)
mouse3BaselineDF['sleepCondition'] = baseline
mouse3BaselineDF['foodCondition'] = green
mouse3BaselineDF['mouseNum'] = mouse3

mouse4Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse4 SCORED, baseline per epoch frequency spectrums.csv'
mouse4BaselineDF = pd.read_csv(mouse4Baseline)
mouse4BaselineDF['sleepCondition'] = baseline
mouse4BaselineDF['foodCondition'] = green
mouse4BaselineDF['mouseNum'] = mouse4

# mouse5Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse5 per epoch frequency spectrum, baseline yellow.csv'
# mouse5BaselineDF = pd.read_csv(mouse5Baseline)
# mouse5BaselineDF['sleepCondition'] = baseline
# mouse5BaselineDF['foodCondition'] = yellow
# mouse5BaselineDF['mouseNum'] = mouse5

# mouse6Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse6 per epoch frequency spectrum, baseline yellow.csv'
# mouse6BaselineDF = pd.read_csv(mouse6Baseline)
# mouse6BaselineDF['sleepCondition'] = baseline
# mouse6BaselineDF['foodCondition'] = yellow
# mouse6BaselineDF['mouseNum'] = mouse6

# mouse7Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse7 per epoch frequency spectrum, baseline yellow.csv'
# mouse7BaselineDF = pd.read_csv(mouse7Baseline)
# mouse7BaselineDF['sleepCondition'] = baseline
# mouse7BaselineDF['foodCondition'] = yellow
# mouse7BaselineDF['mouseNum'] = mouse7

# mouse8Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse8 per epoch frequency spectrum, baseline yellow.csv'
# mouse8BaselineDF = pd.read_csv(mouse8Baseline)
# mouse8BaselineDF['sleepCondition'] = baseline
# mouse8BaselineDF['foodCondition'] = yellow
# mouse8BaselineDF['mouseNum'] = mouse8

mouse9Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse9 SCORED per epoch frequency spectrum.csv'
mouse9BaselineDF = pd.read_csv(mouse9Baseline)
mouse9BaselineDF['sleepCondition'] = baseline
mouse9BaselineDF['foodCondition'] = green
mouse9BaselineDF['mouseNum'] = mouse9

mouse10Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse10 SCORED per epoch frequency spectrum.csv'
mouse10BaselineDF = pd.read_csv(mouse10Baseline)
mouse10BaselineDF['sleepCondition'] = baseline
mouse10BaselineDF['foodCondition'] = green
mouse10BaselineDF['mouseNum'] = mouse10

mouse11Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse11 SCORED per epoch frequency spectrum.csv'
mouse11BaselineDF = pd.read_csv(mouse11Baseline)
mouse11BaselineDF['sleepCondition'] = baseline
mouse11BaselineDF['foodCondition'] = green
mouse11BaselineDF['mouseNum'] = mouse11

mouse12Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse12 SCORED per epoch frequency spectrum.csv'
mouse12BaselineDF = pd.read_csv(mouse12Baseline)
mouse12BaselineDF['sleepCondition'] = baseline
mouse12BaselineDF['foodCondition'] = green
mouse12BaselineDF['mouseNum'] = mouse12

mouse13Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse13 SCORED per epoch frequency spectrum.csv'
mouse13BaselineDF = pd.read_csv(mouse13Baseline)
mouse13BaselineDF['sleepCondition'] = baseline
mouse13BaselineDF['foodCondition'] = yellow
mouse13BaselineDF['mouseNum'] = mouse13

mouse14Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse14 SCORED per epoch frequency spectrum.csv'
mouse14BaselineDF = pd.read_csv(mouse14Baseline)
mouse14BaselineDF['sleepCondition'] = baseline
mouse14BaselineDF['foodCondition'] = yellow
mouse14BaselineDF['mouseNum'] = mouse14

mouse15Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse15 SCORED per epoch frequency spectrum.csv'
mouse15BaselineDF = pd.read_csv(mouse15Baseline)
mouse15BaselineDF['sleepCondition'] = baseline
mouse15BaselineDF['foodCondition'] = yellow
mouse15BaselineDF['mouseNum'] = mouse15

mouse16Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse16 SCORED per epoch frequency spectrum.csv'
mouse16BaselineDF = pd.read_csv(mouse16Baseline)
mouse16BaselineDF['sleepCondition'] = baseline
mouse16BaselineDF['foodCondition'] = yellow
mouse16BaselineDF['mouseNum'] = mouse16

mouse17Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse17 SCORED per epoch frequency spectrum.csv'
mouse17BaselineDF = pd.read_csv(mouse17Baseline)
mouse17BaselineDF['sleepCondition'] = baseline
mouse17BaselineDF['foodCondition'] = yellow
mouse17BaselineDF['mouseNum'] = mouse17

mouse18Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse18 SCORED per epoch frequency spectrum.csv'
mouse18BaselineDF = pd.read_csv(mouse18Baseline)
mouse18BaselineDF['sleepCondition'] = baseline
mouse18BaselineDF['foodCondition'] = yellow
mouse18BaselineDF['mouseNum'] = mouse18

mouse19Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse19 SCORED per epoch frequency spectrum.csv'
mouse19BaselineDF = pd.read_csv(mouse19Baseline)
mouse19BaselineDF['sleepCondition'] = baseline
mouse19BaselineDF['foodCondition'] = green
mouse19BaselineDF['mouseNum'] = mouse19

mouse20Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse20 SCORED per epoch frequency spectrum.csv'
mouse20BaselineDF = pd.read_csv(mouse20Baseline)
mouse20BaselineDF['sleepCondition'] = baseline
mouse20BaselineDF['foodCondition'] = green
mouse20BaselineDF['mouseNum'] = mouse20

mouse21Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse21 SCORED per epoch frequency spectrum.csv'
mouse21BaselineDF = pd.read_csv(mouse21Baseline)
mouse21BaselineDF['sleepCondition'] = baseline
mouse21BaselineDF['foodCondition'] = yellow
mouse21BaselineDF['mouseNum'] = mouse21

mouse22Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse22 SCORED per epoch frequency spectrum.csv'
mouse22BaselineDF = pd.read_csv(mouse22Baseline)
mouse22BaselineDF['sleepCondition'] = baseline
mouse22BaselineDF['foodCondition'] = yellow
mouse22BaselineDF['mouseNum'] = mouse22

mouse23Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse23 SCORED per epoch frequency spectrum.csv'
mouse23BaselineDF = pd.read_csv(mouse23Baseline)
mouse23BaselineDF['sleepCondition'] = baseline
mouse23BaselineDF['foodCondition'] = yellow
mouse23BaselineDF['mouseNum'] = mouse23

mouse24Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\baseline\baseline per epoch frequency spectrums\mouse24 SCORED per epoch frequency spectrum.csv'
mouse24BaselineDF = pd.read_csv(mouse24Baseline)
mouse24BaselineDF['sleepCondition'] = baseline
mouse24BaselineDF['foodCondition'] = yellow
mouse24BaselineDF['mouseNum'] = mouse24



#Load recovery recordings
mouse1Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse1 SCORED, recovery per epoch frequency spectrum.csv'
mouse1RecoveryDF = pd.read_csv(mouse1Recovery)
mouse1RecoveryDF['sleepCondition'] = recovery
mouse1RecoveryDF['foodCondition'] = green
mouse1RecoveryDF['mouseNum'] = mouse1

mouse2Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse2 SCORED, recovery per epoch frequency spectrum.csv'
mouse2RecoveryDF = pd.read_csv(mouse2Recovery)
mouse2RecoveryDF['sleepCondition'] = recovery
mouse2RecoveryDF['foodCondition'] = green
mouse2RecoveryDF['mouseNum'] = mouse2

mouse3Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse3 SCORED, recovery per epoch frequency spectrum.csv'
mouse3RecoveryDF = pd.read_csv(mouse3Recovery)
mouse3RecoveryDF['sleepCondition'] = recovery
mouse3RecoveryDF['foodCondition'] = green
mouse3RecoveryDF['mouseNum'] = mouse3

mouse4Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse4 SCORED, recovery per epoch frequency spectrum.csv'
mouse4RecoveryDF = pd.read_csv(mouse4Recovery)
mouse4RecoveryDF['sleepCondition'] = recovery
mouse4RecoveryDF['foodCondition'] = green
mouse4RecoveryDF['mouseNum'] = mouse4

# mouse5Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse5 per epoch frequency spectrum, recovery yellow.csv'
# mouse5RecoveryDF = pd.read_csv(mouse5Recovery)
# mouse5RecoveryDF['sleepCondition'] = recovery
# mouse5RecoveryDF['foodCondition'] = yellow
# mouse5RecoveryDF['mouseNum'] = mouse5

# mouse6Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse6 per epoch frequency spectrum, recovery yellow.csv'
# mouse6RecoveryDF = pd.read_csv(mouse6Recovery)
# mouse6RecoveryDF['sleepCondition'] = recovery
# mouse6RecoveryDF['foodCondition'] = yellow
# mouse6RecoveryDF['mouseNum'] = mouse6

# mouse7Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse7 per epoch frequency spectrum, recovery yellow.csv'
# mouse7RecoveryDF = pd.read_csv(mouse7Recovery)
# mouse7RecoveryDF['sleepCondition'] = recovery
# mouse7RecoveryDF['foodCondition'] = yellow
# mouse7RecoveryDF['mouseNum'] = mouse7

# mouse8Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse8 per epoch frequency spectrum, recovery yellow.csv'
# mouse8RecoveryDF = pd.read_csv(mouse8Recovery)
# mouse8RecoveryDF['sleepCondition'] = recovery
# mouse8RecoveryDF['foodCondition'] = yellow
# mouse8RecoveryDF['mouseNum'] = mouse8

mouse9Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse9 SCORED recovery per epoch frequency spectrum.csv'
mouse9RecoveryDF = pd.read_csv(mouse9Recovery)
mouse9RecoveryDF['sleepCondition'] = recovery
mouse9RecoveryDF['foodCondition'] = green
mouse9RecoveryDF['mouseNum'] = mouse9

mouse10Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse10 SCORED recovery per epoch frequency spectrum.csv'
mouse10RecoveryDF = pd.read_csv(mouse10Recovery)
mouse10RecoveryDF['sleepCondition'] = recovery
mouse10RecoveryDF['foodCondition'] = green
mouse10RecoveryDF['mouseNum'] = mouse10

mouse11Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse11 SCORED recovery per epoch frequency spectrum.csv'
mouse11RecoveryDF = pd.read_csv(mouse11Recovery)
mouse11RecoveryDF['sleepCondition'] = recovery
mouse11RecoveryDF['foodCondition'] = green
mouse11RecoveryDF['mouseNum'] = mouse11

mouse12Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse12 SCORED recovery per epoch frequency spectrum.csv'
mouse12RecoveryDF = pd.read_csv(mouse12Recovery)
mouse12RecoveryDF['sleepCondition'] = recovery
mouse12RecoveryDF['foodCondition'] = green
mouse12RecoveryDF['mouseNum'] = mouse12

mouse13Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse13 SCORED recovery per epoch frequency spectrum.csv'
mouse13RecoveryDF = pd.read_csv(mouse13Recovery)
mouse13RecoveryDF['sleepCondition'] = recovery
mouse13RecoveryDF['foodCondition'] = yellow
mouse13RecoveryDF['mouseNum'] = mouse13

mouse14Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse14 SCORED recovery per epoch frequency spectrum.csv'
mouse14RecoveryDF = pd.read_csv(mouse14Recovery)
mouse14RecoveryDF['sleepCondition'] = recovery
mouse14RecoveryDF['foodCondition'] = yellow
mouse14RecoveryDF['mouseNum'] = mouse14

mouse15Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse15 SCORED recovery per epoch frequency spectrum.csv'
mouse15RecoveryDF = pd.read_csv(mouse15Recovery)
mouse15RecoveryDF['sleepCondition'] = recovery
mouse15RecoveryDF['foodCondition'] = yellow
mouse15RecoveryDF['mouseNum'] = mouse15

mouse16Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse16 SCORED recovery per epoch frequency spectrum.csv'
mouse16RecoveryDF = pd.read_csv(mouse16Recovery)
mouse16RecoveryDF['sleepCondition'] = recovery
mouse16RecoveryDF['foodCondition'] = yellow
mouse16RecoveryDF['mouseNum'] = mouse16

mouse17Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse17 SCORED recovery per epoch frequency spectrum.csv'
mouse17RecoveryDF = pd.read_csv(mouse17Recovery)
mouse17RecoveryDF['sleepCondition'] = recovery
mouse17RecoveryDF['foodCondition'] = yellow
mouse17RecoveryDF['mouseNum'] = mouse17

mouse18Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse18 SCORED recovery per epoch frequency spectrum.csv'
mouse18RecoveryDF = pd.read_csv(mouse18Recovery)
mouse18RecoveryDF['sleepCondition'] = recovery
mouse18RecoveryDF['foodCondition'] = yellow
mouse18RecoveryDF['mouseNum'] = mouse18

mouse19Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse19 SCORED recovery per epoch frequency spectrum.csv'
mouse19RecoveryDF = pd.read_csv(mouse19Recovery)
mouse19RecoveryDF['sleepCondition'] = recovery
mouse19RecoveryDF['foodCondition'] = green
mouse19RecoveryDF['mouseNum'] = mouse19

mouse20Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse20 SCORED recovery per epoch frequency spectrum.csv'
mouse20RecoveryDF = pd.read_csv(mouse20Recovery)
mouse20RecoveryDF['sleepCondition'] = recovery
mouse20RecoveryDF['foodCondition'] = green
mouse20RecoveryDF['mouseNum'] = mouse20

mouse21Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse21 SCORED recovery per epoch frequency spectrum.csv'
mouse21RecoveryDF = pd.read_csv(mouse21Recovery)
mouse21RecoveryDF['sleepCondition'] = recovery
mouse21RecoveryDF['foodCondition'] = yellow
mouse21RecoveryDF['mouseNum'] = mouse21

mouse22Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse22 SCORED recovery per epoch frequency spectrum.csv'
mouse22RecoveryDF = pd.read_csv(mouse22Recovery)
mouse22RecoveryDF['sleepCondition'] = recovery
mouse22RecoveryDF['foodCondition'] = yellow
mouse22RecoveryDF['mouseNum'] = mouse22

mouse23Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse23 SCORED recovery per epoch frequency spectrum.csv'
mouse23RecoveryDF = pd.read_csv(mouse23Recovery)
mouse23RecoveryDF['sleepCondition'] = recovery
mouse23RecoveryDF['foodCondition'] = yellow
mouse23RecoveryDF['mouseNum'] = mouse23

mouse24Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\recovery\recovery per epoch frequency spectrums\mouse24 SCORED recovery per epoch frequency spectrum.csv'
mouse24RecoveryDF = pd.read_csv(mouse24Recovery)
mouse24RecoveryDF['sleepCondition'] = recovery
mouse24RecoveryDF['foodCondition'] = yellow
mouse24RecoveryDF['mouseNum'] = mouse24




# # 18 hour post sleep dep pilot
# mouse1Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 1, 4711, green 18h baseline FFTs.csv'
# mouse1BaselineDF = pd.read_csv(mouse1Baseline)
# mouse1BaselineDF['sleepCondition'] = baseline
# mouse1BaselineDF['foodCondition'] = green
# mouse1BaselineDF['mouseNum'] = mouse1

# mouse3Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 3, 4713, green 18h baseline FFTs.csv'
# mouse3BaselineDF = pd.read_csv(mouse3Baseline)
# mouse3BaselineDF['sleepCondition'] = baseline
# mouse3BaselineDF['foodCondition'] = green
# mouse3BaselineDF['mouseNum'] = mouse3

# mouse4Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 4, 4714, green 18h baseline FFTs.csv'
# mouse4BaselineDF = pd.read_csv(mouse4Baseline)
# mouse4BaselineDF['sleepCondition'] = baseline
# mouse4BaselineDF['foodCondition'] = green
# mouse4BaselineDF['mouseNum'] = mouse4

# mouse14Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 14, 4704, yellow18h baseline FFTs.csv'
# mouse14BaselineDF = pd.read_csv(mouse14Baseline)
# mouse14BaselineDF['sleepCondition'] = baseline
# mouse14BaselineDF['foodCondition'] = yellow
# mouse14BaselineDF['mouseNum'] = mouse14

# mouse15Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 15, 4710, yellow18h baseline FFTs.csv'
# mouse15BaselineDF = pd.read_csv(mouse15Baseline)
# mouse15BaselineDF['sleepCondition'] = baseline
# mouse15BaselineDF['foodCondition'] = yellow
# mouse15BaselineDF['mouseNum'] = mouse15

# mouse16Baseline = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour baseline FFTs\mouse 16, 4719, yellow18h baseline FFTs.csv'
# mouse16BaselineDF = pd.read_csv(mouse16Baseline)
# mouse16BaselineDF['sleepCondition'] = baseline
# mouse16BaselineDF['foodCondition'] = yellow
# mouse16BaselineDF['mouseNum'] = mouse16



# mouse1Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 1, 4711, green 18h recovery FFTs.csv'
# mouse1RecoveryDF = pd.read_csv(mouse1Recovery)
# mouse1RecoveryDF['sleepCondition'] = recovery
# mouse1RecoveryDF['foodCondition'] = green
# mouse1RecoveryDF['mouseNum'] = mouse1

# mouse3Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 3, 4713, green 18h recovery FFTs.csv'
# mouse3RecoveryDF = pd.read_csv(mouse3Recovery)
# mouse3RecoveryDF['sleepCondition'] = recovery
# mouse3RecoveryDF['foodCondition'] = green
# mouse3RecoveryDF['mouseNum'] = mouse3

# mouse4Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 4, 4714, green 18h recovery FFTs.csv'
# mouse4RecoveryDF = pd.read_csv(mouse4Recovery)
# mouse4RecoveryDF['sleepCondition'] = recovery
# mouse4RecoveryDF['foodCondition'] = green
# mouse4RecoveryDF['mouseNum'] = mouse4

# mouse14Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 14, 4704, yellow 18h recovery FFTs.csv'
# mouse14RecoveryDF = pd.read_csv(mouse14Recovery)
# mouse14RecoveryDF['sleepCondition'] = recovery
# mouse14RecoveryDF['foodCondition'] = yellow
# mouse14RecoveryDF['mouseNum'] = mouse14

# mouse15Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 15, 4710, yellow 18h recovery FFTs.csv'
# mouse15RecoveryDF = pd.read_csv(mouse15Recovery)
# mouse15RecoveryDF['sleepCondition'] = recovery
# mouse15RecoveryDF['foodCondition'] = yellow
# mouse15RecoveryDF['mouseNum'] = mouse15

# mouse16Recovery = r'D:\VeaseyLabMaterialsJoe\sleepRecs\18 hour recovery FFTs\Mouse 16, 4719, yellow 18h recovery FFTs.csv'
# mouse16RecoveryDF = pd.read_csv(mouse16Recovery)
# mouse16RecoveryDF['sleepCondition'] = recovery
# mouse16RecoveryDF['foodCondition'] = yellow
# mouse16RecoveryDF['mouseNum'] = mouse16








freqList = ['0.000000Hz','0.244141Hz','0.488281Hz','0.732422Hz','0.976563Hz','1.220703Hz','1.464844Hz','1.708984Hz','1.953125Hz','2.197266Hz','2.441406Hz',
            '2.685547Hz','2.929688Hz','3.173828Hz','3.417969Hz','3.662109Hz','3.906250Hz','4.150391Hz','4.394531Hz','4.638672Hz','4.882813Hz','5.126953Hz',
            '5.371094Hz','5.615234Hz','5.859375Hz','6.103516Hz','6.347656Hz','6.591797Hz','6.835938Hz','7.080078Hz','7.324219Hz','7.568359Hz','7.812500Hz',
            '8.056641Hz','8.300781Hz','8.544922Hz','8.789063Hz','9.033203Hz','9.277344Hz','9.521484Hz','9.765625Hz','10.009766Hz','10.253906Hz','10.498047Hz',
            '10.742188Hz','10.986328Hz','11.230469Hz','11.474609Hz','11.718750Hz','11.962891Hz','12.207031Hz','12.451172Hz','12.695313Hz','12.939453Hz',
            '13.183594Hz','13.427734Hz','13.671875Hz','13.916016Hz','14.160156Hz','14.404297Hz','14.648438Hz','14.892578Hz','15.136719Hz','15.380859Hz',
            '15.625000Hz','15.869141Hz','16.113281Hz','16.357422Hz','16.601563Hz','16.845703Hz','17.089844Hz','17.333984Hz','17.578125Hz','17.822266Hz',
            '18.066406Hz','18.310547Hz','18.554688Hz','18.798828Hz','19.042969Hz','19.287109Hz','19.531250Hz','19.775391Hz']


deltaList = ['0.488281Hz','0.732422Hz','0.976563Hz','1.220703Hz','1.464844Hz','1.708984Hz','1.953125Hz','2.197266Hz','2.441406Hz','2.685547Hz',
             '2.929688Hz','3.173828Hz','3.417969Hz','3.662109Hz','3.906250Hz','4.150391Hz','4.394531Hz','4.638672Hz','4.882813Hz','5.126953Hz']


################# SWITCHES #####################
plotSpectrums = True
plotSpectrumsByBin = False

plotDeltaDecay = False

stateToAnalyze = 'NR'
# stateToAnalyze = 'W'
# stateToAnalyze = 'R'

binLength = 60 # in minutes, SET TO 360 FOR FULL 6 HOUR RECORDING, use for plotting delta decay + plotting spectrums by bin
epochLength = 4


#excluding mouse 5
dfList = [mouse1BaselineDF,mouse2BaselineDF,mouse3BaselineDF,mouse4BaselineDF,mouse9BaselineDF,mouse10BaselineDF,mouse11BaselineDF,mouse12BaselineDF,mouse13BaselineDF,mouse14BaselineDF,mouse15BaselineDF,mouse16BaselineDF,mouse17BaselineDF,mouse18BaselineDF,mouse19BaselineDF,mouse20BaselineDF,mouse21BaselineDF,mouse22BaselineDF,mouse23BaselineDF,mouse24BaselineDF,
          mouse1RecoveryDF,mouse2RecoveryDF,mouse3RecoveryDF,mouse4RecoveryDF,mouse9RecoveryDF,mouse10RecoveryDF,mouse11RecoveryDF,mouse12RecoveryDF,mouse13RecoveryDF,mouse14RecoveryDF,mouse15RecoveryDF,mouse16RecoveryDF,mouse17RecoveryDF,mouse18RecoveryDF,mouse19RecoveryDF,mouse20RecoveryDF,mouse21RecoveryDF,mouse22RecoveryDF,mouse23RecoveryDF,mouse24RecoveryDF]


# dfList = [mouse1BaselineDF,mouse3BaselineDF,mouse4BaselineDF,mouse9BaselineDF,mouse10BaselineDF,mouse11BaselineDF,mouse12BaselineDF,mouse13BaselineDF,mouse14BaselineDF,mouse15BaselineDF,mouse16BaselineDF,mouse17BaselineDF,mouse19BaselineDF,mouse20BaselineDF,mouse21BaselineDF,mouse23BaselineDF,mouse24BaselineDF,
#           mouse1RecoveryDF,mouse3RecoveryDF,mouse4RecoveryDF,mouse9RecoveryDF,mouse10RecoveryDF,mouse11RecoveryDF,mouse12RecoveryDF,mouse13RecoveryDF,mouse14RecoveryDF,mouse15RecoveryDF,mouse16RecoveryDF,mouse17RecoveryDF,mouse19RecoveryDF,mouse20RecoveryDF,mouse21RecoveryDF,mouse23RecoveryDF,mouse24RecoveryDF]


# 18 hour pilot
# dfList = [mouse1BaselineDF,mouse3BaselineDF,mouse4BaselineDF,mouse14BaselineDF,mouse15BaselineDF,mouse16BaselineDF,
#           mouse1RecoveryDF,mouse3RecoveryDF,mouse4RecoveryDF,mouse14RecoveryDF,mouse15RecoveryDF,mouse16RecoveryDF]



#calculate how many epochs to take
numSecondsPerBin = binLength*60
numEpochsPerBin = int(numSecondsPerBin/epochLength)

numBins = int(numRawEpochs/binLength) #5400 6 hours hardcoded, 4 s epoch length
binList = np.arange(0,numRawEpochs+numEpochsPerBin,numEpochsPerBin)
binNames = np.arange(0,360+binLength,binLength)

totalDeltaAvgDF = pd.DataFrame()
for eachDF in dfList:
    # first calculate total FFT avg using delta avg code from below
    tempDF = pd.DataFrame()
# get average delta power across whole recording to use for normalization
    totalFFTAvg = eachDF #take all FFT values regardless of stage
    
    totalFFTAvg = totalFFTAvg.drop(columns=['EpochNo','Stage','Time','sleepCondition','foodCondition','mouseNum'])
    totalFFTAvg = totalFFTAvg.mean(axis=0)
    totalPowers = totalFFTAvg.tolist()
    totalFFTAvgDict = dict(zip(freqList,totalPowers))
    allFreqVals = []
    for key,value in totalFFTAvgDict.items(): #THIS IS THE PART THATS DIFFERENT, TAKE ALL THE FREQUENCY VALUES INSTEAD OF JUST DELTA
        allFreqVals.append(value)
    totalFFTAvg = np.mean(allFreqVals)
    tempDF['totalFFTAvg'] = [totalFFTAvg]
    mouseNum = [eachDF['mouseNum'].unique()[0]]
    tempDF['mouseNum'] = mouseNum
    sleepCondition = [eachDF['sleepCondition'].unique()[0]]
    tempDF['sleepCondition'] = sleepCondition
    foodCondition = [eachDF['foodCondition'].unique()[0]]
    tempDF['foodCondition'] = foodCondition
    # totalFFTAvgDF = totalFFTAvgDF.append(tempDF)
    
    
    # Then calculate DELTA avg
# get average delta power across whole recording to use for normalization
    totalDeltaAvg = eachDF[eachDF['Stage'] == stateToAnalyze]
    
    totalDeltaAvg = totalDeltaAvg.drop(columns=['EpochNo','Stage','Time','sleepCondition','foodCondition','mouseNum'])
    totalDeltaAvg = totalDeltaAvg.mean(axis=0)
    totalPowers = totalDeltaAvg.tolist()
    totalDeltaAvgDict = dict(zip(freqList,totalPowers))
    deltaVals = []
    for key,value in totalDeltaAvgDict.items():
        if key in deltaList: #these values are odd because of sleep sign spitting out weird values
            deltaVals.append(value)
    totalDeltaAvg = np.mean(deltaVals)
    tempDF['totalDeltaAvg'] = [totalDeltaAvg] #use tempDF that was set up from above
    # mouseNum = [eachDF['mouseNum'].unique()[0]]
    # tempDF['mouseNum'] = mouseNum
    # sleepCondition = [eachDF['sleepCondition'].unique()[0]]
    # tempDF['sleepCondition'] = sleepCondition
    # foodCondition = [eachDF['foodCondition'].unique()[0]]
    # tempDF['foodCondition'] = foodCondition
    totalDeltaAvgDF = totalDeltaAvgDF.append(tempDF) #contains total FFT avg too
    

    
    
    
spectrumDF = pd.DataFrame()
deltaDF = pd.DataFrame()
# NREMDF = pd.DataFrame()
NREMFreqDF = pd.DataFrame()
NREMFreqDFTimeBins = pd.DataFrame()
avgNormDeltaPowerDF = pd.DataFrame()
for eachDF in dfList:
    eachDF = eachDF.drop('EpochNo',axis=1) #drop epoch number so we don't take the average on it
    
    NREMOnlyDF = eachDF[eachDF['Stage'] == stateToAnalyze]
    
    mouseNum = eachDF['mouseNum'].unique()[0]
    foodCondition = eachDF['foodCondition'].unique()[0]
    sleepCondition = eachDF['sleepCondition'].unique()[0]
    
    #Get Dataframe to use for FREQUENCY SPECTRUM calculations!!
    if plotSpectrums:
        
        if plotSpectrumsByBin: #So you can plot individual conditions and lots of overlayed NREM spectrums by bin
            for eachBin in binList: 
                if eachBin == binList[-1]: #if it's the last bin at 5400 we're done because there's nothing beyond 5400
                    continue
                start = eachBin
                end = eachBin + numEpochsPerBin
                tempDF = pd.DataFrame()
                tempDF = eachDF[start:end] #slice all epochs by index in range of start and stop bins
                NREMPerBinDF = tempDF[tempDF['Stage'] == stateToAnalyze] # THIS IS NOW NREM frequency list PER BIN ########
                
                NREMFreqDFTemp = pd.DataFrame()
                totalFFT = totalDeltaAvgDF[(totalDeltaAvgDF.sleepCondition == 'baseline') & (totalDeltaAvgDF.mouseNum == mouseNum) & (totalDeltaAvgDF.foodCondition == foodCondition)]
                totalFFT = totalFFT['totalFFTAvg'].tolist()[0]
                # reorganize dataframe into one long column with frequency
                for freq in freqList:
                    NREMFreqDFTempTemp = pd.DataFrame() #double temp lol
                    power = NREMPerBinDF[freq].tolist() #not NREMOnlyDF which is based on the full 6 hours
                    normPower = np.asarray(power) / totalFFT #Calculate normalized power for each frequency. Ie. the power value divided by the total average FFT
                    
                    NREMFreqDFTempTemp['power'] = power
                    NREMFreqDFTempTemp['normPower'] = normPower
                    freqLabel = [freq] * len(power)
                    NREMFreqDFTempTemp['freq'] = freqLabel
                    
                    NREMFreqDFTempTemp['mouseNum'] = [mouseNum] * len(power)
                    NREMFreqDFTempTemp['foodCondition'] = [foodCondition] * len(power)
                    NREMFreqDFTempTemp['sleepCondition'] = [sleepCondition] * len(power)
                    NREMFreqDFTempTemp['timeBin'] = [str(int(start*epochLength / 60)) + '-' + str(int(end*epochLength / 60))] * len(power)
                    NREMFreqDFTemp = NREMFreqDFTemp.append(NREMFreqDFTempTemp) #add double temp df to temp df
                NREMFreqDFTimeBins = NREMFreqDFTimeBins.append(NREMFreqDFTemp)

                
        else:
            NREMFreqDFTemp = pd.DataFrame()
            # reorganize dataframe into one long column with frequency
            for freq in freqList:
                totalFFT = totalDeltaAvgDF[(totalDeltaAvgDF.sleepCondition == 'baseline') & (totalDeltaAvgDF.mouseNum == mouseNum) & (totalDeltaAvgDF.foodCondition == foodCondition)]
                totalFFT = totalFFT['totalFFTAvg'].tolist()[0]
                
                NREMFreqDFTempTemp = pd.DataFrame() #double temp lol
                power = np.mean(NREMOnlyDF[freq].tolist())
                normPower = np.asarray(power) / totalFFT #Calculate normalized power for each frequency. Ie. the power value divided by the total average FFT
                NREMFreqDFTempTemp['power'] = [power]
                NREMFreqDFTempTemp['normPower'] = [normPower]
                # freqLabel = [freq] * len(power)
                freqLabel = freq
                NREMFreqDFTempTemp['freq'] = [freqLabel]
                
                # NREMFreqDFTempTemp['mouseNum'] = [mouseNum] * len(power)
                # NREMFreqDFTempTemp['foodCondition'] = [foodCondition] * len(power)
                # NREMFreqDFTempTemp['sleepCondition'] = [sleepCondition] * len(power)
                NREMFreqDFTempTemp['mouseNum'] = [mouseNum]
                NREMFreqDFTempTemp['foodCondition'] = [foodCondition]
                NREMFreqDFTempTemp['sleepCondition'] = [sleepCondition]
                NREMFreqDFTemp = NREMFreqDFTemp.append(NREMFreqDFTempTemp) #add double temp df to temp df
            NREMFreqDF = NREMFreqDF.append(NREMFreqDFTemp)
    
    

###############################################################################################################################



    
    if plotDeltaDecay:
        
        mouseNum = eachDF['mouseNum'].unique()[0]
        foodCondition = eachDF['foodCondition'].unique()[0]
        sleepCondition = eachDF['sleepCondition'].unique()[0]
         
        # Get dataFrame to use for Delta decay curves
        for eachBin in binList: 
            
            if eachBin == binList[-1]: #if it's the last bin at 5400 we're done because there's nothing beyond 5400
                continue
            start = eachBin
            end = eachBin + numEpochsPerBin
            tempDF = pd.DataFrame()
            tempDF = eachDF[start:end] #slice all epochs by index in range of start and stop bins
            
            NREMDFPerBin = pd.DataFrame()
            NREMDFPerBin = NREMDFPerBin.append(tempDF[tempDF['Stage'] == stateToAnalyze]) #now select for NREM bins, very important this is the tempDF and not eachDF
    
    
    
            # Get Dataframe to use for DELTA POWER OVER TIME calculations!!
            NREMDFToAvg = NREMDFPerBin.drop(columns=['Stage','Time','sleepCondition','foodCondition','mouseNum'])
                
            meanFreq = NREMDFToAvg.mean(axis=0)
            powers = meanFreq.tolist() #convert series to dataframe
            
            # pdb.set_trace()
            ###################################################################################
            #Normalize the powers list by the totalFFTAvg for that mouse and sleep condition -- NOT TOTALLY NECESSARY
            # x = totalDeltaAvgDF[(totalDeltaAvgDF.mouseNum == mouseNum) & (totalDeltaAvgDF.sleepCondition == sleepCondition) & (totalDeltaAvgDF.foodCondition == foodCondition)]
            # xval = x['totalFFTAvg'][0]
            # powers = [i/xval for i in powers]
            ###################################################################################
            
            # pdb.set_trace()
            NREMDFAvg = pd.DataFrame()
            NREMDFAvg['freq'] = freqList
            NREMDFAvg['power'] = powers
            mouseNum = [eachDF['mouseNum'].unique()[0]] * len(powers)
            NREMDFAvg['mouseNum'] = mouseNum
            sleepCondition = [eachDF['sleepCondition'].unique()[0]] * len(powers)
            NREMDFAvg['sleepCondition'] = sleepCondition
            foodCondition = [eachDF['foodCondition'].unique()[0]] * len(powers)
            NREMDFAvg['foodCondition'] = foodCondition
            NREMDFAvg['timeBin'] = [str(int(start*epochLength / 60)) + '-' + str(int(end*epochLength / 60))] * len(powers)
            
            spectrumDF = spectrumDF.append(NREMDFAvg)
            
            # pdb.set_trace()
            
            # cut out delta and build separated dataframe with average delta power across 0.5 to 5 hz
            freqDictNew = dict(zip(freqList,powers))
            deltaVals = []
            for key,value in freqDictNew.items():
                if key in deltaList: #these values are odd because of sleep sign spitting out weird values
                    deltaVals.append(value)
            deltaAvg = np.mean(deltaVals)
            
            #calculate percent of baseline -- deltaAvg of current bin divided by whole recording delta avg FROM BASELINE RECORDING
            mouseNum = eachDF['mouseNum'].unique()[0]
            foodCondition = eachDF['foodCondition'].unique()[0]
            sleepCondition = eachDF['sleepCondition'].unique()[0]
            
            
            #if sleep condition of current recording, want to divide by delta average from baseline (the first condition listed below)
            baselineDeltaAvg = totalDeltaAvgDF[(totalDeltaAvgDF.sleepCondition == 'baseline') & (totalDeltaAvgDF.mouseNum == mouseNum) & (totalDeltaAvgDF.foodCondition == foodCondition)]
            baselineDeltaAvg = baselineDeltaAvg['totalDeltaAvg'][0]
            # baselineDeltaAvg = baselineDeltaAvg['totalDeltaAvg'][0] / baselineDeltaAvg['totalFFTAvg'][0]  ### FOR normalization
    
    
    
            #when we're currently in a baseline recording we still end up dividing by baseline delta avg but it doesn't matter because we just won't plot it
            deltaPercentBaseline = (deltaAvg / baselineDeltaAvg) * 100 
            
            
            NREMDeltaDF = pd.DataFrame()
            NREMDeltaDF['deltaPower'] = [deltaAvg] #has to be a list to add appropriately
            NREMDeltaDF['deltaPercentBaseline'] = [deltaPercentBaseline]
            NREMDeltaDF['mouseNum'] = [NREMDFAvg['mouseNum'].unique()[0]]
            NREMDeltaDF['sleepCondition'] = NREMDFAvg['sleepCondition'].unique()[0]
            NREMDeltaDF['foodCondition'] = NREMDFAvg['foodCondition'].unique()[0]
            NREMDeltaDF['timeBin'] = [str(int(start*epochLength / 60)) + '-' + str(int(end*epochLength / 60))]
            
            
            deltaDF = deltaDF.append(NREMDeltaDF)
 
    


# pd.set_option("display.max_rows", None, "display.max_columns", None)
# pdb.set_trace()

if plotDeltaDecay:
    
    if binLength == 360: #get avg delta power to do unpaired ttest with
        # pdb.set_trace()
        print('Food Condition Normality')
        normality = pg.normality(data = deltaDF, dv = 'deltaPower', group = 'foodCondition', method = 'shapiro', alpha=0.05)
        print(normality)
        print('\n')
        
        print('Sleep Condition Normality')
        normality = pg.normality(data = deltaDF, dv = 'deltaPower', group = 'sleepCondition', method = 'shapiro', alpha=0.05)
        print(normality)
        print('\n')
        
        print('Mixed ANOVA for Avg 6 hour Delta Power')
        deltaANOVA = pg.mixed_anova(data=deltaDF, dv='deltaPower', between='foodCondition', within='sleepCondition', subject='mouseNum', correction=True, effsize='np2')
        pg.print_table(deltaANOVA)
        
        print('Pairwise ttests')
        deltaTtests = pg.pairwise_ttests(data=deltaDF, dv='deltaPower', between='foodCondition', within='sleepCondition', subject='mouseNum',within_first=True,padjust='bonf',alpha=0.05)
        pg.print_table(deltaTtests)
        
        fig,ax = plt.subplots(1,2)
        plt.subplot(1,2,1)
        sns.barplot(data=deltaDF[deltaDF['foodCondition'] == 'green'], x='foodCondition', y='deltaPower', hue='sleepCondition', palette=['darkgreen','limegreen'])
        sns.despine(right=True, top=True)
        # pg.plot_paired(data=deltaDF[deltaDF['foodCondition'] == 'green'], dv='deltaPower', within='sleepCondition', subject='mouseNum')
        # plt.ylim([0,.00014]) # --> pingouin plots don't work so well or something
        plt.subplot(1,2,2)
        sns.barplot(data=deltaDF[deltaDF['foodCondition'] == 'yellow'], x='foodCondition', y='deltaPower', hue='sleepCondition', palette=['darkgoldenrod','gold'])
        sns.despine(right=True, top=True)
        # pg.plot_paired(data=deltaDF[deltaDF['foodCondition'] == 'yellow'], dv='deltaPower', within='sleepCondition', subject='mouseNum')
        # plt.ylim([0,.00014])
    else:
        
    
        #plot delta powers
        plt.figure()
        DFToPlot = deltaDF[deltaDF['foodCondition'] == 'green']
        sns.lineplot(data = DFToPlot, x = 'timeBin', y = 'deltaPower', hue = 'sleepCondition', palette=['darkgreen','limegreen'], ci=95)
        plt.title('Mice on Green Food')
        plt.xticks(rotation=45, ha="right")
        
        plt.figure()
        DFToPlot = deltaDF[deltaDF['foodCondition'] == 'yellow']
        sns.lineplot(data = DFToPlot, x = 'timeBin', y = 'deltaPower', hue = 'sleepCondition', palette=['darkgoldenrod','gold'], ci=95)
        plt.title('Mice on yellow Food')
        plt.xticks(rotation=45, ha="right")
        
        plt.figure()
        DFToPlot = deltaDF[deltaDF['sleepCondition'] == 'baseline']
        sns.lineplot(data = DFToPlot, x = 'timeBin', y = 'deltaPower', hue = 'foodCondition', palette=['darkgreen','darkgoldenrod'], ci=95)
        plt.title('Green and Yellow Food Mice during Baseline')
        plt.xticks(rotation=45, ha="right")
        
        plt.figure()
        DFToPlot = deltaDF[deltaDF['sleepCondition'] == 'recovery']
        sns.lineplot(data = DFToPlot, x = 'timeBin', y = 'deltaPower', hue = 'foodCondition', palette=['limegreen','gold'], ci=95)
        plt.title('Green and Yellow Food Mice during Recovery')
        plt.xticks(rotation=45, ha="right")
        
        #Percent baseline
        plt.figure()
        DFToPlot = deltaDF[deltaDF['sleepCondition'] == 'recovery']
        sns.lineplot(data = DFToPlot, x = 'timeBin', y = 'deltaPercentBaseline', hue = 'foodCondition', palette=['darkgreen','darkgoldenrod'], ci=95)
        plt.axhline(y=100, color='black', linestyle='--')
        plt.title('Delta During Recovery as Percent Baseline')
        plt.xticks(rotation=45, ha="right")
        
        plt.figure()
        DFToPlot = deltaDF[deltaDF['sleepCondition'] == 'baseline']
        sns.lineplot(data = DFToPlot, x = 'timeBin', y = 'deltaPercentBaseline', hue = 'foodCondition', palette=['darkgreen','darkgoldenrod'], ci=95)
        plt.axhline(y=100, color='black', linestyle='--')
        plt.title('Delta During Baseline as Percent Baseline')
        plt.xticks(rotation=45, ha="right")
        
        ####################################################################################
        #STATS
        print('Decay normality Grouped by Food Condition')
        DFToPlot = deltaDF[deltaDF['sleepCondition'] == 'recovery']
        normality = pg.normality(data = DFToPlot, dv = 'deltaPercentBaseline', group = 'foodCondition', method = 'shapiro', alpha=0.05)
        print(normality)
        print('\n')
        
        
        deltaDF.to_csv('D:\VeaseyLabMaterialsJoe\sleepRecs\deltaDF.csv')
        
        # Test normality of 10 mice in green and yellow recovery at each time point. SOME ARE NORMAL SOME ARE NOT????
        # DOES THIS MEAN I HAVE TO USE SOMETHING OTHER THAN ANOVAS??
        # for timeBin in deltaDF['timeBin'].unique():
        #     test = deltaDF[(deltaDF['sleepCondition'] == 'recovery') & (deltaDF['foodCondition'] == 'green') & (deltaDF['timeBin'] == timeBin)]
        #     pg.qqplot(x=test['deltaPercentBaseline'].tolist())
        #     plt.title(timeBin)
        #     normality = pg.normality(data=test, dv='deltaPercentBaseline', group='foodCondition')
        #     pg.print_table(normality)
            
        #     test = deltaDF[(deltaDF['sleepCondition'] == 'recovery') & (deltaDF['foodCondition'] == 'yellow') & (deltaDF['timeBin'] == timeBin)]
        #     pg.qqplot(x=test['deltaPercentBaseline'].tolist())
        #     plt.title(timeBin)
        #     normality = pg.normality(data=test, dv='deltaPercentBaseline', group='foodCondition')
        #     pg.print_table(normality)
            
        
        #DeltaPower as percent baseline mixed ANOVA
        print('Delta as Percent Baseline Mixed ANOVA -- Within Timebins, Between Food Condition for Recovery')
        DFToPlot = deltaDF[deltaDF['sleepCondition'] == 'recovery'] #select only recovery
        deltaANOVA = pg.mixed_anova(data=DFToPlot, dv='deltaPercentBaseline', between='foodCondition', within='timeBin', subject='mouseNum', correction=True, effsize='np2')
        pg.print_table(deltaANOVA) #no main effect of food condition --> 0.665 uncorrected (nan corrected but doesn't matter because would only go up anyways)
        print('\n')
       
        #Just baselines mixed ANOVA
        print('Delta Power at Baseline between G+Y Mixed ANOVA')
        DFToPlot = deltaDF[deltaDF['sleepCondition'] == 'baseline']
        baselineANOVA = pg.mixed_anova(data=DFToPlot, dv='deltaPower', between='foodCondition', within='timeBin', subject='mouseNum', correction=True, effsize='np2')
        pg.print_table(baselineANOVA)
        print('\n')
        
        #Just recovery mixed ANOVA
        print('Delta Power at Recovery between G+Y Mixed ANOVA')
        DFToPlot = deltaDF[deltaDF['sleepCondition'] == 'recovery']
        recoveryANOVA = pg.mixed_anova(data=DFToPlot, dv='deltaPower', between='foodCondition', within='timeBin', subject='mouseNum', correction=True, effsize='np2')
        pg.print_table(recoveryANOVA)
        print('\n')
    
        
        #Green only 2 way RM ANOVA on Delta power
        print('Delta Power in Green Mice, Baseline vs Recovery, 2 Way RM ANOVA, within time and sleep condition')
        DFToPlot = deltaDF[deltaDF['foodCondition'] == 'green']
        yellowDeltaANOVA = pg.rm_anova(data=DFToPlot, dv='deltaPower', within=['timeBin', 'sleepCondition'], subject='mouseNum')
        pg.print_table(yellowDeltaANOVA)
        print('\n')
        
        #repeated measures 2 way ANOVA on deltaPower just in yellow mice
        print('Delta Power in Yellow Mice, Baseline vs Recovery, 2 Way RM ANOVA, within time and sleep condition')
        DFToPlot = deltaDF[deltaDF['foodCondition'] == 'yellow']
        yellowDeltaANOVA = pg.rm_anova(data=DFToPlot, dv='deltaPower', within=['timeBin', 'sleepCondition'], subject='mouseNum')
        pg.print_table(yellowDeltaANOVA)
        print('\n')




######### P L O T   S P E C T R U M S ################
if plotSpectrums and (not plotSpectrumsByBin):
    #non normalized power
    # fig,ax = plt.subplots()
    # DFToPlot = NREMFreqDF[NREMFreqDF['foodCondition'] == 'green']
    # sns.lineplot(data = DFToPlot, x = 'freq', y = 'power', hue = 'sleepCondition', palette=['darkgreen','limegreen'], ci=95)
    # DFToPlot = NREMFreqDF[NREMFreqDF['foodCondition'] == 'yellow']
    # sns.lineplot(data = DFToPlot, x = 'freq', y = 'power', hue = 'sleepCondition', palette=['darkgoldenrod','gold'], ci=95)
    # plt.title('Total NREM Spectrum Comparison')
    # every_nth = 8
    # for n, label in enumerate(ax.xaxis.get_ticklabels()):
    #     if n % every_nth != 0:
    #         label.set_visible(False)
    # plt.xticks(rotation=45, ha="right")
    
    #normalized power. 
    #Ie. for each mouse, each power value at each frequency is normalized to the FFT power averaged across all frequencies during NREM+Wake+REM
    #during whole 6 hour baseline recording for that mouse
    fig,ax = plt.subplots()
    DFToPlot = NREMFreqDF[NREMFreqDF['foodCondition'] == 'green']
    sns.lineplot(data = DFToPlot, x = 'freq', y = 'normPower', hue = 'sleepCondition', palette=['darkgreen','limegreen'], ci=95)
    DFToPlot = NREMFreqDF[NREMFreqDF['foodCondition'] == 'yellow']
    sns.lineplot(data = DFToPlot, x = 'freq', y = 'normPower', hue = 'sleepCondition', palette=['darkgoldenrod','gold'], ci=95)
    plt.title('Normalized NREM Spectrum Comparison')
    every_nth = 8
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    plt.xticks(rotation=45, ha="right")
    
    
    print('Mixed ANOVA Baseline between foodCondition') #is there difference in baselines
    DFToPlot = NREMFreqDF[NREMFreqDF['sleepCondition'] == 'baseline'] #select only recovery
    deltaANOVA = pg.mixed_anova(data=DFToPlot, dv='normPower', between='foodCondition', within='freq', subject='mouseNum', correction=True, effsize='np2')
    pg.print_table(deltaANOVA) #no main effect of food condition --> 0.665 uncorrected (nan corrected but doesn't matter because would only go up anyways)
    print('\n')
    
    
    print('Mixed ANOVA Recovery between foodCondition') #is there difference in recovery
    DFToPlot = NREMFreqDF[NREMFreqDF['sleepCondition'] == 'recovery'] #select only recovery
    deltaANOVA = pg.mixed_anova(data=DFToPlot, dv='normPower', between='foodCondition', within='freq', subject='mouseNum', correction=True, effsize='np2')
    pg.print_table(deltaANOVA) #no main effect of food condition --> 0.665 uncorrected (nan corrected but doesn't matter because would only go up anyways)
    print('\n')
    
    print('Two Way RM ANOVA Green between sleepCondition') #is there difference between baseline and recovery in green
    DFToPlot = NREMFreqDF[NREMFreqDF['foodCondition'] == 'green'] #select only recovery
    deltaANOVA = pg.rm_anova(data=DFToPlot, dv='normPower', within=['freq', 'sleepCondition'], subject='mouseNum')
    pg.print_table(deltaANOVA) #no main effect of food condition --> 0.665 uncorrected (nan corrected but doesn't matter because would only go up anyways)
    print('\n')
    
    print('Two Way RM ANOVA Yellow between sleepCondition') #is there difference in baseline and recovery in yellow
    DFToPlot = NREMFreqDF[NREMFreqDF['foodCondition'] == 'green'] #select only recovery
    deltaANOVA = pg.rm_anova(data=DFToPlot, dv='normPower', within=['freq', 'sleepCondition'], subject='mouseNum')
    pg.print_table(deltaANOVA) #no main effect of food condition --> 0.665 uncorrected (nan corrected but doesn't matter because would only go up anyways)
    print('\n')
    
    # pdb.set_trace()
    NREMFreqDF.to_csv('D:\VeaseyLabMaterialsJoe\sleepRecs\FreqNREMDF.csv')
    
    # pdb.set_trace()
    
    
if plotSpectrums and plotSpectrumsByBin:
    # #Green baseline normalized power
    fig,ax = plt.subplots()
    DFToPlot = NREMFreqDFTimeBins[(NREMFreqDFTimeBins.foodCondition == 'green') & (NREMFreqDFTimeBins.sleepCondition == 'baseline')]
    sns.lineplot(data = DFToPlot, x = 'freq', y = 'normPower', hue = 'timeBin', ci=95) #each bin frequency spectrum is normalized to 6 hour avg FFT during baseline
    plt.title('Green Baseline Normalized NREM Spectrum per TimeBin')
    every_nth = 8
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    plt.xticks(rotation=45, ha="right")
    
    #Green recovery normalized power
    fig,ax = plt.subplots()
    DFToPlot = NREMFreqDFTimeBins[(NREMFreqDFTimeBins.foodCondition == 'green') & (NREMFreqDFTimeBins.sleepCondition == 'recovery')]
    sns.lineplot(data = DFToPlot, x = 'freq', y = 'normPower', hue = 'timeBin', ci=95) #each bin frequency spectrum is normalized to 6 hour avg FFT during baseline
    plt.title('Green Recovery Normalized NREM Spectrum per TimeBin')
    every_nth = 8
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    plt.xticks(rotation=45, ha="right")
    
    #Yellow baseline normalized power
    fig,ax = plt.subplots()
    DFToPlot = NREMFreqDFTimeBins[(NREMFreqDFTimeBins.foodCondition == 'yellow') & (NREMFreqDFTimeBins.sleepCondition == 'baseline')]
    sns.lineplot(data = DFToPlot, x = 'freq', y = 'normPower', hue = 'timeBin', ci=95) #each bin frequency spectrum is normalized to 6 hour avg FFT during baseline
    plt.title('Yellow Baseline Normalized NREM Spectrum per TimeBin')
    every_nth = 8
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    plt.xticks(rotation=45, ha="right")
    
    #Green recovery normalized power
    fig,ax = plt.subplots()
    DFToPlot = NREMFreqDFTimeBins[(NREMFreqDFTimeBins.foodCondition == 'yellow') & (NREMFreqDFTimeBins.sleepCondition == 'recovery')]
    sns.lineplot(data = DFToPlot, x = 'freq', y = 'normPower', hue = 'timeBin', ci=95) #each bin frequency spectrum is normalized to 6 hour avg FFT during baseline
    plt.title('Yellow Recovery Normalized NREM Spectrum per TimeBin')
    every_nth = 8
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)
    plt.xticks(rotation=45, ha="right")
    
     
############## IMPORT STATS CSVs FROM conditions_stats_veasey and run TESTS ######################

runSleepStats = False

if runSleepStats:
    mouseStats_csvToLoad = r'D:\VeaseyLabMaterialsJoe\sleepRecs\mouseStats - 6 hours.csv'
    mouseStats6Hours = pd.read_csv(mouseStats_csvToLoad)
    
    mouseStats_csvToLoad = r'D:\VeaseyLabMaterialsJoe\sleepRecs\mouseStats - 3 hours.csv'
    mouseStats3Hours = pd.read_csv(mouseStats_csvToLoad)
    
    mouseStats_csvToLoad = r'D:\VeaseyLabMaterialsJoe\sleepRecs\mouseStats - 3 hoursANOVA.csv'
    mouseStats3HoursForANOVA = pd.read_csv(mouseStats_csvToLoad)
    
    

    # Unpaired Ttests on baseline 6 hour percentages
    print('###### Baseline ######')
    baselineDF = pd.DataFrame()
    baselineDFTemp = mouseStats6Hours[mouseStats6Hours.Condition == 'green baseline']
    baselineDF = baselineDF.append(baselineDFTemp)
    baselineDFTemp = mouseStats6Hours[mouseStats6Hours.Condition == 'yellow baseline']
    baselineDF = baselineDF.append(baselineDFTemp)
    for state in ['NREM','WAKE','REM']:
        stateDF = baselineDF[baselineDF['Brain State'] == state]
        # pdb.set_trace()
        greenDF = stateDF[stateDF.Condition == 'green baseline']
        yellowDF = stateDF[stateDF.Condition == 'yellow baseline']
        for stat in ['Percent','Duration','Frequency']:
            greenStat = greenDF[stat].tolist()
            yellowStat = yellowDF[stat].tolist()
            test1Normality = pg.normality(greenStat)
            test1Normality = test1Normality['normal'][0]
            test2Normality = pg.normality(yellowStat)
            test2Normality = test2Normality['normal'][0]
            if test1Normality and test2Normality:
                ttest = pg.ttest(greenStat,yellowStat,paired=False)
                print(state + ' ' + stat + ' Baseline Unpaired TTest')
                pg.print_table(ttest)
            else:
                ttest = pg.mwu(greenStat,yellowStat)
                print(state + ' ' + stat + ' Baseline MannWhitneyU Test')
                pg.print_table(ttest)
            
  
            
    print('\n')
    print('\n')
    print('###### RECOVERY ######')
    recoveryDF = pd.DataFrame()
    recoveryDFTemp = mouseStats3Hours[mouseStats3Hours.Condition == 'green recovery']
    recoveryDF = recoveryDF.append(recoveryDFTemp)
    recoveryDFTemp = mouseStats3Hours[mouseStats3Hours.Condition == 'yellow recovery']
    recoveryDF = recoveryDF.append(recoveryDFTemp)
    for state in ['NREM','WAKE','REM']:
        stateDF = recoveryDF[recoveryDF['Brain State'] == state]
        greenDF = stateDF[stateDF.Condition == 'green recovery']
        yellowDF = stateDF[stateDF.Condition == 'yellow recovery']
        for stat in ['Percent','Duration','Frequency']:
            greenStat = greenDF[stat].tolist()
            yellowStat = yellowDF[stat].tolist()
            test1Normality = pg.normality(greenStat)
            test1Normality = test1Normality['normal'][0]
            test2Normality = pg.normality(yellowStat)
            test2Normality = test2Normality['normal'][0]
            if test1Normality and test2Normality:
                ttest = pg.ttest(greenStat,yellowStat,paired=False)
                print(state + ' ' + stat + ' Baseline Unpaired TTest')
                pg.print_table(ttest)
            else:
                ttest = pg.mwu(greenStat,yellowStat)
                print(state + ' ' + stat + ' Baseline MannWhitneyU Test')
                pg.print_table(ttest)
        
    
    
    print('\n')
    print('\n')
    print('###### GREEN ######')
    greenDF = pd.DataFrame()
    greenDFTemp = mouseStats3Hours[mouseStats3Hours.Condition == 'green baseline']
    greenDF = greenDF.append(greenDFTemp)
    greenDFTemp = mouseStats3Hours[mouseStats3Hours.Condition == 'green recovery']
    greenDF = greenDF.append(greenDFTemp)
    for state in ['NREM','WAKE','REM']:
        stateDF = greenDF[greenDF['Brain State'] == state]
        # pdb.set_trace()
        baselineDF = stateDF[stateDF.Condition == 'green baseline']
        recoveryDF = stateDF[stateDF.Condition == 'green recovery']
        for stat in ['Percent','Duration','Frequency']:
            baselineStat = baselineDF[stat].tolist()
            recoveryStat = recoveryDF[stat].tolist()
            test1Normality = pg.normality(baselineStat)
            test1Normality = test1Normality['normal'][0]
            test2Normality = pg.normality(recoveryStat)
            test2Normality = test2Normality['normal'][0]
            if test1Normality and test2Normality:
                ttest = pg.ttest(baselineStat,recoveryStat,paired=True)
                print(state + ' ' + stat + ' Green Paired TTest')
                pg.print_table(ttest)
            else:
                ttest = pg.wilcoxon(x=greenStat,y=yellowStat)
                # ttest = pg.ttest(baselineStat,recoveryStat,paired=True)
                print(state + ' ' + stat + ' Green Wilcoxon Signed Rank Test')
                pg.print_table(ttest)
    
    
    
    print('\n')
    print('\n')
    print('###### YELLOW ######')
    yellowDF = pd.DataFrame()
    yellowDFTemp = mouseStats3Hours[mouseStats3Hours.Condition == 'yellow baseline']
    yellowDF = yellowDF.append(yellowDFTemp)
    yellowDFTemp = mouseStats3Hours[mouseStats3Hours.Condition == 'yellow recovery']
    yellowDF = yellowDF.append(yellowDFTemp)
    for state in ['NREM','WAKE','REM']:
        stateDF = yellowDF[yellowDF['Brain State'] == state]
        # pdb.set_trace()
        baselineDF = stateDF[stateDF.Condition == 'yellow baseline']
        recoveryDF = stateDF[stateDF.Condition == 'yellow recovery']
        for stat in ['Percent','Duration','Frequency']:
            baselineStat = baselineDF[stat].tolist()
            recoveryStat = recoveryDF[stat].tolist()
            test1Normality = pg.normality(baselineStat)
            test1Normality = test1Normality['normal'][0]
            test2Normality = pg.normality(recoveryStat)
            test2Normality = test2Normality['normal'][0]
            if test1Normality and test2Normality:
                ttest = pg.ttest(baselineStat,recoveryStat,paired=True)
                print(state + ' ' + stat + ' Yellow Paired TTest')
                pg.print_table(ttest)
            else:
                ttest = pg.wilcoxon(x=greenStat,y=yellowStat)
                print(state + ' ' + stat + ' Yellow Wilcoxon Signed Rank Test')
                pg.print_table(ttest)
    
    
    
    # pdb.set_trace()
    # Run ANOVAS and pairwise comparisons
    print('\n')
    print('NREM Percents Mixed ANOVA')
    NREMDF3Hours = mouseStats3HoursForANOVA[mouseStats3HoursForANOVA['Brain State'] == 'NREM']
    NREMPercANOVA = pg.mixed_anova(data=NREMDF3Hours, dv='Percent', between='Food Condition', within='Sleep Condition', subject='Name', correction=True, effsize='np2')
    pg.print_table(NREMPercANOVA)
    
    
    print('Pairwise ttests')
    NREMPairwiseTtests = pg.pairwise_ttests(data=NREMDF3Hours, dv='Percent', between='Food Condition', within='Sleep Condition', subject='Name',within_first=True,padjust='bonf',alpha=0.05)
    pg.print_table(NREMPairwiseTtests)
    
    
    
    
    
    
    
    


