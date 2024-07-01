# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
config.load_autoconfig(True)

c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = "smart"
# c.colors.webpage.darkmode.grayscale.images = False

# config.source('themes/qute-city-lights/city-lights-theme.py')

c.editor.command = ["alacritty", "-e", "nvim", "{file}"]

c.session.default_name = "default"

# c.spellcheck.languages = ['en-US', 'pt-BR']

c.statusbar.show = "in-mode"
c.scrolling.smooth = True

c.tabs.background = True
c.tabs.close_mouse_button = "middle"
c.tabs.close_mouse_button_on_bar = "new-tab"
c.tabs.show = "always"
c.tabs.favicons.scale = 1.0

c.url.default_page = "https://www.google.com/"
c.url.searchengines = {
    "DEFAULT": "https://www.google.com.br/search?q={}",
    "gg": "https://www.google.com/search?q={}",
    "dd": "https://duckduckgo.com/?q={}",
    "fv": "https://forvo.com/search/{}/",
    "yt": "https://www.youtube.com/results?search_query={}",
    "gtpt:en": "https://translate.google.com/?sl=pt&tl=en&text={}",
    "gten:pt": "https://translate.google.com/?sl=en&tl=pt&text={}",
    "gtpt:es": "https://translate.google.com/?sl=pt&tl=es&text={}",
    "gtes:pt": "https://translate.google.com/?sl=es&tl=pt&text={}",
}

c.colors.completion.category.border.bottom = "#151515"
c.colors.completion.category.border.top = "#151515"
c.colors.completion.category.fg = "white"
c.colors.completion.category.bg = "#151515"
c.colors.completion.even.bg = "#000000"
c.colors.completion.odd.bg = "#000000"
c.colors.completion.fg = ["#BBBBBB", "#BBBBBB", "#BBBBBB"]
c.colors.completion.item.selected.bg = "#151515"
c.colors.completion.item.selected.border.top = "#000000"
c.colors.completion.item.selected.border.bottom = "#000000"
c.colors.completion.item.selected.fg = "#FFFFFF"
c.colors.completion.item.selected.match.fg = "#00FF00"
c.colors.completion.match.fg = "#00A300"
c.colors.completion.scrollbar.bg = "#000000"
c.colors.completion.scrollbar.fg = "#00A300"
c.colors.contextmenu.disabled.bg = None
c.colors.contextmenu.disabled.fg = None
c.colors.contextmenu.menu.bg = None
c.colors.contextmenu.menu.fg = None
c.colors.contextmenu.selected.bg = None
c.colors.contextmenu.selected.fg = None
c.colors.downloads.bar.bg = "black"
c.colors.downloads.error.bg = "red"
c.colors.downloads.error.fg = "white"
c.colors.downloads.start.bg = "#0000aa"
c.colors.downloads.start.fg = "white"
c.colors.downloads.stop.bg = "#00aa00"
c.colors.downloads.stop.fg = "white"
c.colors.downloads.system.bg = "none"
c.colors.downloads.system.fg = "none"
c.colors.hints.bg = "#101010"
c.colors.hints.fg = "#00A300"
c.colors.hints.match.fg = "#00A300"
c.colors.keyhint.bg = "#000000"
c.colors.keyhint.fg = "#FFFFFF"
c.colors.keyhint.suffix.fg = "#00FF00"
c.colors.messages.error.bg = "red"
c.colors.messages.error.border = "#bb0000"
c.colors.messages.error.fg = "white"
c.colors.messages.info.bg = "black"
c.colors.messages.info.border = "#333333"
c.colors.messages.info.fg = "white"
c.colors.messages.warning.bg = "darkorange"
c.colors.messages.warning.border = "#d47300"
c.colors.messages.warning.fg = "black"
c.colors.prompts.bg = "#444444"
c.colors.prompts.border = "1px solid gray"
c.colors.prompts.fg = "white"
c.colors.prompts.selected.bg = "grey"
c.colors.prompts.selected.fg = "#00FF00"
c.colors.statusbar.caret.bg = "purple"
c.colors.statusbar.caret.fg = "white"
c.colors.statusbar.caret.selection.bg = "#a12dff"
c.colors.statusbar.caret.selection.fg = "white"
c.colors.statusbar.command.bg = "black"
c.colors.statusbar.command.fg = "white"
c.colors.statusbar.command.private.bg = "darkslategray"
c.colors.statusbar.command.private.fg = "white"
c.colors.statusbar.insert.bg = "#151515"
c.colors.statusbar.insert.fg = "#FFFFFF"
c.colors.statusbar.normal.bg = "black"
c.colors.statusbar.normal.fg = "white"
c.colors.statusbar.passthrough.bg = "darkblue"
c.colors.statusbar.passthrough.fg = "white"
c.colors.statusbar.private.bg = "#666666"
c.colors.statusbar.private.fg = "white"
c.colors.statusbar.progress.bg = "white"
c.colors.statusbar.url.error.fg = "orange"
c.colors.statusbar.url.fg = "white"
c.colors.statusbar.url.hover.fg = "#00A300"
c.colors.statusbar.url.success.http.fg = "white"
c.colors.statusbar.url.success.https.fg = "lime"
c.colors.statusbar.url.warn.fg = "yellow"
c.colors.tabs.bar.bg = "#000000"
c.colors.tabs.indicator.error = "#ff0000"
c.colors.tabs.indicator.start = "#0000aa"
c.colors.tabs.indicator.stop = "#00aa00"
c.colors.tabs.indicator.system = "none"
c.colors.tabs.odd.bg = "#000000"
c.colors.tabs.odd.fg = "#BBBBBB"
c.colors.tabs.pinned.even.bg = "#000000"
c.colors.tabs.pinned.even.fg = "#BBBBBB"
c.colors.tabs.pinned.odd.bg = "#000000"
c.colors.tabs.pinned.odd.fg = "#BBBBBB"
c.colors.tabs.pinned.selected.even.bg = "#151515"
c.colors.tabs.pinned.selected.even.fg = "#FFFFFF"
c.colors.tabs.pinned.selected.odd.bg = "#151515"
c.colors.tabs.pinned.selected.odd.fg = "#FFFFFF"
c.colors.tabs.selected.even.bg = "#151515"
c.colors.tabs.selected.even.fg = "#FFFFFF"
c.colors.tabs.selected.odd.bg = "#151515"
c.colors.tabs.selected.odd.fg = "#FFFFFF"
c.colors.tooltip.bg = None
c.colors.tooltip.fg = None
c.colors.webpage.bg = "white"

