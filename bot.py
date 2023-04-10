import sys

import discord
import random
import json


def run_discord_bot():
    TOKEN = 'MTA3MDM1NjA1OTI3MDY4ODc2OQ.Gaa7wE.2Nx7iUXGb2scjs85ZcEYWY8OQjg4k-CIRa5wcU'
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        await client.get_channel(914606748743127072).send("BOT BACK UP AND RUNNING!")
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return
        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if channel == 'gym-challenge' or channel == 'test' or channel == 'gym-leader':
            print(f"{message.author} said: '{message}' ({message.content})")

            # Debug printing
            print(f"{username} said: '{user_message}' ({channel})")
            # If the user message contains a '?' in front of the text, it becomes a private message
            if user_message != "":
                if user_message[0] == '?':
                    await send_message(message, is_private=True)
                else:
                    await send_message(message, is_private=False)
        else:
            return
    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)


# Send messages
async def send_message(message, is_private):
    try:
        response = handle_response(message.author, message.content, message.channel)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        print("this is the main error: ", e)
        print("Exception type: ", exception_type)
        print("File name: ", filename)
        print("Line number: ", line_number)


def handle_response(author, message, channel) -> str:
    lowerMSG = str(message.lower())
    testchannel = str(channel)
    msglist = convert(str(message.lower()))
    returnmsg = ""

    if testchannel == 'gym-challenge' or testchannel == 'test' or testchannel == 'gym-leader':
        if lowerMSG == 'ping':
            return author.mention
        if lowerMSG == 'coin':
            if (random.randint(1, 2)) == 1:
                returnmsg = "heads"
            else:
                returnmsg = "heads"
        if msglist[0] == '!':
            returnmsg = Exclamation(author, message)

    return returnmsg


def Exclamation(author, message):
    lowerMSG = str(message.lower())
    returnmsg = "`INCORRECT`"
    boolcheck = False
    if lowerMSG[1] == 'g':
        if lowerMSG[2] == 'i':
            if lowerMSG[3] == 'v':
                if lowerMSG[4] == 'e':
                    if lowerMSG[5] == ' ':
                        for leader in currentleaders():
                            if str(author) == str(leader):
                                boolcheck = True
                        if boolcheck:
                            returnmsg = GiveCommand(message, GetAllChallengersFromJson())
                        else:
                            returnmsg = "`You are not Authorized to use this command!`\n`***Please ping a leader or " \
                                        "e4 to give ya the badge.***`"

    if lowerMSG[1] == 'r':
        if lowerMSG[2] == 'e':
            if lowerMSG[3] == 's':
                if lowerMSG[4] == 'e':
                    if lowerMSG[5] == 't':
                        if lowerMSG[6] == ' ':
                            for admin in currentadmins():
                                if str(author) == str(admin):
                                    boolcheck = True
                            if boolcheck:
                                returnmsg = resetcommand(message, GetAllChallengersFromJson())
                            else:
                                returnmsg = "`New person detected!`\n`New profile made and saved`"

    if lowerMSG[1] == 'j':
        if lowerMSG[2] == 'o':
            if lowerMSG[3] == 'i':
                if lowerMSG[4] == 'n':
                    if Join(author, GetAllChallengersFromJson()):
                        returnmsg = "`You are already in the list!`"
                    else:
                        returnmsg = "`New person detected!`\n`New profile made and saved`"

    if lowerMSG[1] == 's':
        if lowerMSG[2] == 'c':
            if lowerMSG[3] == 'o':
                if lowerMSG[4] == 'r':
                    if lowerMSG[5] == 'e':
                        returnmsg = ScoreCommand(author, message)

    if lowerMSG[1] == 'c':
        if lowerMSG[2] == 'o':
            if lowerMSG[3] == 'm':
                if lowerMSG[4] == 'm':
                    if lowerMSG[5] == 'a':
                        if lowerMSG[6] == 'n':
                            if lowerMSG[7] == 'd':
                                if lowerMSG[8] == 's':
                                    returnmsg = "commands are: `!help`, `!commands`, `!score`, `!give`, `!reset`, " \
                                                "`!join`, coin, ping\n"\
                                                "`!join` | makes a profile to track your badges, every new person " \
                                                "hass to do this\n" \
                                                "`!give` | gives the user a badge only gym leaders can use this" \
                                                "`!give Rishino#5321 water`\n"\
                                                "`!score` | shows the user's badges earned" \
                                                "`!score` or `!score Rishino#5321` or `!score Rishino#5321 water`\n" \
                                                "`!reset` | resets the stats of a person " \
                                                "`!reset Rishino#5321 all` or `!reset Rishino#5321 e4`\n"\
                                                "*`I'm still in beta, so errors may occur(keep a mental note of " \
                                                "badges you earned)`*"
    if lowerMSG[1] == 'h':
        if lowerMSG[2] == 'e':
            if lowerMSG[3] == 'l':
                if lowerMSG[4] == 'p':
                    returnmsg = "commands are: `!help`, `!commands`, `!score`, `!give`, `!reset`, " \
                                "`!join`, coin, ping\n" \
                                "`!join` | makes a profile to track your badges, every new person " \
                                "hass to do this\n" \
                                "`!give` | gives the user a badge only gym leaders can use this" \
                                "`!give Rishino#5321 water`\n" \
                                "`!score` | shows the user's badges earned" \
                                "`!score` or `!score Rishino#5321` or `!score Rishino#5321 water`\n" \
                                "`!reset` | resets the stats of a person " \
                                "`!reset Rishino#5321 all` or `!reset Rishino#5321 e4`\n"\
                                "*`I'm still in beta, so errors may occur(keep a mental note of badges you earned)`*"

    return returnmsg


