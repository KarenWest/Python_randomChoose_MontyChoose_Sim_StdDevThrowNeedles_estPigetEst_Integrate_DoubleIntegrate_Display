Hashing Example:

 import random



def strToInt(s):

    number = ''

    for c in s:

        number = number + str(ord(c))

    index = int(number)

    return index



#print 'Index =', strToInt('a')

#print 'Index =', strToInt('John is a cool dude')


Dictionary With Integer Keys:

import random





class intDict(object):

    """A dictionary with integer keys"""

    

    def __init__(self, numBuckets):

        """Create an empty dictionary"""

        self.buckets = []

        self.numBuckets = numBuckets

        for i in range(numBuckets):

            self.buckets.append([])

            

    def addEntry(self, dictKey, dictVal):

        """Assumes dictKey an int.  Adds an entry."""

        hashBucket = self.buckets[dictKey%self.numBuckets]

        for i in range(len(hashBucket)):

            if hashBucket[i][0] == dictKey:

                hashBucket[i] = (dictKey, dictVal)

                return

        hashBucket.append((dictKey, dictVal))

        

    def getValue(self, dictKey):

        """Assumes dictKey an int.  Returns entry associated

           with the key dictKey"""

        hashBucket = self.buckets[dictKey%self.numBuckets]

        for e in hashBucket:

            if e[0] == dictKey:

                return e[1]

        return None

    

    def __str__(self):

        res = '{'

        for b in self.buckets:

            for t in b:

                res = res + str(t[0]) + ':' + str(t[1]) + ','

        return res[:-1] + '}' #res[:-1] removes the last comma





D = intDict(29)

for i in range(20):

    #choose a random int in range(10**5)

    key = random.choice(range(10**5))

    D.addEntry(key, i)



print '\n', 'The buckets are:'

for hashBucket in D.buckets: #violates abstraction barrier

    print '  ', hashBucket


Monte Carlo Simulations:

import random



def rollDie():

    """returns a random int between 1 and 6"""

    return random.choice([1,2,3,4,5,6])



def checkPascal(numTrials, roll):

    yes = 0.0

    for i in range(numTrials):

        for j in range(24):

            d1 = roll()

            d2 = roll()

            if d1 == 6 and d2 == 6:

                yes += 1

                break

    print 'Probability of losing =', 1.0 - yes/numTrials



##checkPascal(10000, rollDie)


Some Plotting code:

import random, pylab

#set line width

pylab.rcParams['lines.linewidth'] = 6

#set font size for titles 

pylab.rcParams['axes.titlesize'] = 20

#set font size for labels on axes

pylab.rcParams['axes.labelsize'] = 20

#set size of numbers on x-axis

pylab.rcParams['xtick.major.size'] = 5

#set size of numbers on y-axis

pylab.rcParams['ytick.major.size'] = 5















def stdDev(X):

    mean = sum(X)/float(len(X))

    tot = 0.0

    for x in X:

        tot += (x - mean)**2

    return (tot/len(X))**0.5





def runTrial(numFlips):

    numHeads = 0

    for n in range(numFlips):

        if random.random() < 0.5:

            numHeads += 1

    numTails = numFlips - numHeads

    return numHeads, numTails



def flipPlot(minExp, maxExp, numTrials):

    meanRatios = []

    meanDiffs = []

    ratiosSDs =  []

    diffsSDs =  []

    xAxis = []

    for exp in range(minExp, maxExp + 1):

        xAxis.append(2**exp)

    for numFlips in xAxis:

        ratios = []

        diffs = []

        for t in range(numTrials):

            numHeads, numTails = runTrial(numFlips)

            ratios.append(numHeads/float(numTails))

            diffs.append(abs(numHeads - numTails))

        meanRatios.append(sum(ratios)/numTrials)

        meanDiffs.append(sum(diffs)/numTrials)

        ratiosSDs.append(stdDev(ratios))

        diffsSDs.append(stdDev(diffs))

    pylab.plot(xAxis, meanRatios, 'bo')

    pylab.title('Mean Heads/Tails Ratios ('

                + str(numTrials) + ' Trials)')

    pylab.xlabel('Number of Flips')

    pylab.ylabel('Mean Heads/Tails')

    pylab.semilogx()

    pylab.figure()

    pylab.plot(xAxis, ratiosSDs, 'bo')

    pylab.title('SD Heads/Tails Ratios ('

                + str(numTrials) + ' Trials)')

    pylab.xlabel('Number of Flips')

    pylab.ylabel('Standard Deviation')

    pylab.semilogx()

    pylab.semilogy()



##flipPlot(4, 20, 20)

##pylab.show()







