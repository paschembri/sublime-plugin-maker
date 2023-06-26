import sublime
import sublime_plugin
import urllib.request
import json
import webbrowser


class NpmSearcherCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel('Search NPM:', '', self.on_done, None, None)

    def on_done(self, input):
        url = 'https://registry.npmjs.com/-/v1/search?text={}&size=20'.format(input)
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            self.packages = [(str(p['package']['name']), p['package']['links']['npm']) for p in data['objects']]
            self.window.show_quick_panel(self.packages, self.on_select)

    def on_select(self, index):
        if index == -1:
            return
        webbrowser.open(self.packages[index][1])