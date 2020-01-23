import urllib.request
import urllib.parse
import re
import os

def createNewAccount():
    url = input('Please Insert the link to your dotabuff account here\n')
    savefile = open('url.txt', 'a')
    savefile.write(input('What would you like the name of the account to be? ') + '\n')
    savefile.write(url + '\n')
    savefile.close()

def getUrlsFromTxt():
    urls = {}
    names_and_urls = open('url.txt', 'r').readlines()
    for url in enumerate(names_and_urls):
        key = re.findall(r'(.*?)\n', names_and_urls[url[0] - 1])
        value = re.findall(r'(.*?)\n', names_and_urls[url[0]])
        if url[0] % 2 == 1:
            urls[key[0]] = value[0]
    return urls

def topTen(list):
    newlist = []
    for i in range(10):
        newlist.append(list[i])
    return newlist

def recentlyPlayed(list):
    newlist = []
    for i in range(10,25):
        newlist.append(list[i])
    return newlist

def getOverview(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        }
    
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    return resp.read()

def getNamesFromOverview(respData):
    overviewP = re.findall(r'/heroes/(.*?)">', str(respData))
    overviewP = re.findall(r'heroes/(.*?).jpg', str(overviewP))
    heroes = []
    for hero in overviewP:
        if hero.count('-') > 1:
            whole_name = re.findall(r'(\w*)-', hero)
            heroes.append('{} {}'.format(whole_name[0], whole_name[1]))
        else:
            only_name = re.findall(r'(\w*)-', hero)
            heroes.append(only_name[0])
    return heroes

def getAccounts(dict):
    keys = dict.keys()
    x = 'Available Accounts: '
    for key in keys:
        x = x + '\n{}'.format(key)
    return x

def printMostPlayed(heroes):
        print('Their top ten most played hereos are:')
        mostPlayed = topTen(heroes)
        for i in enumerate(mostPlayed):
            print('{}. {}'.format(i[0] + 1, mostPlayed[i[0]]))    

def printMostRecent(heroes):
        print('Their most recent games were as:')
        mostRecent = recentlyPlayed(heroes)
        for i in enumerate(mostRecent):
            print('{}. {}'.format(i[0] + 1, mostRecent[i[0]]))

def chooseAccount(urls):
    print(getAccounts(urls))
    print('all')
    whatAccount = input('Choose an account to view.\n')
    if whatAccount in urls.keys():
        return whatAccount
    elif whatAccount == 'all':
        return whatAccount
    else:
        return 'Account doesn\'t exist'

    



    
if not os.path.isfile('url.txt'):
    txt = open('url.txt', 'w')
    txt.close()


print('Welcome to the Quick Dota Stats Viewer\n Type a command to start or type help to get a list of commands')

listOfCommands = [
    'accounts',
    'add account',
    'delete all',
    'exit',
    'most played',
    'all stats',
    'stats',
    'recent games'
    ]
listOfCommands.sort()
urls = getUrlsFromTxt()
print(getAccounts(urls))
x = input()
while x.lower() != 'exit':
    urls = getUrlsFromTxt()
    if x == 'help':
        print('List of valid commands: ')
        for command in listOfCommands:
            print(command)
        x = input()
    elif x.lower() == 'accounts':
        print(getAccounts(urls))
        x = input()
    elif x.lower() == 'add account':
        createNewAccount()
        urls = getUrlsFromTxt()
        print(getAccounts(urls))
        x = input()
    elif x.lower() == 'delete all':
        txt = open('url.txt' , 'w')
        txt.close()
        x = input()
    elif x.lower() == 'most played':
        chosenAccount = chooseAccount(urls)
        if chosenAccount == 'all':
            accounts = urls.keys()
            for account in accounts:
                print(account)
                respData = getOverview(urls[account])
                heroes = getNamesFromOverview(respData)
                printMostPlayed(heroes)
        elif chosenAccount in urls.keys():
            respData = getOverview(urls[chosenAccount])
            heroes = getNamesFromOverview(respData)
            printMostPlayed(heroes)
        else: print('account does not exist')
        x = input()
    elif x.lower() == 'recent games':
        chosenAccount = chooseAccount(urls)
        if chosenAccount == 'all':
            accounts = urls.keys()
            for account in accounts:
                print(account)
                respData = getOverview(urls[account])
                heroes = getNamesFromOverview(respData)
                printMostRecent(heroes)
        elif chosenAccount in urls.keys():
            respData = getOverview(urls[chosenAccount])
            heroes = getNamesFromOverview(respData)
            printMostRecent(heroes)
        else: print('account does not exist')
        x = input()
    elif x.lower() == 'stats':
        chosenAccount = chooseAccount(urls)
        if chosenAccount == 'all':
            accounts = urls.keys()
            for account in accounts:
                print(account)
                respData = getOverview(urls[account])
                heroes = getNamesFromOverview(respData)
                printMostPlayed(heroes)
                printMostRecent(heroes)
        else:
            respData = getOverview(urls[chosenAccount])
            heroes = getNamesFromOverview(respData)
            printMostPlayed(heroes)
            printMostRecent(heroes)
        x = input()
    elif x.lower() == 'all stats':
        accounts = urls.keys()
        for account in accounts:
            print(account)
            respData = getOverview(urls[account])
            heroes = getNamesFromOverview(respData)
            printMostPlayed(heroes)
            printMostRecent(heroes)
        x = input()
    else:
        x = input('invalid command\n')
