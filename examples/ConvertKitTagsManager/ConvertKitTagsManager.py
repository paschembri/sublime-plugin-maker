import sublime
import sublime_plugin
import urllib.request
import json

class ConvertKitTagsManagerCommand(sublime_plugin.WindowCommand):
    def run(self):
        settings = sublime.load_settings("ConvertKitTagsManager.sublime-settings")
        api_key = settings.get("api_key")
        url = "https://api.convertkit.com/v3/tags?api_key={}".format(api_key)
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            self.tags = data["tags"]
            self.window.show_quick_panel([tag["name"] for tag in self.tags], self.on_done)

    def on_done(self, index):
        if index == -1:
            return
        tag_id = str(self.tags[index]["id"])
        sublime.set_clipboard(tag_id)