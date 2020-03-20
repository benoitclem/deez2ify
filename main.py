
import deezer
import re
from spotify import spotify


deezerClient = deezer.Client()
spotifyClient = spotify()
importFails = []

#search for public stuffs

playlists = {"Showgun":7300472344,
            "Showgun II":7300772364,
            "Showgun III":7300796284,
            "Showgun IV":7300846084,
            "Showgun V":7369522804}

for playlistName in playlists:
    playlistId = playlists[playlistName]
    rockPlaylistName = "🤘- %s" % playlistName
    # Check if playlist exists in spotify 
    spotifyPlaylist = spotifyClient.exactSearchPlaylist(rockPlaylistName)
    if not spotifyPlaylist:
        print("/!\ - %s does not exist do create it" % rockPlaylistName)
        spotifyPlaylist = spotifyClient.createPlaylist(rockPlaylistName)

    print(spotifyPlaylist)

    deezerPlaylist = deezerClient.get_playlist(playlistId)

    tracksToAdd = []

    for track in deezerPlaylist.tracks:
        trackSearchName = "%s %s" %(track.title, track.artist.name)
        trackSearchName = re.sub(r" ?\([^)]+\)", "", trackSearchName)
        print("- Searching for track: %s" % trackSearchName)
        trackToAdd = spotifyClient.exactSearchTrack(trackSearchName)
        if trackToAdd:
            tracksToAdd.append(trackToAdd["id"])
        else:
            importFails.append("[%s]:%s" %(playlistName,trackSearchName))
 
    if tracksToAdd:
        print(tracksToAdd)
        print("- Inserting %d new tracks to %s" %(len(tracksToAdd),playlistName))
        spotifyClient.addTracksToPlaylist(spotifyPlaylist["id"],tracksToAdd)

print("/!\ Import done, got failure on %d titles:" % (len(importFails)))

for importFail in importFails:
    print("- %s" % importFail)

