import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8840114975:AAFucalzGzQso1AoDAS_0qXdIBAjd7z0QE4")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 34446649))
    API_HASH = os.environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    VIDEO_FORMATS = ["mp4", "mkv", "mov", "m4v", "avi", "unknown_video"]
    AUDIO_FORMATS = ["mp3", "flac", "m4a", "wav"]
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "7892805795"))
    ADMINS = int(os.environ.get("ADMINS", "7892805795"))
    SESSION_NAME = "URLUPLOADERBOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Anujedit")
    MAX_RESULTS = "50"
    #update channel
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1003873749415")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003971269572")
    #log channel
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1003873749415")
    
