path = []
path += [d for d in os.environ.get('NLTK_DATA', str('')).split(os.pathsep) if d]
if os.path.expanduser('~/') != '~/':
    path.append(os.path.expanduser(str('~/nltk_data')))

if sys.platform.startswith('win'):
path += [
        str(r'C:\nltk_data'), str(r'D:\nltk_data'), str(r'E:\nltk_data'),
        os.path.join(sys.prefix, str('nltk_data')),
        os.path.join(sys.prefix, str('lib'), str('nltk_data')),
        os.path.join(os.environ.get(str('APPDATA'), str('C:\\')), str('nltk_data'))
    ]
else:
    path += [
        str('/usr/share/nltk_data'),
        str('/usr/local/share/nltk_data'),
        str('/usr/lib/nltk_data'),
        str('/usr/local/lib/nltk_data')
    ]
