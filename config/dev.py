from pecan.hooks import TransactionHook, RequestViewerHook
from chacra import models


# Server Specific Configurations
server = {
    'port': '8083',
    'host': '172.18.232.2'
}

# Pecan Application Configurations
app = {
    'root': 'chacra.controllers.root.RootController',
    'modules': ['chacra'],
    'default_renderer': 'json',
    'hooks': [
        TransactionHook(
            models.start,
            models.start_read_only,
            models.commit,
            models.rollback,
            models.clear
        ),
        RequestViewerHook(),
    ],
    'debug': True,
}

logging = {
    'loggers': {
        'root': {'level': 'INFO', 'handlers': ['console']},
        'chacra': {'level': 'DEBUG', 'handlers': ['console']},
        'pecan.commands.serve': {'level': 'DEBUG', 'handlers': ['console']},
        'py.warnings': {'handlers': ['console']},
        '__force_dict__': True
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'color'
        }
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s %(levelname)-5.5s [%(name)s]'
                       '[%(threadName)s] %(message)s')
        },
        'color': {
            '()': 'pecan.log.ColorFormatter',
            'format': ('%(asctime)s [%(padded_color_levelname)s] [%(name)s]'
                       '[%(threadName)s] %(message)s'),
            '__force_dict__': True
        }
    }
}

sqlalchemy = {
    'url': 'postgresql+psycopg2://chacra:pass4root@127.0.0.1/chacra',
    'echo':          True,
    'echo_pool':     True,
    'pool_recycle':  3600,
    'encoding':      'utf-8'
}

# location for storing uploaded binaries
binary_root = '%(confdir)s/public'
repos_root = '%(confdir)s/repos'
distributions_root = '%(confdir)s/distributions'

# When True it will set the headers so that Nginx can serve the download
# instead of Pecan.
delegate_downloads = False

# Basic HTTP Auth credentials
api_user = 'admin'
api_key = 'secret'

# Celery options
# How often (in seconds) the database should be queried for repos that need to
# be rebuilt
polling_cycle = 15

# Once a "create repo" task is called, how many seconds (if any) to wait before actually
# creating the repository
quiet_time = 30


# Use this to define how distributions files will be created per project
distributions = {
    "defaults": {
        "DebIndices": "Packages Release . .gz .bz2",
        "DscIndices": "Sources Release .gz .bz2",
        "Contents": ".gz .bz2",
        "Origin": "RedHat",
        "Description": "",
        "Architectures": "s390x source",
        "Suite": "stable",
        "Components": "main",
        "DDebComponents": "main",
    },
    "ceph": {
        "Description": "Ceph distributed file system",
    },
}