def currentadmins() -> list:
    adminlist = ["iMissKecleon#8097", "Cryptidwitch#8354", "Bubblesaur#2996", "Rishino#5321", "Ed-Boy24#2424"]
    return adminlist


def currentleaders() -> list:
    leaderslist = ["iMissKecleon#8097", "Honest | The Uchiha 🧞♂#7865", "Cryptidwitch#8354", "Bubblesaur#2996",
                   "Rishino#5321", "Ed-Boy24#2424", "『 Kyom 』#0858", "Socktapus#0036", "Drew07#7032", "Vyoru#0001",
                   "Leonidas#0888", "Owl#1095", "Socktapus#0036"]
    return leaderslist


def currentbadges() -> list:
    badgeslist = ["dragon", "electric", "fairy", "fighting", "fire", "grass", "poison", "water", "e4"]
    return badgeslist


def resetlist() -> list:
    resetreturnlist = ["all", "e4"]
    return resetreturnlist


def givelistofuserstats(user) -> list:
    badgeslist = []
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        challengers = dict()

        for userdatatogive in data['challengers']:
            name = userdatatogive['name']
            userdatatogive = userdatatogive['userstats']
            challengers[name] = userdatatogive
        badgelist = currentbadges()
        for i in range(len(badgelist)):
            if badgelist[i] == "e4":
                badgeslist.append(challengers[str(user)]['E4'])
            else:
                badgeslist.append(challengers[str(user)][badgelist[i]])
    return badgeslist


def scorebadge(user, badge) -> str:
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        challengers = dict()

        for userdatatogive in data['challengers']:
            name = userdatatogive['name']
            userdatatogive = userdatatogive['userstats']
            challengers[name] = userdatatogive

    badgeresult = challengers[str(user)][str(badge.lower())]
    if badgeresult == "false":
        returnmsg = "`" + user + " did not beat the " + badge + " gym !`"
    else:
        returnmsg = "`" + user + " has already beaten the " + badge + " gym !`"

    return returnmsg


def badges(user) -> str:
    badgeslist = []
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        challengers = dict()

        for badgedata in data['challengers']:
            name = badgedata['name']
            allbadgedata = badgedata['userstats']
            challengers[name] = allbadgedata
        badgelist = currentbadges()
        for i in range(len(badgelist)):
            if badgelist[i] == "e4":
                badgeslist.append(challengers[str(user)]['E4'])
            else:
                badgeslist.append(challengers[str(user)][badgelist[i]])
        for badge in badgeslist:
            if str(badge) != str("false"):
                return badgesstr(str(user), badgeslist, currentbadges(), True)
        return elitefour(str(challengers[str(user)]['E4']))


