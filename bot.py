import sys

import discord
import random
import json


def run_discord_bot():
    TOKEN = 'MTA3MDM1NjA1OTI3MDY4ODc2OQ.Gaa7wE.2Nx7iUXGb2scjs85ZcEYWY8OQjg4k-CIRa5wcU'
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        # 914606748743127072 gym-challenge   | BOT BACK UP AND RUNNING!
        await client.get_channel(1070373326440120361).send(
            "!join | ``!give <@98475932624371712> poison badge | !score <@98475932624371712>``")
        print(f'{client.user} is now running!')
        print(" ")

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        user_message = str(message.content)
        channel = str(message.channel)

        if channelCheck(channel):
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
        # filename = exception_traceback.tb_frame.f_code.co_filename
        # line_number = exception_traceback.tb_lineno
        print(f'error? (Might just be a RCG message): {e} |  Exception type: {exception_type}\n')
        # print("this is the main error: "  e + "Exception type: ", exception_type)
        # print("File name: ", filename)
        # print("Line number: ", line_number)


def handle_response(author, messageContent, channel) -> str:
    lowerMSG = str(messageContent.lower())
    testchannel = str(channel)
    msglist = convert(str(messageContent.lower()))
    if lowerMSG == 'ping':
        return author.mention
    if lowerMSG == 'coin':
        if (random.randint(1, 2)) == 1:
            return "tails"
        else:
            return "heads"
    if lowerMSG == 'bot!':
        return "HI! How can i help you?!\nAlso <@350990937587056640> is a beeg nerd"
    if testchannel == 'gym-challenge' or testchannel == 'test' or testchannel == 'gym-leader':
        if msglist[0] == '!':
            logUserMessage(author, messageContent, testchannel)
            return Exclamation(author, messageContent)
    if testchannel == 'raid-chat-general':
        if msglist[0] == '!':
            splitmsg = lowerMSG.split()
            if splitmsg[0] == '!ping':
                logUserMessage(author, messageContent, testchannel)
                return "<@" + splitmsg[1] + ">"


def Exclamation(msgAuthor, message):
    lowerMSG = str(message.lower())
    # author = str(msgAuthor)
    authorID = str(msgAuthor.id)
    returnMSG = "`INCORRECT`\n`I do not recognize command you tried to use`"
    boolcheck = leaderCheck(authorID)

    if giveCheck(lowerMSG):
        if boolcheck:
            returnMSG = giveCommand(message, GetAllChallengersFromJson())
        else:
            returnMSG = "`You are not Authorized to use this command!`\n" \
                        "`<@&700735818268147723> or <@&700737181580525659> " \
                        "could you investigate and give out the badge.`"
    if resetCheck(lowerMSG):
        for mod in currentMods():
            if authorID == mod:
                boolcheck = True
                if boolcheck:
                    returnMSG = resetcommand(message, GetAllChallengersFromJson())
                else:
                    returnMSG = "`New person detected!`\n`New profile made and saved`"

    if joinCheck(lowerMSG):
        if joinCommand(msgAuthor, GetAllChallengersFromJson()):
            returnMSG = "`You are already in the list!`"
        else:
            returnMSG = "`New profile made and saved`"

    if eliteFourCheck(lowerMSG):
        returnMSG = eliteFourCommand(authorID, GetAllChallengersFromJson())

    if champCheck(lowerMSG):
        returnMSG = champCommand(authorID, GetAllChallengersFromJson())

    if scoreCheck(lowerMSG):
        returnMSG = ScoreCommand(msgAuthor, message)

    if helpCheck(lowerMSG):
        returnMSG = "commands are: " \
                    "`!help`, `!commands`, `!score`, `!give`, `!reset`, `!join`," \
                    "`!champ`,`!e4`, coin, ping, and my favourite `bot!`\n" \
                    "`!join` | makes a profile to track your badges, every new person hass to do this\n" \
                    "`!give` | gives the user a badge only gym leaders can use this" \
                    "`!give ||@User or there ID|| ||The Badge Name||`\n" \
                    "`!score` | shows the user's badges earned" \
                    "`!score` or !score ||@User or there ID||" \
                    " optional !score ||@User or there ID|| ||The Badge Name||`\n" \
                    "`!reset` | resets the stats of a person " \
                    "!reset ||@User or there ID|| ||all or e4||\n" \
                    "`!champ` | pings the current champ for a challenge\n" \
                    "`!e4` | pings the current champ for a challenge\n" \
                    "*`I'm still in beta, so errors may occur(keep a mental note of badges you earned)`*"

    return returnMSG


