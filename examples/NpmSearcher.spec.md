# Overview


I want to create a Sublime Text Plugin.

I want to be able to fetch data from a JSON REST API and display
the results in the quick panel.

The features I need are :

- Dynamically fetch data
- Display in the quick panel

Upon selection, I'll need to perform an operation described hereunder.

Plugin name: "NpmSearcher"

We need :

User input requirements before making the API call
- Feature to implement upon selection
- Example CURL command for the selected API endpoint
- Example response to the CURL command
- Optional authentication requirements or method

Provide a list of questions to gather the required information.

# Questions - Answers

What feature do you want to implement upon selection?

> Open the browser showing the homepage of the package

Can you provide an example CURL command for the selected API endpoint?

> ask for `user-input` then perform a curl https://registry.npmjs.com/-/v1/search?text=<user-input>&size=20

Can you provide an example response to the CURL command?

> curl https://registry.npmjs.com/-/v1/search?text=lexical-vue&size=20
> {"objects":[{"package":{"name":"lexical-vue","scope":"unscoped","version":"0.6.1","description":"An extensible Vue 3 web text-editor based on Lexical.","keywords":["vue","lexical","editor","rich-text"],"date":"2023-06-24T02:49:53.492Z","links":{"npm":"https://www.npmjs.com/package/lexical-vue","homepage":"https://github.com/wobsoriano/lexical-vue#readme","repository":"https://github.com/wobsoriano/lexical-vue","bugs":"https://github.com/wobsoriano/lexical-vue/issues"},"author":{"name":"Robert Soriano","email":"sorianorobertc@gmail.com","username":"wobsoriano"},"publisher":{"username":"wobsoriano","email":"sorianorobertc@gmail.com"},"maintainers":[{"username":"wobsoriano","email":"sorianorobertc@gmail.com"}]},"flags":{"unstable":true},"score":{"final":0.2515652209228157,"detail":{"quality":0.43333981323566173,"popularity":0.0139903151012872,"maintenance":0.3333333333333333}},"searchScore":100000.22},{"package":{"name":"@meogic/lexical-vue","scope":"meogic","version":"0.11.1-mod6","description":"An extensible Vue 3 web text-editor based on Lexical.","keywords":["vue","lexical","editor","rich-text"],"date":"2023-06-18T09:38:16.653Z","links":{"npm":"https://www.npmjs.com/package/%40meogic%2Flexical-vue","homepage":"https://github.com/wobsoriano/lexical-vue#readme","repository":"https://github.com/wobsoriano/lexical-vue","bugs":"https://github.com/wobsoriano/lexical-vue/issues"},"author":{"name":"Robert Soriano","email":"sorianorobertc@gmail.com"},"publisher":{"username":"wingnpm","email":"lwy8wing@gmail.com"},"maintainers":[{"username":"wingnpm","email":"lwy8wing@gmail.com"}]},"flags":{"unstable":true},"score":{"final":0.24886096218040604,"detail":{"quality":0.43333981323566173,"popularity":0.006263861551545318,"maintenance":0.3333333333333333}},"searchScore":3.5608699e-7},{"package":{"name":"v-lexical","scope":"unscoped","version":"0.0.0","description":"Bundleless Vue component library starter.","date":"2022-12-30T09:55:36.116Z","links":{"npm":"https://www.npmjs.com/package/v-lexical"},"author":{"name":"Robert Soriano","email":"sorianorobertc@gmail.com","username":"wobsoriano"},"publisher":{"username":"wobsoriano","email":"sorianorobertc@gmail.com"},"maintainers":[{"username":"wobsoriano","email":"sorianorobertc@gmail.com"}]},"flags":{"unstable":true},"score":{"final":0.24661865465885796,"detail":{"quality":0.43333981323566173,"popularity":0.0020485492309798353,"maintenance":0.33114205273519}},"searchScore":1.9905723e-7},{"package":{"name":"lexical-vue-testing","scope":"unscoped","version":"0.3.7","description":"An extensible Vue 3 web text-editor based on Lexical.","keywords":["vue","lexical","editor","rich-text"],"date":"2022-12-31T09:26:24.657Z","links":{"npm":"https://www.npmjs.com/package/lexical-vue-testing","homepage":"https://github.com/wobsoriano/lexical-vue#readme","repository":"https://github.com/wobsoriano/lexical-vue","bugs":"https://github.com/wobsoriano/lexical-vue/issues"},"author":{"name":"Robert Soriano","email":"sorianorobertc@gmail.com","username":"wobsoriano"},"publisher":{"username":"wobsoriano","email":"sorianorobertc@gmail.com"},"maintainers":[{"username":"wobsoriano","email":"sorianorobertc@gmail.com"}]},"flags":{"unstable":true},"score":{"final":0.22218594804371278,"detail":{"quality":0.347696184078777,"popularity":0.003472939982760946,"maintenance":0.33331875378889525}},"searchScore":7.232054e-8},{"package":{"name":"@wattanx/lexical-vue","scope":"wattanx","version":"0.0.2","description":"An extensible Vue web text-editor based on Lexical.","keywords":["vue","lexical","editor","rich-text"],"date":"2023-03-16T14:27:30.946Z","links":{"npm":"https://www.npmjs.com/package/%40wattanx%2Flexical-vue","homepage":"https://github.com/wattanx/lexical-vue#readme","repository":"https://github.com/wattanx/lexical-vue","bugs":"https://github.com/wattanx/lexical-vue/issues"},"author":{"name":"wattanx"},"publisher":{"username":"wattanx","email":"wattan.dev@gmail.com"},"maintainers":[{"username":"wattanx","email":"wattan.dev@gmail.com"}]},"flags":{"unstable":true},"score":{"final":0.2217645176313004,"detail":{"quality":0.347696184078777,"popularity":0.0027800241857935688,"maintenance":0.3328075826932559}},"searchScore":7.0236894e-8},{"package":{"name":"@wingnpm/lexical-vue","scope":"wingnpm","version":"0.2.4","description":"An extensible Vue 3 web text-editor based on Lexical.","keywords":["vue","lexical","editor","rich-text"],"date":"2022-12-20T09:07:11.635Z","links":{"npm":"https://www.npmjs.com/package/%40wingnpm%2Flexical-vue","homepage":"https://github.com/aquarius-wing/lexical-vue#readme","repository":"https://github.com/aquarius-wing/lexical-vue","bugs":"https://github.com/aquarius-wing/lexical-vue/issues"},"author":{"name":"Robert Soriano","email":"sorianorobertc@gmail.com"},"publisher":{"username":"wingnpm","email":"lwy8wing@gmail.com"},"maintainers":[{"username":"wingnpm","email":"lwy8wing@gmail.com"}]},"flags":{"unstable":true},"score":{"final":0.21322771868429385,"detail":{"quality":0.3195947325657706,"popularity":0.003274528161818685,"maintenance":0.3320091830226461}},"searchScore":4.0868702e-8},{"package":{"name":"vue-lexical","scope":"unscoped","version":"1.0.0","description":"just for fun","date":"2022-04-14T06:21:27.949Z","links":{"npm":"https://www.npmjs.com/package/vue-lexical"},"publisher":{"username":"baixiaoyu","email":"bxy2997@sina.com"},"maintainers":[{"username":"baixiaoyu","email":"bxy2997@sina.com"}]},"score":{"final":0.1296524877147108,"detail":{"quality":0.384912226820316,"popularity":0.0012544410285713007,"maintenance":0.039256472310331546}},"searchScore":5.7244195e-11}],"total":7,"time":"Mon Jun 26 2023 21:35:29 GMT+0000 (Coordinated Universal Time)"}%

Are there any authentication requirements or methods for the API?

> No.
