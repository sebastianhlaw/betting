__author__ = 'Sebastian.Law'

import lxml.html, lxml.etree
import datetime
import pandas as pd

def stripper(urlTarget):

    # response = urllib.request.urlopen('http://python.org/')
    # html = response.read()
    # local = open("C:/Users/Sebastian.Law/Google Drive/Python/Betting/test.htm")
    # html = local.read()

    # import render
    # urlDirty = './source/test.htm'
    # r = render.Render(urlDirty)
    # html = r.frame.toHtml()
    urlCleaned = './source/testx.htm'
    local = open(urlCleaned)
    html = local.read()
    doc = lxml.html.fromstring(html)

    frame = pd.DataFrame(columns=['date','homeTeam','awayTeam','homeScore','awayScore','homeOdds','drawOdds','awayOdds'])
    fixtures = doc.xpath("//table[@id='tournamentTable']")[0]
    rows = fixtures.xpath('tbody/tr')
    i = 0
    for row in rows:
        # date
        if "center nob-border" in row.attrib["class"]:
            matchday = row.xpath("th")[0].xpath("span")[0].text
            matchdate = datetime.datetime.strptime(matchday,"%d %b %Y").date()
        if 'deactivate' in row.attrib["class"]:
            # teams
            home, away = None, None
            check = row.xpath("td[@class='name table-participant']/a")
            if not check[0].text: # home wins
                if row.xpath("td[@class='name table-participant']/a/span"):
                    check2 = row.xpath("td[@class='name table-participant']/a/span")
                    home = check2[0].text
                    away = check2[0].tail
            else: # home loses or a draw
                home = check[0].text
                away = ""
                if row.xpath("td[@class='name table-participant']/a/span"):
                    check2 = row.xpath("td[@class='name table-participant']/a/span")
                    away = check2[0].text
            match = home + away
            teams = match.split("-")
            for team in teams:
                team.strip()
            # scores
            score = row.xpath("td[@class='center bold table-odds table-score']")[0].text
            scores = score.split(":")
            # odds
            odds = [''] * 3
            for col in range(3):
                odds[col] = row.xpath("td")[col+3].xpath("a")[0].text
            # results
            # print(teams[0], teams[1], scores[0], scores[1], odds[0], odds[1], odds[2])
            frame.loc[i] = [matchdate, teams[0], teams[1], scores[0], scores[1], odds[0], odds[1], odds[2]]
            i = i+1
    # print(frame)
    return frame
