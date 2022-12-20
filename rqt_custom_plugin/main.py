#!/usr/bin/env python

import sys

from rqt_gui.main import Main

PLUGIN = 'rqt_custom_plugin'
def main():
    main = Main(filename=PLUGIN)
    sys.exit(main.main(standalone=PLUGIN))

if __name__ == "__main__":
    main()
