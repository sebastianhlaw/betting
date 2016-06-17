__author__ = 'Sebastian.Law'

import historical_stripper
import datetime
import pandas as pd

# frame = pd.DataFrame(columns=['date','homeTeam','awayTeam','homeScore','awayScore','homeOdds','drawOdds','awayOdds'])
frame = historical_stripper.stripper("dummy_url")

years = int(2)
urls = int(years*8)

urlFull = [];
for year in range(2012,2012+years):
    urlStart = "http://www.oddsportal.com/soccer/england/premier-league-"+str(year)+"-"+str(year+1)+"/results/"
    for page in range(1,8):
        if page != 1:
            urlFull.append( urlStart + "page/" + str(page) + "/")
    urlFull.append( urlStart )

print(urlFull)