from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def get_scraped_stats(url):
    uClient = uReq(url)
    pageHtml = uClient.read()
    uClient.close()
    pageSoup = soup(pageHtml, "html.parser")

    season = pageSoup.find("tr",{"id":"per_game.2018"})
    games = season.find("td",{"data-stat":"g"})
    gamesStarted = season.find("td",{"data-stat":"gs"})
    avgMinutes = season.find("td",{"data-stat":"mp_per_g"})
    avgFgm = season.find("td",{"data-stat":"fg_per_g"})
    avgFga = season.find("td",{"data-stat":"fga_per_g"})
    fieldGoalPercentage = season.find("td",{"data-stat":"fg_pct"})
    avgTpm = season.find("td",{"data-stat":"fg3_per_g"})
    avgTpa = season.find("td",{"data-stat":"fg3a_per_g"})
    threePointPercentage = season.find("td",{"data-stat":"fg3_pct"})
    avgTwoPointersMade = season.find("td",{"data-stat":"fg2_per_g"})
    avgTwoPointersAttempted = season.find("td",{"data-stat":"fg2a_per_g"})
    twoPointPercentage = season.find("td",{"data-stat":"fg2_pct"})
    effectiveFieldGoalPercentage = season.find("td",{"data-stat":"efg_pct"})
    avgFreeThrowsMade = season.find("td",{"data-stat":"ft_per_g"})
    avgFreeThrowsAttempted = season.find("td",{"data-stat":"fta_per_g"})
    freeThrowPercentage = season.find("td",{"data-stat":"ft_pct"})
    avgOffensiveRebounds = season.find("td",{"data-stat":"orb_per_g"})
    avgDefensiveRebounds = season.find("td",{"data-stat":"drb_per_g"})
    avgTotalRebounds = season.find("td",{"data-stat":"trb_per_g"})
    avgAst =season.find("td",{"data-stat":"ast_per_g"})
    avgStl = season.find("td",{"data-stat":"stl_per_g"})
    avgBlk = season.find("td",{"data-stat":"blk_per_g"})
    avgTov = season.find("td",{"data-stat":"tov_per_g"})
    avgPf = season.find("td",{"data-stat":"pf_per_g"})
    avgPts = season.find("td",{"data-stat":"pts_per_g"})


    seasonAvgs = {'games': games.text,'gamesStarted': gamesStarted.text, 'avgMinutes': avgMinutes.text,
                'avgFgm': avgFgm.text, 'avgFga': avgFga.text, 'fieldGoalPercentage': fieldGoalPercentage.text,
                'avgTpm': avgTpm.text, 'avgTpa': avgTpa.text, 'threePointPercentage': threePointPercentage.text,
                'avgTwoPointersMade': avgTwoPointersMade.text, 'avgTwoPointersAttempted': avgTwoPointersAttempted.text,
                'twoPointPercentage': twoPointPercentage.text, 'effectiveFieldGoalPercentage': effectiveFieldGoalPercentage.text,
                'avgFreeThrowsMade': avgFreeThrowsMade.text, 'avgFreeThrowsAttempted': avgFreeThrowsAttempted.text,
                'freeThrowPercentage': freeThrowPercentage.text, 'avgOffensiveRebounds': avgOffensiveRebounds.text,
                'avgDefensiveRebounds': avgDefensiveRebounds.text, 'avgTotalRebounds': avgTotalRebounds.text, 'avgAst': avgAst.text, 'avgStl': avgStl.text,
                'avgBlk': avgBlk.text, 'avgTov': avgTov.text, 'avgPf': avgPf.text, 'avgPts': avgPts.text}

    return seasonAvgs
