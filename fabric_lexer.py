from pygments.lexer import RegexLexer, bygroups
from pygments.token import Text, Name, Generic, Whitespace, Operator

class FabLexer(RegexLexer):
    name = 'FAB'
    aliases = ['fab', 'fabric']
    filenames = ['*.txt', '*.log']

    tokens = {
        'root': [
            (r'\s+', Whitespace), # matches all whitespaces
            (r'(\[[^\[]+\])', Name.Namespace), # matches [host1]
            (r'(Warning: )(.*?)$', bygroups(Generic.Deleted, Text)),
            (r'(Fatal error: )(.*?)$', bygroups(Generic.Error, Text)),
            (r'(run: )(.*?)$', bygroups(Generic.Inserted, Text)),
            (r'(Executing task )\'(.+)(\.)(.+)\'$', #matches Executing task 'some_namespace.some_task' 
                bygroups(Generic.Strong, Name.Variable, Operator, Name.Attribute)),
            (r'(Executing task )\'(.+)\'$', # matches Executing task 'some_task'
                bygroups(Generic.Strong, Name.Variable)),
            (r'.', Text), # everything else
        ]
    }