def currentMods() -> list:
    modlist = ["450849016536629276", "659970441263185921", "329899029372731393",
               "98475932624371712", "575525936368451594"]
    return modlist


def currentLeaders() -> list:
    leaderslist = ["450849016536629276", "Honest | The Uchiha 🧞♂#7865",
                   "Cryptidwitch#8354", "Bubblesaur#2996", "Ed-Boy24#2424",
                   "『 Kyom 』#0858", "Socktapus#0036", "Drew07#7032", "Vyoru#0001", "Leonidas#0888",
                   "Owl#1095", "Socktapus#0036", "98475932624371712"]
    return leaderslist


def currentBadges() -> list:
    badgeslist = ["dragon", "electric", "fairy", "fighting", "fire", "grass", "poison", "water", "e4", "champion"]
    return badgeslist


def resetList() -> list:
    resetreturnlist = ["all", "e4"]
    return resetreturnlist


def giveListOfUserStats(user) -> list:
    badgeslist = []
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        challengers = dict()

        for userData in data['challengers']:
            userid = userData['userid']
            userData = userData['userstats']
            challengers[userid] = userData

        badgelist = currentBadges()
        for i in range(len(badgelist)):
            if badgelist[i] == "e4":
                badgeslist.append(challengers[user]['E4'])
            else:
                badgeslist.append(challengers[user][badgelist[i]])
    return badgeslist


def badgeData(user, badge) -> str:
    badgeresult = ""
    with open('badges.json') as jsonData:
        data = json.load(jsonData)

        for userData in data['challengers']:
            userID = userData['userid']
            userDataID = str(userID)
            if userDataID == user:
                badgeresult = userData['userstats'][badge]

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

        for userData in data['challengers']:
            userid = userData['userid']
            userData = userData['userstats']
            challengers[userid] = userData

        badgelist = currentBadges()
        for i in range(len(badgelist)):
            if badgelist[i] == "e4":
                badgeslist.append(challengers[user]['E4'])
            else:
                badgeslist.append(challengers[user][badgelist[i]])
        for badge in badgeslist:
            if str(badge) != str("false"):
                return badgeReplyStringData(user, badgeslist, currentBadges(), True, False, "")
        return eliteFour(str(challengers[user]['E4']))


def badgeReplyStringData(user, badgeslist, badgesnames, forScoreCommand, forGiveCommand, badgeGiven) -> str:
    returnstr = ""
    if forScoreCommand:
        returnstr = returnstr + "This is <@" + user + ">'s gyms progress:\n"
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
            if forGiveCommand:
                if badgeGiven != badgesnames[x]:
                    if str(badgeslist[x]) == str('false'):
                        returnstr = returnstr + badgesnames[x] + " gym\n"
    return returnstr


def eliteFour(e4number) -> str:
    if int(e4number) >= 4:
        returnstr = "You've beaten ALL the elite four members!\n" \
                    " You can go ahead and use `!champ` to challenge the champ"
    else:
        returnstr = "You've beaten " + e4number + "/4 e4 members"
    return returnstr


def GetAllChallengersFromJson() -> list:
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        challengers = []

        for challengerdata in data['challengers']:
            userid = challengerdata['userid']
            challengers.append(str(userid))

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

        for userData in data['challengers']:
            userid = userData['userid']
            userData = userData['userstats']
            challengers[userid] = userData

    return str(challengers)


def champCommand(author, allchallengernames):
    userCheck = True
    boolCheck = False

    for challenger in allchallengernames:
        if challenger == author:
            userCheck = False

    for i in range(9):
        if giveListOfUserStats(author)[i] == 4:
            boolCheck = True

    if userCheck:
        return "you are not a challenger do `!join` to enter"
    else:
        if boolCheck:
            return "<@&700737737581527142> You have a new challenger!"
        else:
            return "You have to beat the E4 before you can challenge the champ"


def eliteFourCommand(author, allchallengernames):
    userCheck = True
    boolCheck = True

    for challenger in allchallengernames:
        if challenger == author:
            userCheck = False

    for i in range(10):
        if giveListOfUserStats(author)[i] == 'false':
            boolCheck = False

    if userCheck:
        return "you are not a challenger do `!join` to enter"
    else:
        if boolCheck:
            return "<@&700737181580525659> You have a new challenger!"
        else:
            return "You have to beat all gyms before you can start the E4"


