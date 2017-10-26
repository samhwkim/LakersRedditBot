def get_stats_table(stats):
    """
    seasonAvgs = {'games': games.text,'gamesStarted': gamesStarted.text, 'avgMinutes': avgMinutes.text,
                'avgFgm': avgFgm.text, 'avgFga': avgFga.text, 'fieldGoalPercentage': fieldGoalPercentage.text,
                'avgTpm': avgTpm.text, 'avgTpa': avgTpa.text, 'threePointPercentage': threePointPercentage.text,
                'avgTwoPointersMade': avgTwoPointersMade.text, 'avgTwoPointersAttempted': avgTwoPointersAttempted.text,
                'twoPointPercentage': twoPointPercentage.text, 'effectiveFieldGoalPercentage': effectiveFieldGoalPercentage.text,
                'avgFreeThrowsMade': avgFreeThrowsMade.text, 'avgFreeThrowsAttempted': avgFreeThrowsAttempted.text,
                'freeThrowPercentage': freeThrowPercentage.text, 'avgOffensiveRebounds': avgOffensiveRebounds.text,
                'avgDefensiveRebounds': avgDefensiveRebounds.text, 'avgAst': avgAst.text, 'avgStl': avgStl.text,
                'avgBlk': avgBlk.text, 'avgTov': avgTov.text, 'avgPf': avgPf.text, 'avgPts': avgPts.text}
    """
    table = "G | GS | MP | FG | FGA | FG% | 3P | 3PA | 3P% | 2P | 2PA | 2P% | eFG% | FT | FTA | FT% | ORB | DRB | TRB | AST | STL | BLK | TOV | PF | PTS \n --:|--:|---:|---:|---:|----:|---:|---:|----:|---:|---:|----:|----:|---:|---:|----:|---:|---:|---:|---:|---:|---:|---:|---:|---: \n" + stats['games'] + "|" + stats['gamesStarted'] + "|" + stats['avgMinutes'] + "|" + stats['avgFgm'] + "|" + stats['avgFga'] + "|" + stats['fieldGoalPercentage'] + "|" + stats['avgTpm'] + "|" + stats['avgTpa'] + "|" + stats['threePointPercentage'] + "|" + stats['avgTwoPointersMade'] + "|" + stats['avgTwoPointersAttempted'] + "|" + stats['twoPointPercentage'] + "|" + stats['effectiveFieldGoalPercentage'] + "|" + stats['avgFreeThrowsMade'] + "|" + stats['avgFreeThrowsAttempted'] + "|" + stats['freeThrowPercentage'] + "|" + stats['avgOffensiveRebounds'] + "|" + stats['avgDefensiveRebounds'] + "|" + stats['avgTotalRebounds'] +"|" + stats['avgAst'] + "|" + stats['avgStl'] + "|" + stats['avgBlk'] + "|" + stats['avgTov'] + "|" + stats['avgPf'] + "|" + stats['avgPts']
    return table