def badgesstr(user, badgeslist, badgesnames, displaystylebool) -> str:
    returnstr = ""
    if displaystylebool:
        returnstr = returnstr + "This is ***" + user + "'s*** gyms progress:\n"
        for x in range(8):
            if str(badgeslist[x]) == str('false'):
                if x > 0:
                    returnstr = returnstr + ",\n"
                returnstr = returnstr + "`" + badgesnames[x] + " gym NOT beaten" + "`"
            else:
                if x > 0:
                    returnstr = returnstr + ",\n"
                returnstr = returnstr + "***" + badgesnames[x] + " gym beaten" + "***"
    else:
        returnstr = returnstr + "You need to beat the following gyms:\n"
        for x in range(8):
            if str(badgeslist[x]) == str('false'):
                returnstr = returnstr + badgesnames[x] + " gym\n"
    return returnstr


def elitefour(e4number) -> str:
    if int(e4number) >= 4:
        returnstr = "You've beaten ALL the elite fours Challenge the champ"
    else:
        returnstr = "You've beaten " + e4number + "/4 e4 members"
    return returnstr


def GetAllChallengersFromJson() -> list:
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        challengers = []

        for challengerdata in data['challengers']:
            name = challengerdata['name']
            challengers.append(str(name))

    return challengers


def jsonloader() -> str:
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        challengers = dict()

        for jsonbadges in data['challengers']:
            name = jsonbadges['name']
            jsonbadges = jsonbadges['userstats']
            challengers[name] = jsonbadges

    return str(challengers)


def formattedjsonloader() -> str:
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        challengers = dict()

        for formattedjsonbadges in data['challengers']:
            name = formattedjsonbadges['name']
            formattedjsonbadges = formattedjsonbadges['userstats']
            challengers[name] = formattedjsonbadges

    return str(challengers)


def Join(author, allchallengernames):
    new_data = {
        "name": str(author),
        "userstats": {
            "dragon": "false",
            "electric": "false",
            "fairy": "false",
            "fighting": "false",
            "fire": "false",
            "grass": "false",
            "poison": "false",
            "water": "false",
            "E4": 0
        }
    }

    returnbool = False
    for name in allchallengernames:
        if name == str(author):
            returnbool = True
            return returnbool

    writejson(new_data)
    return returnbool


def ScoreCommand(author, message):
    splitmsg = message.split()
    msgcount = len(splitmsg)
    returnmsg = "`this person must not be in saved! maybe if they `!join` you can see theur stats`"
    if msgcount < 2:
        if Join(author, GetAllChallengersFromJson()):
            returnmsg = badges(author)
        else:
            returnmsg = "***User not recognized!\n" \
                        "***The correct format is: `!score user badge`\n" \
                        "Example: `!score Rishino#5321 water`\n" \
                        "You can see their username underneath their name on their profile\n" \
                        "https://cdn.discordapp.com/attachments/1025013785548836875" \
                        "/1071815928960000010/image.png"
    else:
        if msgcount == 2:
            for badge in currentbadges():
                if badge == splitmsg[1].lower():
                    returnmsg = scorebadge(author, splitmsg[1].lower())
                    break
                else:
                    for chall in GetAllChallengersFromJson():
                        if chall == splitmsg[1]:
                            returnmsg = badges(splitmsg[1])
                            break
                        else:
                            returnmsg = "***User not recognized!\n" \
                                        "***The correct format is: `!score user badge`\n" \
                                        "Example: `!score Rishino#5321 water`\n" \
                                        "You can see their username underneath their name on their profile\n" \
                                        "https://cdn.discordapp.com/attachments/1025013785548836875" \
                                        "/1071815928960000010/image.png"
        else:
            if msgcount > 2:
                for challuser in GetAllChallengersFromJson():
                    if challuser == splitmsg[1]:
                        for badge in currentbadges():
                            if badge == str(splitmsg[2].lower()):
                                returnmsg = scorebadge(challuser, badge)
                                break
                            else:
                                returnmsg = "***badge not recognized!\n" \
                                                "***The correct format is: `!score user badge`\n" \
                                                "Example: `!score Rishino#5321 water`\n" \
                                                "You can see their username underneath their name on their " \
                                                "profile\n" \
                                                "https://cdn.discordapp.com/attachments/1025013785548836875" \
                                                "/1071815928960000010" \
                                                "/image.png"
                        break
                    else:
                        returnmsg = "***User not recognized!\n" \
                                        "***The correct format is: `!score user badge`\n" \
                                        "Example: `!score Rishino#5321 water`\n" \
                                        "You can see their username underneath their name on their profile\n" \
                                        "https://cdn.discordapp.com/attachments/1025013785548836875" \
                                        "/1071815928960000010/image.png"

    return returnmsg


