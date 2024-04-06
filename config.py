# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = 'smart'
# c.colors.webpage.darkmode.grayscale.images = False

# config.source('themes/qute-city-lights/city-lights-theme.py')

c.editor.command = ["alacritty", "-e", "nvim", "{file}"]

c.session.default_name = 'nitaicharan'

# c.spellcheck.languages = ['en-US', 'pt-BR']

c.statusbar.show = "in-mode"

c.tabs.background = True
c.tabs.close_mouse_button = 'middle'
c.tabs.close_mouse_button_on_bar = 'new-tab'
c.tabs.show = "always"
c.tabs.favicons.scale = 1.0

c.url.default_page = 'https://www.google.com/'
c.url.searchengines = {
    'DEFAULT': 'https://www.google.com.br/search?q={}',
    'gg': 'https://www.google.com/search?q={}',
    'dd': 'https://duckduckgo.com/?q={}',
    'fv': 'https://forvo.com/search/{}/',
    'yt': 'https://www.youtube.com/results?search_query={}',
    'gten': 'https://translate.google.com/?sl=pt&tl=en&text={}',
    'tgen': 'https://translate.google.com/?sl=en&tl=pt&text={}',
    'gtes': 'https://translate.google.com/?sl=pt&tl=es&text={}',
    'tges': 'https://translate.google.com/?sl=es&tl=pt&text={}',
}

# Unbinds
config.unbind('xO')
config.unbind('f')
config.unbind('F')
config.unbind('d')
config.unbind('<Ctrl+w>')

# Whout prefix
config.bind(':', 'cmd-set-text :')

config.bind('<f12>', 'devtools')

config.bind('ff', 'hint all')
config.bind('fi', 'hint images')
config.bind('fl', 'hint links')
config.bind('fh', 'hint all hover')
config.bind('fp', 'hint inputs')

config.bind('fF', 'hint all tab')
config.bind('fI', 'hint images tab')
config.bind('fL', 'hint links tab')
config.bind('fP', 'hint inputs tab')

config.bind('<Ctrl+Shift++>', 'zoom-in')
config.bind('<Ctrl+->', 'zoom-out')
config.bind('<Ctrl+0>', 'zoom')

# Moviments
config.bind('<Ctrl+d>', 'scroll-px 0 300')
config.bind('<Ctrl+j>', 'completion-item-focus next', mode='command')
config.bind('<Ctrl+k>', 'completion-item-focus prev', mode='command')
config.bind('<Ctrl+i>', 'forward')
config.bind('<Ctrl+o>', 'back')
config.bind('<Ctrl-u>', 'scroll-px 0 -300')

config.bind('<Shift+k>', 'tab-prev')
config.bind('<Shift+j>', 'tab-next')

config.bind('<Space><Tab>', 'tab-focus last')
config.bind('<Space>?', 'bind')

#  Buffers
config.bind('<Space>bd', 'tab-close')
config.bind('<Space>bb', 'tab-select')
config.bind('<Space>bu', 'undo')
config.bind('<Space>bn', 'tab-next')
config.bind('<Space>bp', 'tab-prev')
config.bind('<Space>bNn', 'open -w')
config.bind('<Space>bU', 'undo --window')
config.bind('<Space>bTp', 'tab-pin')

# Files
config.bind('<Space>fr', 'history --tab')
config.bind('<Space>fed', 'config-edit')
config.bind('<Space>feR', 'config-source')

# Help
config.bind('<Space>hh', 'help --tab')

# Insert
config.bind('<Space>iPP', 'spawn --userscript qute-pass --dmenu-invocation dmenu')
config.bind('<Space>iPu', 'spawn --userscript qute-pass --username-only --dmenu-invocation dmenu')
config.bind('<Space>iPp', 'spawn --userscript qute-pass --password-only --dmenu-invocation dmenu')
config.bind('<Space>iPp', 'spawn --userscript qute-pass --otp-only --dmenu-invocation dmenu')

# Window
config.bind('<Space>wpm', 'messages')
config.bind('<Space>wv', 'tab-clone --window')
config.bind('<Space>wqq', 'close')
config.bind('<Space>wpP', 'clear-messages')

# Quit
config.bind('<Space>qq', 'quit')

config.bind('<Space>xOm', 'hint images')
config.bind('<Space>xOM', 'hint images tab')
config.bind('<Space>xOi', 'hint inputs')
config.bind('<Space>xOI', 'hint inputs --first')
