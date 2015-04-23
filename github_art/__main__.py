import optparse

from github import Github


parser = optparse.OptionParser(conflict_handler="resolve")
parser.add_option('--string', action='store', type='string', \
                  dest='string', default=None, \
                  help='Art string for Github Contributions table'
)
parser.add_option('--dictionary', action='store', type='string', \
                  dest='dictionary', default='letters', \
                  help='Letter dictionary '
)
parser.add_option('--project', action='store', type='string', \
                  dest='project', help='Github git URL'
)
parser.add_option('--path', action='store', type='string', \
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
if len(options.project) > 0:
    git.set_account(options.project)
git.run()