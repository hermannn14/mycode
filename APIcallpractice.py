import requests

hockey= requests.get("https://statsapi.web.nhl.com/api/v1/teams").json()

# hockey["teams"] is a list!

for i in hockey["teams"]:
    # i is a dictionary!
    # print out the name of the team
    # print out their website
    # print out the name of the team's division
    # timezone is their home venue/arena?
    print(i["teamName"])
    print(i["officialSiteUrl"])
    print(i["venue"]["timeZone"]["tz"])
    print(i["division"]["name"])
    print(end="\n")
        
