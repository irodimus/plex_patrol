from decouple import config, Csv

DEBUG = config('DEBUG', False, cast=bool)
SERVER_URL = config('SERVER_URL')
SERVER_TOKEN = config('SERVER_TOKEN')
SERVER_NAME = config('SERVER_NAME')
CHECK_INTERVAL = config('CHECK_INTERVAL', 60, cast=int)

KICK_VIDEO_TRANSCODES = config('KICK_VIDEO_TRANSCODES', False, cast=bool)
KICK_AUDIO_TRANSCODES = config('KICK_AUDIO_TRANSCODES', False, cast=bool)
KICK_PAUSED_TRANSCODES = config('KICK_PAUSED_TRANSCODES', False, cast=bool)
KICK_PAUSED_DIRECTPLAY = config('KICK_PAUSED_DIRECTPLAY', False, cast=bool)
KICK_PAUSED_GRACE_MINS = config('KICK_PAUSED_GRACE_MINS', 5, cast=int)
KICK_CLIENT_PLAYERS = config('KICK_CLIENT_PLAYERS', [], cast=Csv())

KICK_PAUSED_MESSAGE = config('KICK_PAUSED_MESSAGE', 'You are not allowed to pause a stream for that long... cya!')
KICK_TRANSCODE_MESSAGE = config('KICK_TRANSCODE_MESSAGE',
                                'You are not allowed to transcode streams, use a better client!')
KICK_PLAYER_MESSAGE = config('KICK_PLAYER_MESSAGE',
                             'You are not allowed to use this trash player. '
                             'Use the official software from www.plex.tv/downloads -> Get An App!!!')

WHITELISTED_USERS = config('WHITELISTED_USERS', [], cast=Csv())