def flipPlot2(minExp, maxExp, numTrials):

    meanRatios = []

    meanDiffs = []

    ratiosSDs =  []

    diffsSDs =  []

    xAxis = []

    for exp in range(minExp, maxExp + 1):

        xAxis.append(2**exp)

    for numFlips in xAxis:

        ratios = []

        diffs = []

        for t in range(numTrials):

            numHeads, numTails = runTrial(numFlips)

            ratios.append(numHeads/float(numTails))

            diffs.append(abs(numHeads - numTails))

        meanRatios.append(sum(ratios)/numTrials)

        meanDiffs.append(sum(diffs)/numTrials)

        ratiosSDs.append(stdDev(ratios))

        diffsSDs.append(stdDev(diffs))

    pylab.plot(xAxis, meanRatios, 'bo')

    pylab.title('Mean Heads/Tails Ratios ('

                + str(numTrials) + ' Trials)')

    pylab.xlabel('Number of Flips')

    pylab.ylabel('Mean Heads/Tails')

    pylab.semilogx()

    pylab.figure()

    pylab.plot(xAxis, ratiosSDs, 'bo')

    pylab.title('SD Heads/Tails Ratios ('

                + str(numTrials) + ' Trials)')

    pylab.xlabel('Number of Flips')

    pylab.ylabel('Standard Deviation')

    pylab.semilogx()

    pylab.semilogy()

    #Additional code to look at difference in abolute

    #number of heads and tails

    pylab.figure()

    pylab.title('Mean abs(#Heads - #Tails) ('

                + str(numTrials) + ' Trials)')

    pylab.xlabel('Number of Flips')

    pylab.ylabel('Mean abs(#Heads - #Tails')

    pylab.plot(xAxis, meanDiffs, 'bo')

    pylab.semilogx()

    pylab.semilogy()

    pylab.figure()

    pylab.plot(xAxis, diffsSDs, 'bo')

    pylab.title('SD abs(#Heads - #Tails) ('

                + str(numTrials) + ' Trials)')

    pylab.xlabel('Number of Flips')

    pylab.ylabel('Standard Deviation')

    pylab.semilogx()

    pylab.semilogy()



##flipPlot2(4, 20, 20)

##pylab.show()




Normal Distributions Code:

import random, pylab



#set line width

pylab.rcParams['lines.linewidth'] = 6

#set font size for titles 

pylab.rcParams['axes.titlesize'] = 20

#set font size for labels on axes

pylab.rcParams['axes.labelsize'] = 20

#set size of numbers on x-axis

pylab.rcParams['xtick.major.size'] = 5

#set size of numbers on y-axis

pylab.rcParams['ytick.major.size'] = 5







##def makeNormal(mean, sd, numSamples):

##    samples = []

##    for i in range(numSamples):

##        samples.append(random.gauss(mean, sd))

##    pylab.hist(samples, bins = 101)

##

##makeNormal(0, 1.0, 100000)

##pylab.show()











def clear(n, clearProb, steps):

    numRemaining = [n]

    for t in range(steps):

        numRemaining.append(n*((1-clearProb)**t))

    pylab.plot(numRemaining, label = 'Exponential Decay')



##clear(1000, 0.01, 500)

##pylab.xlabel('Number of Steps')

##pylab.ylabel('Number of Molecules')

##pylab.show()





def clearSim(n, clearProb, steps):

    numRemaining = [n]

    for t in range(steps):

        numLeft = numRemaining[-1]

        for m in range(numRemaining[-1]):

            if random.random() <= clearProb: 

                numLeft -= 1

        numRemaining.append(numLeft)

    pylab.plot(numRemaining, 'ro', label = 'Simulation')



clear(10000, 0.01, 1000)

clearSim(10000, 0.01, 1000)

pylab.xlabel('Number of Steps')

pylab.ylabel('Number of Molecules')

pylab.legend()

pylab.show()

SimMontyHall Code:

import random, pylab



#set line width

pylab.rcParams['lines.linewidth'] = 6

#set font size for titles 

pylab.rcParams['axes.titlesize'] = 20

#set font size for labels on axes

pylab.rcParams['axes.labelsize'] = 20

#set size of numbers on x-axis

pylab.rcParams['xtick.major.size'] = 5

#set size of numbers on y-axis

pylab.rcParams['ytick.major.size'] = 5

#set font size for text

pylab.rcParams['legend.fontsize'] = 20







def montyChoose(guessDoor, prizeDoor):

    if 1 != guessDoor and 1 != prizeDoor:

        return 1

    if 2 != guessDoor and 2 != prizeDoor:

        return 2

    return 3



def randomChoose(guessDoor, prizeDoor):

    if guessDoor == 1:

        return random.choice([2,3])

    if guessDoor == 2:

        return random.choice([1,3])

    return random.choice([1,2])

    

