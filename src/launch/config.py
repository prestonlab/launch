"""Module to manage cluster configurations."""

import os
import toml


def find_config():
    """Find any available config files."""
    if 'LAUNCH_CONFIG' in os.environ:
        config = os.environ['LAUNCH_CONFIG']
    else:
        config = os.path.join(os.environ['HOME'], '.launch.toml')
    return config


def load_config(config):
    """Attempt to load a config file."""
    if not os.path.exists(config):
        raise IOError(f'Config file does not exist: {config}')

    options = toml.load(config)
    for queue, keys in options.items():
        if 'cores' not in keys:
            keys['cores'] = None
        if 'max-nodes' not in keys:
            keys['max-nodes'] = None
        if 'max-cores' not in keys:
            keys['max-cores'] = None
    return options
