from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from jinja2 import Markup, evalcontextfilter

from alphabits import app

@evalcontextfilter
@app.template_filter()
def source(eval_context, content):
    lex = get_lexer_by_name('python', stripall=True)
    formatter = HtmlFormatter(linenos=True, cssclass="source")
    result = highlight(content, lex, formatter)
    if eval_context.autoescape:
        result = Markup(result)

    return result
