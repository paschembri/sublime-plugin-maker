# Overview


I want to create a Sublime Text Plugin.

I want to be able to fetch data from a JSON REST API and display
the results in the quick panel.

The features I need are :

- Dynamically fetch data
- Display in the quick panel

Upon selection, I'll need to perform an operation described hereunder.

Plugin name: "Tiktoken-Counter"

We need :

User input requirements before making the API call
- Feature to implement upon selection
- Example CURL command for the selected API endpoint
- Example response to the CURL command
- Optional authentication requirements or method

Provide a list of questions to gather the required information.

# Questions - Answers

What is the feature you want to implement upon selection?

> I want the sublime bottom bar to show the answer to a curl request ; specifically the `token_count`.
> I want the following message displayed : "Tiktoken counter: 4 tokens" where "4" is the value of `token_count`

Can you provide an example CURL command for the selected API endpoint?

> curl -d '{"prompt" : "my test request", "model" : "gpt-3.5-turbo"}' -H "Content-Type: application/json"  http://localhost:5502/tokenize

Can you provide an example response to the CURL command?

> {"tokens": [2465, 836, 374, 36292], "token_count": 4}

Are there any authentication requirements or methods for the API?

> No

Other requirements ?

> the endpoint should be configurable in the settings
