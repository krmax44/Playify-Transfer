# Playify Transfer
Transfers Spotify playlists to Google Play Music. It is an addition to Playify.

## Setup
Download the [latest release](https://github.com/krmax44/playify-transfer/releases/latest) and unzip it. Firstly, open `password.exe` and set a password. **Without setting a password, the Transfer app will not start.** You will need the password later. Then open `playify-transfer.exe`.

Now open a playlist link. You can take (this one) [https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMDoHDwVN2tF] for testing. Click on the red transfer icon in the bottom right corner to begin the transfer progress.

Transfer needs to run everytime you need to transfer a playlist. If you wish it runs always by default, right-click `playify-transfer-invisible.exe` and select "Create shortcut". Press <kbd>Win + R</kbd>, type in `shell:startup` and press enter. A explorer window will open. Now copy the created shortcut into this folder, double click it and it will always be running.

## API documentation

All commands are sent in JSON format via WebSocket to `ws://localhost:5673`.

### listing playlists
```
{
  "q": "get_playlists",
  "auth": "your transfer password",
  "email": "your gmail address",
  "password": "your google password"
}
```
will return an array of objects with playlist names and ids.

### transfering playlists
```
{
  "q": "transfer_playlist",
  "auth": "your transfer password",
  "email": "your gmail address",
  "password": "your google password",
  "tracks": ["Sample Song - Sample Artist", "Sample Song - Sample Artist"],
  "new_playlist": true,
  "playlist": "new playlist name"
}
```
`new_playlist` can be true or false; if false, `playlist` must contain a playlist id.
