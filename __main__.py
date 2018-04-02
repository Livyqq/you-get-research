#!/usr/bin/env python

import getopt  #getopt:解析命令行参数
import os
import platform
import sys
from .version import script_name, __version__
from .util import git, log #util(utility):通用工具

_options = [
    'help',
    'version',
    'gui',#gui:图形用户界面 (graphic user interface)
    'force',#force:强制
    'playlists',#playlist:播放列表
]
_short_options = 'hVgfl'

_help = """Usage: {} [OPTION]... [URL]...
TODO
""".format(script_name)

# TBD:待定（To Be Determined）
def main_dev(**kwargs):
    """Main entry point.
    you-get-dev
    """

    # Get (branch, commit) if running from a git repo.
    head = git.get_head(kwargs['repo_path'])

    # Get options and arguments.
    try:
        opts, args = getopt.getopt(sys.argv[1:], _short_options, _options)
    except getopt.GetoptError as e:
        log.wtf("""
    [Fatal] {}.
    Try '{} --help' for more options.""".format(e, script_name))

    if not opts and not args:
        # Display help.
        print(_help)
        # Enter GUI mode.
        #from .gui import gui_main
        #gui_main()
    else:
        conf = {}
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                # Display help.
                print(_help)

            elif opt in ('-V', '--version'):#elif:else if
                # Display version.
                log.println("you-get:", log.BOLD)#BOLD:粗体
                log.println("    version:  {}".format(__version__))
                if head is not None:
                    log.println("    branch:   {}\n    commit:   {}".format(*head))#branch:分支
                else:
                    log.println("    branch:   {}\n    commit:   {}".format("(stable)", "(tag v{})".format(__version__)))#tag:标记

                log.println("    platform: {}".format(platform.platform()))#println:换行打印
                log.println("    python:   {}".format(sys.version.split('\n')[0]))

            elif opt in ('-g', '--gui'):
                # Run using GUI.
                conf['gui'] = True

            elif opt in ('-f', '--force'):
                # Force download.
                conf['force'] = True

            elif opt in ('-l', '--playlist', '--playlists'):
                # Download playlist whenever possible.
                conf['playlist'] = True

        if args:
            if 'gui' in conf and conf['gui']:#conf:配置文件
                # Enter GUI mode.
                from .gui import gui_main
                gui_main(*args, **conf)
            else:
                # Enter console mode.
                from .console import console_main
                console_main(*args, **conf)

def main(**kwargs):
    """Main entry point.
    you-get (legacy)
    """
    from .common import main
    main(**kwargs)

if __name__ == '__main__':
    main()
