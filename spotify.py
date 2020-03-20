


import sys
import spotipy
import spotipy.util as util
import json

# export SPOTIPY_CLIENT_ID='7f77cfcbd657468cac080e702dd22954'
# export SPOTIPY_CLIENT_SECRET='193bc9cc711e42f7b610a02bc0f4c6e8'
# export SPOTIPY_REDIRECT_URI='http://localhost/'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

class spotify:

    scope = 'playlist-modify-public'

    def __init__(self):
        self.token = util.prompt_for_user_token(username, self.scope)
        self.sp = spotipy.Spotify(auth=self.token)
        self.me = self.sp.me()['id']
        print("Logged into spotify with %s username" % self.me)

    def exactSearchPlaylist(self,name):
        results = self.sp.search(name,limit=10,offset=0,type="playlist")
        if results['playlists']['items']:
            # Check only the first result
            # In my case I expect the first result to 
            # be scrictly the one i'm looking for.
            result = results['playlists']['items'][0]
            if result["name"] == name:
                return result
            else:
                return None

    def exactSearchTrack(self,name):
        results = self.sp.search(name,limit=10,offset=0,type="track")
        if results['tracks']['items']:
            return results['tracks']['items'][0]
        else:
            return None
            #print(json.dumps(t, indent=2, sort_keys=True))

    def createPlaylist(self,name):
        return self.sp.user_playlist_create(self.me, name, public=True, description='')

    def addTracksToPlaylist(self, playlist, tracks):
        self.sp.user_playlist_add_tracks(self.me, playlist, tracks, position=None)

if __name__ == "__main__":
    s = spotify()
    t = s.exactSearchTrack("face of light rival sons")
    print(t)

    