def joinCommand(author, allchallengernames):
    new_data = {
        "userid": str(author.id),
        "username": str(author.name),
        "userstats": {
            "dragon": "false",
            "electric": "false",
            "fairy": "false",
            "fighting": "false",
            "fire": "false",
            "grass": "false",
            "poison": "false",
            "water": "false",
            "E4": 0,
            "champion": "false"
        }
    }

    returnbool = False
    for userid in allchallengernames:
        if userid == str(author.id):
            returnbool = True
            return returnbool

    writejson(new_data)
    return returnbool


def ScoreCommand(author, message):
    splitmsg = message.split()
    msgcount = len(splitmsg)
    returnMSG = "this person must not be in saved!\n ask them to `!join` you can see their stats"

    if msgcount < 2:
        authorID = str(author.id)
        if joinCommand(author, GetAllChallengersFromJson()):
            return badges(authorID)
        else:
            return "***User not recognized!\n" \
                   "***The correct format is: !give ||@User or there ID|| ||The Badge Name||\n" \
                   "Example: `!score <@98475932624371712> water` | `!score 98475932624371712 water`"
    else:
        authorID = splitmsg[1]

        if usernameCheck(splitmsg[1]):
            authorID = usernameSplit(splitmsg[1])

        if msgcount == 2:
            for badge in currentBadges():
                if badge == splitmsg[1].lower():
                    return badgeData(authorID, splitmsg[1].lower())
                else:
                    for chall in GetAllChallengersFromJson():
                        if chall == authorID:
                            return badges(authorID)
                        else:
                            returnMSG = "***User not recognized!\n" \
                                        "***The correct format is: !give ||@User or there ID|| ||The Badge Name||\n" \
                                        "Example: `!score <@98475932624371712> water` " \
                                        "| `!score 98475932624371712 water`"

        else:
            if msgcount > 2:
                for challuser in GetAllChallengersFromJson():
                    if challuser == splitmsg[1]:
                        for badge in currentBadges():
                            if badge == str(splitmsg[2].lower()):
                                return badgeData(challuser, badge)
                            else:
                                returnMSG = "***badge not recognized!\n" \
                                            "***The correct format is: " \
                                            "!give ||@User or there ID|| ||The Badge Name||\n" \
                                            "Example: " \
                                            "`!score <@98475932624371712> water` | `!score 98475932624371712 water`"
                    else:
                        returnMSG = "***User not recognized!\n" \
                                    "***The correct format is: !give ||@User or there ID|| ||The Badge Name||\n" \
                                    "Example: `!score <@98475932624371712> water` | `!score 98475932624371712 water`"

    return returnMSG


def giveCommand(message, allChallengers):
    splitmsg = message.split()
    inBadges = False
    inUsers = False
    authorID = splitmsg[1]

    if usernameCheck(splitmsg[1]):
        authorID = usernameSplit(splitmsg[1])

    if (len(splitmsg) > 2):
        if splitmsg[0].lower() == "!give":
            for badge in currentBadges():
                if splitmsg[2].lower() == badge:
                    inBadges = True
                    for userid in allChallengers:
                        if authorID == userid:
                            inUsers = True

    else:
        return "`INCORRECT!\n`" \
               "!give ||@User or there ID|| ||The Badge Name||"

    if not inBadges:
        return "***badge not recognized!\n" \
               "***The correct format is: !give ||@User or there ID|| ||The Badge Name||\n" \
               "Example: `!give 98475932624371712 poison` or `!give <@98475932624371712> poison`\n"
    else:
        if not inUsers:
            return "***User not recognized!\n" \
                   "***The correct format is: !give ||@User or there ID|| ||The Badge Name||\n" \
                   "Example: `!give 98475932624371712 poison` or `!give <@98475932624371712> poison badge`\n"
        else:
            return give(authorID, splitmsg[2].lower())


def resetcommand(message, allchallengernames):
    splitmsg = message.split()
    e4reset = False
    allreset = False
    resettypelist = resetList()
    authorID = splitmsg[1]

    if usernameCheck(splitmsg[1]):
        authorID = usernameSplit(splitmsg[1])

    if splitmsg[0].lower() == "!reset":
        for userID in allchallengernames:
            if authorID == userID:
                for resettype in resettypelist:
                    if splitmsg[2].lower() == resettype:
                        if resettype == "all":
                            allreset = True
                        if resettype == "e4":
                            e4reset = True

    if not e4reset:
        if not allreset:
            return "***Command error***\n" \
                   "Either the person is not in the list and has to use `!join` or the value being reset is wrong\n" \
                   "The correct format is: \n" \
                   "`!reset ||@User or there ID|| ||E4 or ALL||` Example: `!reset 98475932624371712 e4`"
        else:
            reset(authorID, True)
            return "All <@" + authorID + ">'s data has been reset!"
    else:
        reset(authorID, False)
        return "<@" + authorID + ">'s E4 data has been reset!"


