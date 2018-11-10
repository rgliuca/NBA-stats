import urllib.request
import json

USER_AGENT  = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:60.0) Gecko/20100101 Firefox/60.0'}
URL         = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2018-19&SeasonType=Regular+Season&StatCategory=PTS"

req = urllib.request.Request(
    url     = URL,
    headers = USER_AGENT
)

with urllib.request.urlopen(req) as raw_stats:
    player_stats_json = json.loads(raw_stats.read())

with open("2018-2019.txt", 'w') as out:
    out.write(json.dumps(player_stats_json))

