from browser import html, document, window
import javascript

_path = __file__[:__file__.rfind('/')]+'/'

document <= html.LINK(rel="stylesheet",
    href=_path+'css/smoothness/jquery-ui-1.10.3.custom.min.css')

# The scripts must be loaded in blocking mode, otherwise they will not be
# in the Javascript namespace when "import jqui" returns

# laod jQuery and put name 'jQuery' in the global Javascript namespace
javascript.load(_path+'jquery-1.11.2.min.js', ['jQuery'])
javascript.load(_path+'jquery-ui.js')

_jqui = window.jQuery.noConflict(True)

class JQFunction:

    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kw):
        return self.func(kw)

class Element:

    def __init__(self, item):
        self.item = item

    def __getattr__(self, attr):
        res = getattr(self.item, attr)
        if callable(res):
            res = JQFunction(res)
        return res

class jq:

    def __init__(self, *selectors):
        items = []
        for selector in selectors:
            item = _jqui(selector)
            if isinstance(item, list):
                items += [Element(x) for x in item]
            else:
                items.append(Element(item))
        self.items = items
    
    @staticmethod
    def __getitem__(element_id):
        return jq('#'+element_id).items[0]
    
    def __iter__(self):
        return iter(self.items)