
"""
This is the class for the iridescent calculator.
This class gathers the user's current level,
current amount of iridescent shards, 
their current xp(unless xpon is set to false,
in which case, this would default to 0), and the 
amount of iridescent shards the user is trying to
save up for. This calculator only takes getting
iridescent shard through xp into account, this 
cannot be used with rewards given through the shop
or through the Tome because those cannot be individually tracked.
"""
class iridescentCalc():

    lvlneeded = 0
    irileft = 0
    xpneeded = 0

    def __init__(self,curlvl, curiri, curxp, irineeded, xpon):
        self.curlvl = curlvl
        self.curiri = curiri
        self.irineeded = irineeded
        if(xpon):
            self.curxp = curxp
        else: self.curxp = 0
        self.xpon = xpon


    """
    This calculator uses the players current level,
    current iridescent shard count, and current xp count
    and calculates how many levels it would take to get the 
    item the player wants. This calculator would also 
    calculate how many iridescent shards would be left over
    and the amount of xp needed based on the initial xp given.
    """
    def CalculateLvl(self):
        tempcurlvl = self.curlvl
        tempcuriri = self.curiri
        templvlneeded = 0
        iriamt = int
        xp = int
        tempxpneeded = self.xpneeded
        while(tempcuriri < self.irineeded):
            iriamt = 0
            xp = 0
            
            if tempcurlvl == 1:
                iriamt = 50
                xp = 720
            elif tempcurlvl == 2:
                iriamt = 65
                xp = 900
            elif (tempcurlvl >= 3 and tempcurlvl < 6) :
                iriamt = 85
                xp = 1200
            elif(tempcurlvl >= 6 and tempcurlvl < 14):
                iriamt = 150
                xp = 2100
            elif tempcurlvl >= 14 and tempcurlvl < 24:
                iriamt = 195
                xp = 2700
            elif tempcurlvl >= 24 and tempcurlvl < 34:
                iriamt = 235
                xp = 3300
            elif tempcurlvl >= 34 and tempcurlvl < 49:
                iriamt = 270
                xp = 3750
            elif tempcurlvl >= 49:
                iriamt = 300
                xp = 4200
            # print("current lvl = " + str(tempcurlvl))
            if self.xpon : tempxpneeded += xp
            tempcuriri += iriamt
            if(tempcurlvl < 99):
                tempcurlvl += 1
            else:
                tempcurlvl = 1
            templvlneeded += 1
            # print("updated lvl = " + str(tempcurlvl))
            # print("current lvl needed = " + str(templvlneeded))
            # if self.xpon:
            #     print("current xp needed = " + str(tempxpneeded))
        
        self.irileft = tempcuriri - self.irineeded
        if(self.xpon):
            tempxpneeded -= self.curxp
            self.xpneeded = tempxpneeded
        return templvlneeded
    
    def getXP(self):
        return self.xpneeded
    
    def getIriLeft(self):
        return self.irileft
            

# calc1 = iridescentCalc(42,300,150,500,False)
# print("Levels needed to get needed Iridescent Shards = " + str(calc1.CalculateLvl()))
# print("Iridescent Shards left over " + str(calc1.irileft))
# if(calc1.xpon): print("XP needed for iridescent shards " + str(calc1.xpneeded))