def GiveCommand(message, allchallengernames):
    splitmsg = message.split()
    inBadges = False
    inUsers = False

    if splitmsg[0].lower() == "!give":
        for badge in currentbadges():
            if splitmsg[2].lower() == badge:
                inBadges = True
                for name in allchallengernames:
                    if splitmsg[1] == name:
                        inUsers = True

    if not inBadges:
        returnmsg = "***badge not recognized!\n" \
                    "***The correct format is: `!give user badge`\n" \
                    "Example: `!give Rishino#5321 poison badge`\n" \
                    "You can see their username underneath their name on their profile\n" \
                    "https://cdn.discordapp.com/attachments/1025013785548836875/1071815928960000010/image.png"
    else:
        if not inUsers:
            returnmsg = "***User not recognized!\n" \
                        "***The correct format is: `!give user badge`\n" \
                        "Example: `!give Rishino#5321 poison badge`\n" \
                        "You can see their username underneath their name on their profile\n" \
                        "https://cdn.discordapp.com/attachments/1025013785548836875/1071815928960000010/image.png"
        else:
            returnmsg = give(splitmsg[1], splitmsg[2].lower())

    return returnmsg


def resetcommand(message, allchallengernames):
    splitmsg = message.split()
    e4reset = False
    allreset = False
    resettypelist = resetlist()

    if splitmsg[0].lower() == "!reset":
        for name in allchallengernames:
            if splitmsg[1] == name:
                for resettype in resettypelist:
                    if splitmsg[2].lower() == resettype:
                        e4reset = True
                    if splitmsg[2].lower() == resettype:
                        allreset = True

    if not e4reset:
        if not allreset:
            returnmsg = "***I don't understand who's data or what you are trying to reset***\n" \
                        "Either the person is not in the list and has to use `!join` or the value being reset is " \
                        "wrong\n" \
                        "The correct format is: \n" \
                        "`!reset user e4` or `!reset user all` Example: `!reset Rishino#5321 e4`\n" \
                        "You can see their username underneath their name on their profile\n" \
                        "https://cdn.discordapp.com/attachments/1025013785548836875/1071815928960000010/image.png"
        else:
            reset(splitmsg[1], True)
            returnmsg = "`All " + splitmsg[1] + "'s data has been reset!`"
    else:
        reset(splitmsg[1], False)
        returnmsg = "`" + splitmsg[1] + "'s E4 data has been reset!`"

    return returnmsg


