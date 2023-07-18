import sublime
import sublime_plugin
import json
import urllib.request


class TiktokenCounterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings("TiktokenCounter.sublime-settings")
        endpoint = settings.get("endpoint")

        # Get the selected text
        selected_text = self.view.substr(self.view.sel()[0])

        data = json.dumps(
            {"prompt": selected_text, "model": "gpt-3.5-turbo"}
        ).encode("utf-8")

        req = urllib.request.Request(
            endpoint, data=data, headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            token_count = str(result.get("token_count", 0))
            sublime.status_message(
                "Tiktoken counter: {} tokens".format(token_count)
            )
