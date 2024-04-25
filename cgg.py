#!/usr/bin/env python3

__version__="0.2.7"

def __init__():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('tag', help='tag(s) available: c, cpp, g, gpp, go, r or menu')
    args = parser.parse_args()
    if args.tag=="c":
        from gguf_connector import c
    elif args.tag=="cpp":
        from gguf_connector import cpp
    elif args.tag=="g":
        from gguf_connector import g
    elif args.tag=="gpp":
        from gguf_connector import gpp
    elif args.tag=="r":
        from gguf_connector import r
    elif args.tag=="us":
        from gguf_connector import w
    elif args.tag=="menu":
        from gguf_connector import menu