# Unbinds
config.unbind("xO")
config.unbind("f")
config.unbind("m")
config.unbind("F")
config.unbind("d")
config.unbind("<Ctrl+w>")
config.unbind("<Ctrl+n>")
config.unbind("<Ctrl+p>")
config.unbind("<Ctrl+e>", mode="command")
config.unbind("<Tab>", mode="command")

# Whout prefix
config.bind(":", "cmd-set-text :")

config.bind("<f12>", "devtools")

config.bind("ff", "hint all")
config.bind("fF", "hint all tab")
config.bind("fi", "hint images")
config.bind("fI", "hint images tab")
config.bind("fl", "hint links")
config.bind("fL", "hint links tab")
config.bind("fh", "hint all hover")
config.bind("fp", "hint inputs")
config.bind("fP", "hint inputs tab")

config.bind("<Ctrl+Shift++>", "zoom-in")
config.bind("<Ctrl+->", "zoom-out")
config.bind("<Ctrl+0>", "zoom")

# Moviments
config.bind("<Ctrl+d>", "scroll-px 0 300")
config.bind("<Ctrl+i>", "forward")
config.bind("<Ctrl+o>", "back")
config.bind("<Ctrl-u>", "scroll-px 0 -300")
config.bind("<Ctrl+x>", "completion-item-del", mode="command")

config.bind("<Shift+k>", "tab-prev")
config.bind("<Shift+j>", "tab-next")

config.bind("<Space><Tab>", "tab-focus last")
config.bind("<Space>?", "bind")

for i in range(0, 10):
    config.bind(str(i), f"cmd-set-text :tab-select {i}", mode="normal")

#  Buffers
config.bind("<Space>bb", "tab-select")
config.bind("<Space>bd", "tab-close")
config.bind("<Space>bn", "tab-next")
config.bind("<Space>bNn", "open --window")
config.bind("<Space>bp", "tab-prev")
config.bind("<Space>bu", "undo")
config.bind("<Space>bU", "undo --window")
config.bind("<Space>bTp", "tab-pin;;tab-move")

# Files
config.bind("<Space>fr", "history --tab")
config.bind("<Space>fbb", "bookmark-list")
config.bind("<Space>fba", "bookmark-add")
config.bind("<Space>fbd", "bookmark-del")
config.bind("<Space>fed", "config-edit")
config.bind("<Space>feR", "config-source")

# Help
config.bind("<Space>hh", "help --tab")

# Insert
config.bind("<Space>iPP", "spawn --userscript qute-pass --dmenu-invocation dmenu")
config.bind(
    "<Space>iPu",
    "spawn --userscript qute-pass --username-only --dmenu-invocation dmenu",
)
config.bind(
    "<Space>iPp",
    "spawn --userscript qute-pass --password-only --dmenu-invocation dmenu",
)
config.bind(
    "<Space>iPp", "spawn --userscript qute-pass --otp-only --dmenu-invocation dmenu"
)

# Layout
# config.bind('<Space>ld', 'session-delete default')
config.bind("<Space>ll", "session-load --clear default")
config.bind("<Space>lL", "cmd-set-text --space :session-load --clear")
config.bind("<Space>ls", "session-save default")
config.bind("<Space>lS", "cmd-set-text --space :session-save")

# Quit
config.bind("<Space>qq", "quit")
config.bind("<Space>qR", "restart")

# Window
config.bind("<Space>wd", "close")
config.bind("<Space>wF", "tab-clone --window")
config.bind("<Space>wpm", "messages")
config.bind("<Space>wm", "fullscreen")
config.bind("<Space>wpP", "clear-messages")

config.bind("<Space>xOm", "hint images")
config.bind("<Space>xOM", "hint images tab")
config.bind("<Space>xOi", "hint inputs")
config.bind("<Space>xOI", "hint inputs --first")
