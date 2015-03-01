#!/usr/bin/python

import datetime, urllib, lxml.html, re

##response = urllib.request.urlopen('http://python.org/')
##html = response.read()
local = open("C:/Users/Sebastian.Law/Google Drive/Python/Betting/test.htm")
html = local.read()
doc = lxml.html.fromstring(html)

fixtures = doc.xpath("//table[@id='tournamentTable']")[0]
rows = fixtures.xpath('tbody/tr')
home, away = None, None
for row in rows:
    if('deactivate' in row.attrib["class"]):
        home = row.xpath("td[@class='name table-participant']/a")[0].text
        if row.xpath("td[@class='name table-participant']/a/span"):
            away = row.xpath("td[@class='name table-participant']/a/span")[0].text
##         = teams[0].text
##        away = teams.xpath("span")[0].text
##            away = teams.xpath("span")[0].text
           
##        spans = row.xpath("span[@class='bold']")[0].text
##        spans = row.xpath("td[@class='name table-participant']/a/span")[0].text
        score = row.xpath("td[@class='center bold table-odds table-score']")[0].text
##        oddsH = row.xpath("td[@class='center bold table-odds table-score']")[0].text
##        oddsD = row.xpath("td[@class='center bold table-odds table-score']")[0].text
##        oddsA = row.xpath("td[@class='center bold table-odds table-score']")[0].text
        print(home, away, score)
        home, away = None, None

##def readFile(url):
##    fileObject = open(filename)
##    doc=lxml.html.fromstring(fileObject.read())
##    doc=lxml.html.fromstring(urllib.urlopen2(url).read())
##    fixtures=doc.xpath("//div[@id='fixtures']")[0]
##    rows=fixtures.xpath("div/table/tbody/tr")
##    events, date = [], None
##    for row in rows:
##        if ("class" in row.attrib and "date" in row.attrib["class"]):
##            date=row.xpath("td[@class='day']/p")[0].text
##        else:
##            time=row.xpath("td[@class='time']/p")[0].text
##            spans=row.xpath("td/p/span[@class='add-to-bet-basket']")
##            hometeam, awayteam = (spans[0].attrib["data-name"], 
##                                  spans[2].attrib["data-name"])
##            link=row.xpath("td[@class='betting']/a")[0].attrib["href"]
##            event={"kickoff": parse_kickoff("%s %s" % (date, time)),
##                   "name": "%s vs %s" % (hometeam, awayteam),
##                   "link": link}
##            events.append(event)
##    return "finished"

 
##MatchEvents=get_match_events("http://www.oddschecker.com/football/english/premier-league")
##MatchEvents=get_match_events("test.htm")

##print(readFile("file:///C:/Users/Sebastian.Law/Google%20Drive/Python/Betting/test.htm"))

##def parse_kickoff(text):
##    tokens=[tok for tok in re.split("\\s|\\:", text)
##            if tok!='']
##    year=int(tokens[3])
##    month=Months.index(tokens[2])+1
##    day=int(tokens[1][:-2])
##    hour=int(tokens[-2])
##    minute=int(tokens[-1])
##    return datetime.datetime(*[year, month, day, hour, minute])
