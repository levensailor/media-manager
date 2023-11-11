# media-manager
Unrar's movies and removes rar files if a movie file exists
Runs every 30 minutes by default

### environment

BASE_DIRECTORY = the directory all your movie folders are in. Default = "media"

DELETE_SIZE = the minimum size a video file must be (in MB) to consider it extracted. Default = 200

*Because some movies download with a trailer or sample included, we need to ensure a large video file exists

### to run

docker pull ghcr.io/levensailor/media-manager
docker run -d --restart=unless-stopped -e DELETE_SIZE=500 -v /media:/media media-manager
