from flask import Flask
from flask import jsonify
from flask import request
import requests
import json


app = Flask(__name__)


@app.route('/')
def index():
  def creatorCheck(): #Checks if im on the Tempus network
    if steamID['steamid'] == 'STEAM_0:0:51919992':
      print(hostname)
      print(steamID['name'], "is currently failing", map)
      return True
    return False
  userCheck = requests.get('https://tempus2.xyz/api/v0/servers/statusList')
  serverList = json.loads(userCheck.content)

    #user = input("Enter the SteamID: ")
  user = request.args.get('SteamID')#user = input(steamID)
  #if user.lower() == 'quit':
 # quitcondition = True
 # continue


  # validation of steam user
  if 'STEAM' not in user:
    #continue
    print('Not a valid SteamID ')
    return "not valid SteamID"

  gameInfoCount = 0

  loopstop = 0

  for server in serverList:
    gameInfoCount += 1 #counts Nulls aswell to get accurate number for list
    if loopstop == 1:
      break
    if server['game_info'] != None:
      #print(server['game_info']['currentMap'])
      for user1 in server['game_info']['users']:

        if user1['steamid'] == user:

          foundServer = serverList[(gameInfoCount -1)]
          hostname = serverList[(gameInfoCount - 1)]['game_info']['hostname']
          map = serverList[(gameInfoCount - 1)]['game_info']['currentMap']

          for steamID in foundServer['game_info']['users']:
            for steamID in foundServer['game_info']['users']:

              if steamID['steamid'] == user:
                #if creatorCheck() == True:
                  #return f'{hostname}\n{steamID["name"]} is currently failing {map}'
                  #Checks if I'm in the server. Will jsonify later
                  #break
                print(hostname)
                print(steamID['name'], "is currently destroying", map)
                loopstop = 1
                #STEAM_0:0:525196361 my steamID
                all_data = [{"User" : steamID, "Server": foundServer}]
                # All data from the server the player was found on
                # User dict has all information about the user
                # Server dict has all data relevant to the server the player was found on
                # Including other players
                # If returned will require additional sorting but all data is there
                relevent_data = [{"User" : steamID["name"], "Server": hostname}]
                # Data relevant to the player that was searched for
                # User dict has just the name of the player
                # Server dict has just the name of the server
                # If returned no additional sorting would be required
                print(f'\n \n {relevent_data} \n \n {all_data} \n \n')
                return 'user online'
  return 'user offline'

app.run(host='0.0.0.0', port=81)










#f'{hostname}\n{steamID["name"]} is currently failing {map}'
#jump.tf (NY) | All Maps | Tempus Network RoastyMyToasty4200 is currently destroying jump_apex_b1