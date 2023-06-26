# Overview


I want to create a Sublime Text Plugin.

I want to be able to fetch data from a JSON REST API and display
the results in the quick panel.

The features I need are :

- Dynamically fetch data
- Display in the quick panel

Upon selection, I'll need to perform an operation described hereunder.

Plugin name: "ConvertKitTagsManager"

We need :

User input requirements before making the API call
- Feature to implement upon selection
- Example CURL command for the selected API endpoint
- Example response to the CURL command
- Optional authentication requirements or method

Provide a list of questions to gather the required information.

# Questions - Answers

What is the feature you want to implement upon selection?

> Copy the tag id in the sublime clipboard

Can you provide an example CURL command for the selected API endpoint?

> curl https://api.convertkit.com/v3/tags?api_key=<your_public_api_key>

Can you provide an example response to the CURL command?

> {
  "tags": [
    {
      "id": 1,
      "name": "House Stark",
      "created_at": "2016-02-28T08:07:00Z"
    },
    {
      "id": 2,
      "name": "House Lannister",
      "created_at": "2016-02-28T08:07:00Z"
    }
  ]
}

Are there any authentication requirements or methods for the API?

> All API calls require the api_key parameter. You can find your API Key in the ConvertKit Account page.
