import os
from pathlib import Path

__all__ = [
    'CfgDict',
    'path',
    'settings',
    'init'
]


class CfgDict(dict):
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value


# In-project paths
path = CfgDict()
path.root = Path(__file__).resolve().parents[2]
path.build = Path(path.root, 'build')
path.emulator = Path(path.build, 'emulator')
path.tests_summary = Path(path.build, 'tests_summary')
path.status = Path(path.build, 'status')

settings = CfgDict()
settings.path = path
settings.swarm_url = 'https://site.net'

github = CfgDict()
github.my_port = '111.222.233.244:5678'  # my server
github.my_client = 'my_server'

def init(ci):
    settings.update(dict(globals()[ci]))


if __name__ == '__main__':
    # Usage: python -m lib.settings
    from pprint import pprint

    print('GITHUB settings')
    init('github')
    pprint(settings)