def simMontyHall(numTrials, chooseFcn):

    stickWins, switchWins, noWin = (0, 0, 0)

    prizeDoorChoices = [1,2,3]

    guessChoices = [1,2,3]

    for t in range(numTrials):

        prizeDoor = random.choice([1, 2, 3])

        guess = random.choice([1, 2, 3])

        toOpen = chooseFcn(guess, prizeDoor)

        if toOpen == prizeDoor:

            noWin += 1

        elif guess == prizeDoor:

            stickWins += 1

        else:

            switchWins += 1

    return (stickWins, switchWins)



def displayMHSim(simResults, title):

    stickWins, switchWins = simResults

    pylab.pie([stickWins, switchWins],

              colors = ['r', 'c'],

              labels = ['stick', 'change'],

              autopct = '%.2f%%')

    pylab.title(title)



simResults = simMontyHall(100000, montyChoose)

displayMHSim(simResults, 'Monty Chooses a Door')

pylab.figure()

simResults = simMontyHall(100000, randomChoose)

displayMHSim(simResults, 'Door Chosen at Random')

pylab.show()





































def stdDev(X):

    mean = sum(X)/float(len(X))

    tot = 0.0

    for x in X:

        tot += (x - mean)**2

    return (tot/len(X))**0.5



def throwNeedles(numNeedles):

    inCircle = 0

    estimates = []

    for Needles in xrange(1, numNeedles + 1, 1):

        x = random.random()

        y = random.random()

        if (x*x + y*y)**0.5 <= 1.0:

            inCircle += 1

    return 2*(inCircle/float(Needles))



def estPi(precision = 0.01, numTrials = 20):

    numNeedles = 1000

#    numTrials = 20

    sDev = precision

    while sDev >= (precision/4.0):

        estimates = []

        for t in range(numTrials):

            piGuess = throwNeedles(numNeedles)

            estimates.append(piGuess)

        sDev = stdDev(estimates)

        curEst = sum(estimates)/len(estimates) 

        curEst = sum(estimates)/len(estimates)

        print 'Est. = ' + str(curEst) +\

              ', Std. dev. = ' + str(sDev)\

              + ', Needles = ' + str(numNeedles)

        numNeedles *= 2

    return curEst



##estPi()



def integrate(a, b, f, numPins):

    pinSum = 0.0

    for pin in range(numPins):

        pinSum += f(random.uniform(a, b))

    average = pinSum/numPins

    return average*(b - a)



def one(x):

    return 1.0



##print integrate(0, 8, one, 100000)

##4 + 3

##import math

##print integrate(0, 8, math.sin, 1000000)



def doubleIntegrate(a, b, c, d, f, numPins):

    pinSum = 0.0

    for pin in range(numPins):

        x = random.uniform(a, b)

        y = random.uniform(c, d)

        pinSum += f(x, y)

    average = pinSum/numPins

    return average*(b - a)*(d - c)



def f(x, y):

    return 4 - x**2 - y**2



##print doubleIntegrate(0, 1.25, 0, 1.25, f, 100000)

Est Pi Code:

import random, pylab



#set line width

pylab.rcParams['lines.linewidth'] = 6

#set font size for titles 

pylab.rcParams['axes.titlesize'] = 20

#set font size for labels on axes

pylab.rcParams['axes.labelsize'] = 20

#set size of numbers on x-axis

pylab.rcParams['xtick.major.size'] = 5

#set size of numbers on y-axis

pylab.rcParams['ytick.major.size'] = 5

#set font size for text

pylab.rcParams['legend.fontsize'] = 20



def stdDev(X):

    mean = sum(X)/float(len(X))

    tot = 0.0

    for x in X:

        tot += (x - mean)**2

    return (tot/len(X))**0.5



def throwNeedles(numNeedles):

    inCircle = 0

    for Needles in xrange(1, numNeedles + 1, 1):

        x = random.random()

        y = random.random()

        if (x*x + y*y)**0.5 <= 1.0:

            inCircle += 1

    return 4*(inCircle/float(numNeedles))



def getEst(numNeedles, numTrials):

    estimates = []

    for t in range(numTrials):

        piGuess = throwNeedles(numNeedles)

        estimates.append(piGuess)

    sDev = stdDev(estimates)

    curEst = sum(estimates)/len(estimates)

    print 'Est. = ' + str(curEst) +\

          ', Std. dev. = ' + str(round(sDev, 6))\

          + ', Needles = ' + str(numNeedles)

    return (curEst, sDev)



def estPi(precision, numTrials):

    numNeedles = 1000

    sDev = precision

    while sDev >= precision/2.0:

        curEst, sDev = getEst(numNeedles, numTrials)

        numNeedles *= 2

    return curEst



random.seed(0)

estPi(0.005, 100)




