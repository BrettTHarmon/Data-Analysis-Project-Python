#Brett Harmon
#Data Analysis Project

import csv


#Organizes the data by putting each row into a different list and returns that data
def read_stats(reader):
    list=[]
    for row in reader:
        list.append(row)
    return list


#Lowest ERA in baseball in the 7th inning or later for the 2014 season
def minimum_ERA(list):
    index=0
    saved_index=0
    min=list[0]
    while index<len(list):
        if min>=list[index]:
            saved_index=index
            min=list[index]
        index+=1
    #print("The minimum earned run average in the 7th inning or later during the 2014 season was",min())
    return(saved_index)
#print("The team with the lowest ERA was",Team_Names[minimum_ERA(Earned_Run_Averages)])




#Maximum Number of Strikeouts for the 7th inning or later for the 2014 season
def maximum_strikeouts(list):
    index=0
    saved_index=0
    max=list[0]
    while index<len(list):
        if max<=list[index]:
            saved_index=index
            max=list[index]
        index+=1
    #print("The maximum number of strikeouts in the 7th inning or later during the 2014 season was",max())
    return(saved_index)
#print("The team with the highest number of strikeouts was the",Team_Names[maximum_strikeouts(Strikeouts)])

#Median number of Earned Runs given up by each of the 30 teams in Major League Baseball during the 2014 season
def median_EarnedRuns(list):
    sort=(sorted(list))
    a=eval(sort[(len(sort)//2)])
    i=eval(sort[len(sort)//2-1])
    return(a+i)//2
#print("The median number of earned runs in the 7th inning or later during the 2014 season was",(median_EarnedRuns(Earned_Runs)))

#Minimum Opponents' Batting Average in the 7th inning or later during the 2014 season
def minimum_batting_average(list):
    index=0
    saved_index=0
    min=list[0]
    while index<len(list):
        if min>=list[index]:
            saved_index=index
            min=list[index]
        index+=1
    #print("The lowest opponents' batting average in the 7th inning or later during the 2014 season was",min())
    return(saved_index)
#print("The team with the lowest opponents' batting average was",Team_Names[(minimum_batting_average(Opponents_Batting_Average))])

def main():
    #This function is taking 2014 MLB Data measuring each of the 30 teams' bullpen during the 7th inning or later
    f= open("2014 MLB Data For Python Project")
    reader = csv.reader(f)
    list=read_stats(reader)

    #Team Names Loop
    Team_Names =[]
    for x in list:
        Team_Names.append(x[1])
    print(Team_Names)

    #Earned Run Averages Loop
    Earned_Run_Averages = []
    for s in list:
        Earned_Run_Averages.append(s[2])
    print(Earned_Run_Averages)

    #Earned Runs Loop
    Earned_Runs = []
    for j in list:
        Earned_Runs.append(j[3])
    print(Earned_Runs)

    #Strikeouts Loop
    Strikeouts = []
    for k in list:
        Strikeouts.append(k[4])
    print(Strikeouts)

    #Batting Average Loop
    Opponents_Batting_Average = []
    for a in list:
        Opponents_Batting_Average.append(a[5])
    print(Opponents_Batting_Average)

    print("The minimum earned run average in the 7th inning or later during the 2014 season was",min(Earned_Run_Averages))
    print("The team with the lowest ERA was",Team_Names[minimum_ERA(Earned_Run_Averages)])

    print("The maximum number of strikeouts in the 7th inning or later during the 2014 season was",max(Strikeouts))
    print("The team with the highest number of strikeouts was the",Team_Names[maximum_strikeouts(Strikeouts)])


    print("The median number of earned runs in the 7th inning or later during the 2014 season was",(median_EarnedRuns(Earned_Runs)))

    print("The lowest opponents' batting average in the 7th inning or later during the 2014 season was",min(Opponents_Batting_Average))
    print("The team with the lowest opponents' batting average was",Team_Names[(minimum_batting_average(Opponents_Batting_Average))])
main()

