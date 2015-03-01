#!/usr/bin/python

import datetime, lxml.html, re, urllib

MontMonths=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def parse_kickoff(text):
    tokens=[tok for tok in re.split("\\s|\\:", text)
            if tok!='']
    year=int(tokens[3])
    month=Months.index(tokens[2])+1
    day=int(tokens[1][:-2])
    hour=int(tokens[-2])
    minute=int(tokens[-1])
    return datetime.datetime(*[year, month, day, hour, minute])

def get_match_events(url):
    doc=lxml.html.fromstring(urllib.urlopen(url).read())
    fixtures=doc.xpath("//div[@id='fixtures']")[0]
    rows=fixtures.xpath("div/table/tbody/tr")
    events, date = [], None
    for row in rows:
        if ("class" in row.attrib and
            "date" in row.attrib["class"]):
            date=row.xpath("td[@class='day']/p")[0].text
        else:
            time=row.xpath("td[@class='time']/p")[0].text
            spans=row.xpath("td/p/span[@class='add-to-bet-basket']")
            hometeam, awayteam = (spans[0].attrib["data-name"], 
                                  spans[2].attrib["data-name"])
            link=row.xpath("td[@class='betting']/a")[0].attrib["href"]
            event={"kickoff": parse_kickoff("%s %s" % (date, time)),
                   "name": "%s vs %s" % (hometeam, awayteam),
                   "link": link}
            events.append(event)
    return events

MatchEvents=get_match_events("http://www.oddschecker.com/football/english/premier-league")

##print "%i events found" % len(MatchEvents)hs=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