def give(user, badge):
    beatenallgyms = True
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        badgesx = currentbadges()
        for userData in data['challengers']:
            name = userData['name']
            if str(name) == str(user):
                newData = {
                    'name': str(name),
                    'userstats': {
                        badgesx[0]: userData['userstats'][badgesx[0]],
                        badgesx[1]: userData['userstats'][badgesx[1]],
                        badgesx[2]: userData['userstats'][badgesx[2]],
                        badgesx[3]: userData['userstats'][badgesx[3]],
                        badgesx[4]: userData['userstats'][badgesx[4]],
                        badgesx[5]: userData['userstats'][badgesx[5]],
                        badgesx[6]: userData['userstats'][badgesx[6]],
                        badgesx[7]: userData['userstats'][badgesx[7]],
                        'E4': userData['userstats']['E4']
                    }
                }
        if badge == 'e4':
            if int(str(newData['userstats']['E4'])) >= 4:
                returnmsg = "`This player already is able to challenge the champion!`"
            else:
                if allowedtogetE4(givelistofuserstats(user)):
                    newData['userstats']['E4'] = int(str(newData['userstats']['E4'])) + 1
                    if int(str(newData['userstats']['E4'])) >= 4:
                        returnmsg = "`This player is now able to challenge the champion!`"
                    else:
                        returnmsg = "`This player has beaten " + newData['userstats']['E4'] + "/4 E4's`"
                else:
                    returnmsg = "`This player has not beaten 8 gyms yet`\n`ask them to do !score to see`"
        else:
            if newData['userstats'][badge] == "true":
                returnmsg = "`This player already beaten this gym!`\n" \
                            + badgesstr(user, givelistofuserstats(user), currentbadges(), False)
            else:
                newData['userstats'][badge] = "true"
                for x in range((len(givelistofuserstats(user))) - 1):
                    if givelistofuserstats(user)[x] == "false":
                        beatenallgyms = False
                if beatenallgyms:
                    returnmsg = "`This player has beaten ALL the gyms!`\n" \
                                "<@" + user + "> `Please start preparing to battle the E4!`"
                else:
                    returnmsg = "`" + user + " has beaten the " + badge + " gym!`\n" \
                                + badgesstr(user, givelistofuserstats(user), currentbadges(), False)
    delete(user)
    with open('badges.json', 'w') as file:
        file.write(json.dumps(data, indent=4))
    writejson(newData)

    return returnmsg


def reset(user, resetbool):
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        badgesx = currentbadges()
        for userData in data['challengers']:
            name = userData['name']
            if str(name) == str(user):
                newData = {
                    'name': str(name),
                    'userstats': {
                        badgesx[0]: userData['userstats'][badgesx[0]],
                        badgesx[1]: userData['userstats'][badgesx[1]],
                        badgesx[2]: userData['userstats'][badgesx[2]],
                        badgesx[3]: userData['userstats'][badgesx[3]],
                        badgesx[4]: userData['userstats'][badgesx[4]],
                        badgesx[5]: userData['userstats'][badgesx[5]],
                        badgesx[6]: userData['userstats'][badgesx[6]],
                        badgesx[7]: userData['userstats'][badgesx[7]],
                        'E4': userData['userstats']['E4']
                    }
                }
        if not resetbool:
            newData['userstats']['E4'] = 0
        else:
            newData['userstats'][badgesx[0]] = "false"
            newData['userstats'][badgesx[1]] = "false"
            newData['userstats'][badgesx[2]] = "false"
            newData['userstats'][badgesx[3]] = "false"
            newData['userstats'][badgesx[4]] = "false"
            newData['userstats'][badgesx[5]] = "false"
            newData['userstats'][badgesx[6]] = "false"
            newData['userstats'][badgesx[7]] = "false"
            newData['userstats']['E4'] = 0
    delete(user)
    with open('badges.json', 'w') as file:
        file.write(json.dumps(data, indent=4))
    writejson(newData)


def delete(user):
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
    deleteindex = 0
    for userDatatodelete in data['challengers']:
        name = userDatatodelete['name']
        if str(name) == str(user):
            break
        deleteindex = deleteindex + 1

    names_to_remove = [str(user)]

    for element in data['challengers']:
        if element['name'] in names_to_remove:
            data['challengers'].remove(element)


def allowedtogetE4(listofbadges) -> bool:
    returnbool = False
    badgesEarned = 0
    for x in range(len(listofbadges)):
        if listofbadges[x] == "true":
            badgesEarned = badgesEarned + 1
    if badgesEarned >= 8:
        returnbool = True

    return returnbool


def writejson(data):
    writenewjson(data)


def writenewjson(new_data):
    filename = 'badges.json'
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data['challengers'].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


def convert(string):
    list1 = []
    list1[:0] = string
    return list1
