import optparse

from github import Github

if __name__ == "__main__":
    parser = optparse.OptionParser(conflict_handler="resolve")
    parser.add_option('-s', '--string', action='store', type='string', \
                      dest='string', default=None, \
                      help='Art string for Github Contributions table'
    )
    parser.add_option('-z', '--size', action='store', type='string', \
                      dest='size', default=2, \
                      help='Size of string\'s letters'
    )
    parser.add_option('-a', '--account', action='store', type='string', \
                      dest='account', help='Github git URL'
    )
    parser.add_option('-p', '--path', action='store', type='string', \
                      dest='path', default='../build', \
                      help='Path to github new project'
    )

    options, arguments = parser.parse_args()

    if not options.string:
        parser.error('String not given')

    if not options.path:
        parser.error('Build git path not given')

    if not options.account:
        parser.error('Github git URL not given')

    git = Github(options.string, options.path, options.size)
    git.initialite()
    if len(options.account) > 0:
        git.set_account(options.account)
    git.run()