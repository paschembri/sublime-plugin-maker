# Sublime Text Plugin Maker

## What's this ?

This packages enables automatic code generation to create plugins for
Sublime Text.

It uses OpenAI newly released Functions and Langchain integration.

## What kind of plugin can it write ?

At the moment, only the `fetch-rest-api-data` plugin type is supported. That means
that it can write a Sublime Text plugin that will fetch data through a API of 
your choice and show the results in a dropdown menu.

You can even ask for input.

## Does it work ?

Yes, I managed to create several plugins. See the `examples` directory :

- ConvertKitTagsManager : A Sublime plugin to retrieve tags from ConvertKit API (so embedding them into forms is nicer)
- NpmSearcher : A sample plugin querying the npmjs registry and then opening a browser upon selection


## How to use ?

```bash
# Sublime Text Plugin Maker

# First we write specifications
# This will prepare a spec file named ConvertKitTagsManager.spec.md.
# We open the file using the default text editor.
# This is a regular text file with some questions to help the AI write the code
make-specs --plugin-name ConvertKitTagsManager --plugin-type fetch-rest-api-data


# Then write the code (make-plugin --help for full parameters)
make-plugin --spec-file-path ConvertKitTagsManager.spec.md
```