def give(user, badge):
    beatenallgyms = True
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        badgesx = currentBadges()
        for userData in data['challengers']:
            userID = userData['userid']
            userName = userData['username']
            userDataID = str(userID)
            userDataName = str(userName)
            if userDataID == user:
                newData = {
                    'userid': userDataID,
                    'username': userDataName,
                    'userstats': {
                        badgesx[0]: userData['userstats'][badgesx[0]],
                        badgesx[1]: userData['userstats'][badgesx[1]],
                        badgesx[2]: userData['userstats'][badgesx[2]],
                        badgesx[3]: userData['userstats'][badgesx[3]],
                        badgesx[4]: userData['userstats'][badgesx[4]],
                        badgesx[5]: userData['userstats'][badgesx[5]],
                        badgesx[6]: userData['userstats'][badgesx[6]],
                        badgesx[7]: userData['userstats'][badgesx[7]],
                        'E4': userData['userstats']['E4'],
                        'champion': userData['userstats']['champion']
                    }
                }
        if badge == 'e4':
            if newData['userstats']['E4'] >= 4:
                returnmsg = "`This player already is able to challenge the champion!`"
            else:
                if allowedtogetE4(giveListOfUserStats(user)):
                    newData['userstats']['E4'] = newData['userstats']['E4'] + 1
                    if newData['userstats']['E4'] >= 4:
                        returnmsg = "`This player is now able to challenge the champion!`"
                    else:
                        e4data = str(newData['userstats']['E4'])
                        returnmsg = "`This player has beaten " + e4data + "/4 E4's`"
                else:
                    returnmsg = "`This player has not beaten 8 gyms yet`\n`ask them to do !score to see`"
        else:
            if badge != 'champion':
                if newData['userstats'][badge] == "true":
                    returnmsg = "`This player already beaten this gym!`"
                else:
                    newData['userstats'][badge] = "true"
                    for x in range((len(newData['userstats'])) - 2):
                        if newData['userstats'][badgesx[x]] == "false":
                            beatenallgyms = False
                    if beatenallgyms:
                        returnmsg = "`This player has beaten ALL the gyms!`\n" \
                                    "<@" + user + "> `Please start preparing to battle the E4!`"
                    else:
                        returnmsg = "<@" + user + ">  has beaten the " + badge + " gym!\n" \
                                    + badgeReplyStringData(user,
                                                           giveListOfUserStats(user), currentBadges(), False, True,
                                                           badge)
            else:
                if newData['userstats'][badge] == "true":
                    returnmsg = "`This player is already Champion!`"
                else:
                    newData['userstats'][badge] = "true"
                    returnmsg = "A NEW CHAMPION HAS TAKEN THE SEAT"
    delete(user)
    with open('badges.json', 'w') as file:
        file.write(json.dumps(data, indent=4))
    writejson(newData)

    return returnmsg


