import json
import os.path
import sys
# thanks to these awesome open source projects! ♥
from gmusicapi import Mobileclient
from websocket_server import WebsocketServer

sp_playlist_uri = ""
sp_playlist_name = ""

if not os.path.isfile("password.txt"):
	sys.exit()
else:
	password = open("password.txt", "r").read()

def receiveWS(c, s, msg):
	data = json.loads(msg.encode("latin-1"))
	print(data)
	try:
		auth = data["auth"]
	except NameError:
		auth = False
	
	if auth == password:
		if data["q"] == "transfer_playlist":
			api = Mobileclient(False)
			if api.login(data["email"], data["password"], Mobileclient.FROM_MAC_ADDRESS):
				if data["new_playlist"] is True:
					playlist = api.create_playlist(data["playlist"], "tranfered with Playify")
				else:
					playlist = data["playlist"]
				
				for track in data["tracks"]:
					print(track)
					result = api.search(track)
					try:
						res = result["song_hits"][0]["track"]["storeId"]
					except NameError:
						res = False
					except IndexError:
						res = False
						
					if res:
						pres = api.add_songs_to_playlist(playlist, res)
						server.send_message_to_all(json.dumps({
							"q": "progress",
							"error": False,
							"track": track,
							"id": res
						}))
					else:
						server.send_message_to_all(json.dumps({
							"q": "progress",
							"error": True,
							"track": track
						}))
		
		elif data["q"] == "get_playlists":
			api = Mobileclient(False)	
			if api.login(data["email"], data["password"], Mobileclient.FROM_MAC_ADDRESS):
				playlists = api.get_all_playlists()
				array = []
				for playlist in playlists:
					array.append({
						"name": playlist["name"],
						"id": playlist["id"]
					})
					
				server.send_message_to_all(json.dumps({
					"q": "playlists",
					"lists": array
				}))
		
		else:
			server.send_message_to_all(json.dumps({
				"q": "auth",
				"error": False
			}))
	else:
		server.send_message_to_all(json.dumps({
			"q": "auth",
			"error": True
		}))

PORT=5673
server = WebsocketServer(PORT)
server.set_fn_message_received(receiveWS)
server.run_forever()
