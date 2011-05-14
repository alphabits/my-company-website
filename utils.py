import os

from jinja2 import Markup, evalcontextfilter
import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from app import app


md = markdown.Markdown(extensions=['my_codehilite'])


@evalcontextfilter
@app.template_filter()
def source(eval_context, content):
    lex = get_lexer_by_name('python', stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass="source")
    result = highlight(content, lex, formatter)
    if eval_context.autoescape:
        result = Markup(result)
    return result


@app.template_filter()
def markdown(content):
    return Markup(md.convert(content))

def get_path(rel_path):
    return os.path.abspath(os.path.dirname(rel_path))