def reset(user, resetbool):
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
        badgesx = currentBadges()
        for userData in data['challengers']:
            userID = userData['userid']
            userName = userData['username']
            userDataID = str(userID)
            userDataName = str(userName)
            if userDataID == user:
                newData = {
                    'userid': userDataID,
                    'username': userDataName,
                    'userstats': {
                        badgesx[0]: userData['userstats'][badgesx[0]],
                        badgesx[1]: userData['userstats'][badgesx[1]],
                        badgesx[2]: userData['userstats'][badgesx[2]],
                        badgesx[3]: userData['userstats'][badgesx[3]],
                        badgesx[4]: userData['userstats'][badgesx[4]],
                        badgesx[5]: userData['userstats'][badgesx[5]],
                        badgesx[6]: userData['userstats'][badgesx[6]],
                        badgesx[7]: userData['userstats'][badgesx[7]],
                        'E4': userData['userstats']['E4'],
                        'champion': userData['userstats']['champion']
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
            newData['userstats']['champion'] = "false"
    delete(user)
    with open('badges.json', 'w') as file:
        file.write(json.dumps(data, indent=4))
    writejson(newData)


def delete(user):
    with open('badges.json') as jsonData:
        data = json.load(jsonData)
    deleteindex = 0
    for userDataToDelete in data['challengers']:
        userID = userDataToDelete['userid']
        if userID == user:
            break
        deleteindex = deleteindex + 1

    names_to_remove = [user]

    for element in data['challengers']:
        if element['userid'] in names_to_remove:
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


# region IF checks/ simple checks
def channelCheck(channel) -> bool:
    commandCheck = False
    if channel == 'gym-challenge':
        commandCheck = True
    if channel == 'test':
        commandCheck = True
    if channel == 'gym-leader':
        commandCheck = True
    if channel == 'raid-chat-general':
        commandCheck = True
    return commandCheck


def leaderCheck(authorID) -> bool:
    commandCheck = False
    for leader in currentLeaders():
        if authorID == leader:
            commandCheck = True
    return commandCheck


def giveCheck(lowerCaseMSG) -> bool:
    commandCheck = False
    if lowerCaseMSG[1] == 'g':
        if lowerCaseMSG[2] == 'i':
            if lowerCaseMSG[3] == 'v':
                if lowerCaseMSG[4] == 'e':
                    if lowerCaseMSG[5] == ' ':
                        commandCheck = True
                        return commandCheck
    return commandCheck


def joinCheck(lowerCaseMSG) -> bool:
    commandCheck = False
    if lowerCaseMSG[1] == 'j':
        if lowerCaseMSG[2] == 'o':
            if lowerCaseMSG[3] == 'i':
                if lowerCaseMSG[4] == 'n':
                    commandCheck = True
                    return commandCheck
    return commandCheck


def resetCheck(lowerCaseMSG) -> bool:
    commandCheck = False
    if lowerCaseMSG[1] == 'r':
        if lowerCaseMSG[2] == 'e':
            if lowerCaseMSG[3] == 's':
                if lowerCaseMSG[4] == 'e':
                    if lowerCaseMSG[5] == 't':
                        if lowerCaseMSG[6] == ' ':
                            commandCheck = True
                            return commandCheck
    return commandCheck


def scoreCheck(lowerCaseMSG) -> bool:
    commandCheck = False
    if lowerCaseMSG[1] == 's':
        if lowerCaseMSG[2] == 'c':
            if lowerCaseMSG[3] == 'o':
                if lowerCaseMSG[4] == 'r':
                    if lowerCaseMSG[5] == 'e':
                        commandCheck = True
                        return commandCheck
    return commandCheck


def eliteFourCheck(lowerCaseMSG) -> bool:
    commandCheck = False
    if lowerCaseMSG[1] == 'e':
        if lowerCaseMSG[2] == '4':
            commandCheck = True
            return commandCheck
    return commandCheck


def champCheck(lowerCaseMSG) -> bool:
    commandCheck = False
    if lowerCaseMSG[1] == 'c':
        if lowerCaseMSG[2] == 'h':
            if lowerCaseMSG[3] == 'a':
                if lowerCaseMSG[4] == 'm':
                    if lowerCaseMSG[5] == 'p':
                        commandCheck = True
                        return commandCheck
    return commandCheck


def helpCheck(lowerCaseMSG) -> bool:
    commandCheck = False
    if lowerCaseMSG[1] == 'c':
        if lowerCaseMSG[2] == 'o':
            if lowerCaseMSG[3] == 'm':
                if lowerCaseMSG[4] == 'm':
                    if lowerCaseMSG[5] == 'a':
                        if lowerCaseMSG[6] == 'n':
                            if lowerCaseMSG[7] == 'd':
                                if lowerCaseMSG[8] == 's':
                                    commandCheck = True
                                    return commandCheck
    if lowerCaseMSG[1] == 'h':
        if lowerCaseMSG[2] == 'e':
            if lowerCaseMSG[3] == 'l':
                if lowerCaseMSG[4] == 'p':
                    commandCheck = True
                    return commandCheck
    return commandCheck


def usernameCheck(username) -> bool:
    commandCheck = False
    substring = "<@"

    if substring in username:
        commandCheck = True
        return commandCheck
    return commandCheck


def usernameSplit(username) -> str:
    userSplit1 = username.split("<@")
    userSplit2 = userSplit1[1].split(">")
    userID = userSplit2[0]
    return userID


# endregion
def logUserMessage(author, message, channel):
    username = str(author)
    channel = str(channel)
    # Debug printing
    print(f"{username} said: '{message}' ({channel})")
