#! /usr/bin/env python
"""
This is a silly program that is used to print out Chuck Norris jokes. If
Chuck Norris jokes aren't your thing you could make a file with motivational
sayings or something and update the configuration and this should still work.
See the example_config.txt for details.
"""
import urllib2
from random import choice
import ConfigParser
import os

def load_config(defaults, location=None, verbose=False):
    """
    Load user configuration from a file.

    :param defaults: a dict with the program defaults
    :param location: a file location to load the config from. This will defaul to ~/.norris
    :param verbose: set this to true if you want to see errors around loading configuration
    """
    user_config = {}
    location = location or os.path.expanduser('~/.norris')
    try:
        config = ConfigParser.ConfigParser()
        config.read(location)
        user_config = dict(config.items('config'))
    except Exception, e:
        if verbose:
            print 'Error when opening user config at {0}: {1}'.format(location, e)
    return dict(defaults, **user_config)

def get_line(url, timeout=.5):
    """
    Hit the passed in url and return a random line of the output.
    """
    return choice(urllib2.urlopen(url, timeout=timeout).readlines()).strip()

def main():
    """
    Run the program printing out the text that is found.
    """
    defaults = {
        'url' : 'http://charliek.github.com/norris/norris.txt',
        'timeout' : .5,
        'verbose' : True
    }
    config = load_config(defaults)
    try:
        line = get_line(config['url'], float(config['timeout']))
        print "{0}".format(line)
    except Exception, e:
        if bool(config['verbose']):
            print 'An error has occurred : {0}'.format(e)

if __name__ == "__main__":
    main()

