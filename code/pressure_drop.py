def pDrop(): #% sums up all the pressure drops

    fluidDens = 493 #% fluid density (kg/m^3) - the 493 is for propane at standard liquid storage conditions
    grav = 9.81 #% acceleration due to gravity (m/s^2)
    fDarcy = .018 #% Darcy Friction Factor
    reynNum = 306900 #% Reynolds number
    totHeadDrop = 0 #%starts to account for the head drop of the system

    pipeLen = 50 #% Pipe length (m)
    nomDiam = 4 #% Pipe outer diameter (in)
    innerDiam = .1023 #% Pipe inner diameter (m)
    avgVel = 3 #% average velocity (m/s)

    #% values for the fitting, 
    #% might need more of these if you have several different fittings
    #% k values format kValues = (k1, kinf, kd (in mm^0.3, not inches))
    kValues = [800, 0.056, 3.9]

    #% find straight pipe head drop, you can count all the different
    #% sections of straight pipe as one pipe that is the total length
    updateHeadDrop = sDrop(grav, fDarcy, pipeLen, innerDiam, avgVel)
    totHeadDrop = totHeadDrop + updateHeadDrop #%updates head drop

    #% find fitting head drop, you need one loop for each fitting type
    #% make sure each one has the correct set of k values

    #% Fitting type one, there's three of these
    for counter1 in range(3):
        updateHeadDrop = fDrop(kValues, reynNum, nomDiam, avgVel, grav)
        totHeadDrop = totHeadDrop + updateHeadDrop
    
    #% There are no other fitting types in this example, but if there were
    #% their respective loops would go below

    pressureDrop = fluidDens * grav * totHeadDrop #% convert head drop to pressure, answer is in pascals

    #% Converts to other units if desired, just uncomment the correct line of code
    #% pressureDrop = pressureDrop / 1000 #% Answer in KPA
    #% pressureDrop = pressureDrop / 101325 #% Answer in Atmospheres
    #% pressureDrop = pressureDrop / 133.3 #% Answer in torr (mmHg)
    pressureDrop = pressureDrop / 6895.76 #% Answer in PSI

    finalP = pressureDrop
    print(f'{finalP:.4f}')
    



#% Use Darcy-Weisbach equation for straight pipe head loss
def sDrop(grav, fDarcy, pipeLen, innerDiam, avgVel):
    straightDrop = fDarcy * (pipeLen / innerDiam) * ((avgVel ** 2) / (2 * grav))
    return straightDrop




#% Use 3K method to find fitting head loss
def fDrop(kValues, reynNum, nomDiam, avgVel, grav):
    #% Get the 3 k values out of the list
    k1 = kValues[0]
    kinf = kValues[1]
    kd = kValues[2]

    #% Do the math
    bigK = (k1 / reynNum) + kinf * (1 + (kd / (nomDiam ** 0.3)))
    fittingDrop = bigK * ((avgVel * avgVel) / (2 * grav))
    return fittingDrop

pDrop()

