#!/usr/bin/env python3

__version__="0.4.8"

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
    elif args.tag=="v":
        from gguf_connector import v
    elif args.tag=="r":
        from gguf_connector import r
    elif args.tag=="a":
        from gguf_connector import r2
    elif args.tag=="d":
        from gguf_connector import d2
    elif args.tag=="m":
        from gguf_connector import m2
    elif args.tag=="y":
        from gguf_connector import y
    elif args.tag=="n":
        from gguf_connector import n
    elif args.tag == 't2i':
        from gguf_connector import i2
    elif args.tag == 't2v':
        from gguf_connector import v2
    elif args.tag == 'i2v':
        from gguf_connector import vg2
    elif args.tag == 'flux':
        from gguf_connector import k
    elif args.tag == 'qwen':
        from gguf_connector import q5
    elif args.tag == 'wan':
        from gguf_connector import w2
    elif args.tag == 'ltxv':
        from gguf_connector import x2
    elif args.tag == 'mochi':
        from gguf_connector import m1
    elif args.tag == 'edit':
        from gguf_connector import q8
    elif args.tag == 'docling':
        from gguf_connector import n3
    elif args.tag == 'fastvlm':
        from gguf_connector import f9
    elif args.tag == 'vibevoice':
        from gguf_connector import v6
    elif args.tag == 'gudio':
        from gguf_connector import g2
    elif args.tag=="io":
        from gguf_connector import i
    elif args.tag=="us":
        from gguf_connector import w
    elif args.tag=="org":
        from gguf_connector import o
    elif args.tag=="menu":
        from gguf_connector import menu
