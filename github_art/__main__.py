import optparse

from github import Github


parser = optparse.OptionParser(conflict_handler="resolve")
parser.add_option('--string', action='store', type='string',
                  dest='string',
                  help='Art string for Github Contributions table')

parser.add_option('--dictionary', action='store', type='string',
                  dest='dictionary', default='alphanumeric',
                  help='Letter dictionary ')

parser.add_option('--path', action='store', type='string',
                  dest='path', help='Path to github new project')

parser.add_option('--project', action='store', type='string',
                  dest='project', help='Github Proejct Name')

parser.add_option('--username', action='store', type='string',
                  dest='username', help='Github Username')

options, arguments = parser.parse_args()

if not options.string:
    parser.error('String not given')

if not options.path:
    parser.error('Build git path not given')

if not options.dictionary:
    parser.error('Github git URL not given')

git = Github(options.string, options.path, options.dictionary)
git.initialite()

if options.username and options.project:
    git.set_account(options.username, options.project)

git.run()
