# -*- coding: utf-8 -*-
import os
import click
from langchain.tools.file_management.write import WriteFileTool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from .constants import BUILDER_PROMPT, OPERATIONS_PROMPT, CHECKER_PROMPT

import langchain

langchain.debug = True


def camel_to_snake_case(string):
    new_string = ""
    for i in range(len(string)):
        if string[i].isupper():
            new_string += "_" + string[i].lower()
        else:
            new_string += string[i]
    return new_string


class PythonFileTool(WriteFileTool):
    """
    WriteFileTool wrapper for sporadic hallucinations from models
    """

    name: str = "python"
    description: str = "Persist python code into a file"


class SublimeSettingsFileTool(WriteFileTool):
    """
    WriteFileTool wrapper for sporadic hallucinations from models
    """

    name: str = "sublime_settings"
    description: str = "Create and write sublime settings into a file"


class SublimeCommandFileTool(WriteFileTool):
    """
    WriteFileTool wrapper for sporadic hallucinations from models
    """

    name: str = "sublime_commands"
    description: str = "Create and write sublime commands into a file"


class ReadmeFileTool(WriteFileTool):
    """
    WriteFileTool wrapper for sporadic hallucinations from models
    """

    name: str = "write_readme"
    description: str = "Create and write readme into a file"


@click.command()
@click.option(
    "--spec-file-path",
    prompt="Spec file generated with `make-specs`",
)
@click.option(
    "--sublime-packages-path",
    default="~/Library/Application Support/Sublime Text 3/Packages",
)
def make(spec_file_path, sublime_packages_path):
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4",
    )

    plugin_name = os.path.basename(spec_file_path).replace(".spec.md", "")

    with open(spec_file_path, "r") as spec_file:
        full_context = spec_file.read()

    prompt = PromptTemplate(
        template=BUILDER_PROMPT,
        input_variables=[
            "context",
            "operations",
            "plugin_name",
        ],
    )

    sublime_packages_path = os.path.expanduser(sublime_packages_path)
    working_directory = os.path.join(sublime_packages_path, plugin_name)
    os.makedirs(working_directory, exist_ok=True)

    tools_cls = (
        PythonFileTool,
        SublimeSettingsFileTool,
        SublimeCommandFileTool,
        ReadmeFileTool,
    )
    tools = [cls(root_dir=str(working_directory)) for cls in tools_cls]

    sublime_maker_agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
    )
    operations = map(
        lambda op: op.format(plugin_name=plugin_name), OPERATIONS_PROMPT
    )

    instructions = prompt.format(
        context=full_context,
        operations=operations,
        plugin_name=plugin_name,
    )

    sublime_maker_agent.run(instructions)

    print("Completed.")
