# -*- coding: utf-8 -*-
import subprocess
import click
import textwrap
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain import LLMChain
from itertools import chain
from .constants import (
    PLUGIN_TYPE_REQUIREMENTS,
    SUPPORTED_PLUGIN_TYPES,
)


def make_spec(plugin_type):
    specs = PLUGIN_TYPE_REQUIREMENTS[plugin_type]

    builtin_requirements = '\n- '.join(specs['builtin-requirements'])
    prompt = specs['prompt']

    p_template = PromptTemplate(
        template=prompt,
        input_variables=["plugin_name", "builtin_requirements"],
    )
    partial_template = p_template.partial(
        builtin_requirements=builtin_requirements
    )

    questions_schema = {
        "name": "ask_questions",
        "description": "Ask questions to a user",
        "parameters": {
            "type": "object",
            "properties": {
                "questions": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["questions"],
        },
    }

    return partial_template, questions_schema


@click.command()
@click.option(
    '--plugin-name',
    prompt='Plugin name',
)
@click.option(
    '--plugin-type',
    prompt='What type of plugin do you want to make ?',
    type=click.Choice(SUPPORTED_PLUGIN_TYPES, case_sensitive=False),
)
def make(plugin_name, plugin_type):
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0613",
    )

    prompt, schema = make_spec(plugin_type)
    spec_chain = LLMChain(
        llm=llm,
        prompt=prompt,
        llm_kwargs={"functions": [schema]},
        output_parser=JsonOutputFunctionsParser(args_only=False),
        output_key="questions",
    )

    response = spec_chain.run(plugin_name=plugin_name)

    questions = response['arguments']['questions']
    placeholders = [
        '> type here your answer providing more context or examples'
    ] * len(questions)

    spec_text = textwrap.dedent(
        '\n'.join(
            (
                '# Overview\n',
                prompt.format(plugin_name=plugin_name),
                '# Questions - Answers\n',
                '\n\n'.join(chain(*zip(questions, placeholders))),
            )
        )
    )

    with open(f'./{plugin_name}.spec.md', 'w') as spec_file:
        spec_file.write(spec_text)

    print(f'Written {plugin_name}.spec.md')
    print('Answer the questions in the `Questions - Answers`. ')
    subprocess.run(['open', f'./{plugin_name}.spec.md'], check=True)
