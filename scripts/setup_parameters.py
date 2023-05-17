#!/usr/bin/env python3
import json
import sys

import .common as common
from .cli import Cli, Type
from .logs import logs
from .settings import init

def declare_cli():
    cli = Cli()
    cli.add_argument('--ci', default='github', choices=['jenkins', 'github'], help='CI environment')

    scenarios = ['base.json', 'short.json', None]
    cli.add_argument('--scenario', nargs='?', type=Type.str, choices=scenarios, help='Autotest scenario')
    cli.add_argument('--platform', nargs='?', type=Type.json, help='Platform (JSON)')
    cli.add_argument('--gris-branch', nargs='?', type=Type.str, choices=['DEV', 'MAIN5', 'MAIN4', None],
                     help='gris branch')
    cli.add_argument('--review', nargs='?', type=Type.int, help='Swarm review ID')
    cli.add_argument('--pass-url', nargs='?', type=Type.url, help='Swarm pass URL')
    cli.add_argument('--fail-url', nargs='?', type=Type.url, help='Swarm fail URL')

    cli.add_command(func=do_gris, help='Setup gris parameters')
    cli.add_command(func=do_swarm, help='Setup SWARM parameters')
    return cli


def do_gris(args):
    logs.log(f'gris_params = {json.dumps(gris_params, indent=2)}')
    print(f'::set-output name=gris_params::{json.dumps(gris_params)}')


def do_swarm(args):
    swarm_params = {'pass_url': args.pass_url if args.pass_url else '',
                    'fail_url': args.fail_url if args.fail_url else '',
                    }
    logs.log(f'swarm_params = {json.dumps(swarm_params, indent=2)}')
    print(f'::set-output name=swarm_params::{json.dumps(swarm_params)}')


@common.return_exit_code
def main():
    cli = declare_cli()
    args = cli.parse_args()
    init(args.ci)

    cli.handle_commands(['gris', 'swarm'])


if __name__ == '__main__':
    sys.exit(main())
