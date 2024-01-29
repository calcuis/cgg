#!/usr/bin/env python3

__version__="0.0.1"

def __init__():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('tag', help='tag(s) available: c, cpp, g, gpp; or menu')
    args = parser.parse_args()
    if args.tag=="c":
        # from .c import *
        from gguf_connector import c
    elif args.tag=="cpp":
        # from .cpp import *
        from gguf_connector import cpp
    elif args.tag=="g":
        # from .g import *
        from gguf_connector import g
    elif args.tag=="gpp":
        # from .gpp import *
        from gguf_connector import gpp
    elif args.tag=="menu":
        # from .gpp import *
        from gguf_connector import menu
