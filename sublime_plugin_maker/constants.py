DISPLAY_REST_API_DATA_PROMPT = """
I want to create a Sublime Text Plugin.

I want to be able to fetch data from a JSON REST API and display
the results in the quick panel.

The features I need are :

- Dynamically fetch data
- Display in the quick panel

Upon selection, I'll need to perform an operation described hereunder.

Plugin name: "{plugin_name}"

We need :

{builtin_requirements}

Provide a list of questions to gather the required information.
"""

SUPPORTED_PLUGIN_TYPES = [
    'fetch-rest-api-data',
]

PLUGIN_TYPE_REQUIREMENTS = {
    'fetch-rest-api-data': {
        'prompt': DISPLAY_REST_API_DATA_PROMPT,
        'builtin-requirements': [
            'User input requirements before making the API call',
            'Feature to implement upon selection',
            'Example CURL command for the selected API endpoint',
            'Example response to the CURL command',
            'Optional authentication requirements or method',
        ],
    }
}

BUILDER_PROMPT = """
{context}

# Next steps

Using the information provided above, create a Sublime Text
plugin.

# Constraints

- Write Python 3.3 compatible code
- f-strings are not authorized.
- Always use `.format` method to interpolate strings
- We can only use the Python Standard Library and sublime and sublime_plugin
- Any dynamic data should be fetched from the sublime settings
- To perform clipboard operation, use `sublime.set_clipboard` method
- The sublime command name should be the snaked_case version of {plugin_name}
  without `command`. For example : MyPluginCommand -> my_plugin
- Always convert data fetched from API to `str` before using


# Todo

Now, perform the following operations :

{operations}

"""

OPERATIONS_PROMPT = [
    '1. Create and write sublime settings in {plugin_name}.sublime-settings',
    '2. Create and write python code in {plugin_name}.py while meeting all constraints',
    '3. Create and write sublime commands file {plugin_name}.sublime-commands',
    '4. Create a {plugin_name}-readme.md file with installation instructions',
]

CHECKER_PROMPT = """

# Constraints

- Write Python 3.3 compatible code
- f-strings are not authorized.
- Always use `.format` method to interpolate strings
- We can only use the Python Standard Library and sublime and sublime_plugin
- Any dynamic data should be fetched from the sublime settings
- To perform clipboard operation, use `sublime.set_clipboard` method
- Always convert data fetched from API to `str` before using

# Code

```python
{code}

# Instructions

Given the previous code, analyze and fix the error or unmet constraints.

Write the results in {plugin_name}.py
```
"""
