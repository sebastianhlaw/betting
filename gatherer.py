__author__ = 'Sebastian.Law'

import stripper
import datetime
import pandas as pd

# frame = pd.DataFrame(columns=['date','homeTeam','awayTeam','homeScore','awayScore','homeOdds','drawOdds','awayOdds'])
# stripper.stripper("hello world")

baseString = "http://www.oddsportal.com/soccer/england/premier-league-"

years = int(2)
urls = int(years*8)

urlFull = [];
for year in range(2012,2012+years):
    urlStart = "http://www.oddsportal.com/soccer/england/premier-league-"+str(year)+"-"+str(year+1)+"/results/"
    for page in range(8,1,-1):
        if page != 1:
            urlFull.append( urlStart + "page/" + str(page) + "/")
    urlFull.append( urlStart )

print(urlFull)