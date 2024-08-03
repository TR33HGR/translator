# translator
Playing around with translation APIs

## Proposal
I want to create a web app that can interact with either [Naver's Papago API](https://api.ncloud-docs.com/docs/en/ai-naver-papagonmt) or [Google's Translator API](https://cloud.google.com/translate/docs/reference/api-overview).

For this, I need to understand REST APIs and how to debug them, so the aim is to start with creating a REST server in Python, that I will be able to use to play around and debug my requests before investing time in the actual servers mentioned above. Once this is useable I can then get a start on the app.

I will at some point need to figure out how to make this app "secure", as I want to interact with paid APIs. My understanding at this time is that this is mainly finding out how to not commit keys into git.

When I am able to send a string and receive its translation, it opens the door to my ultimate goal of creating a React Native app that allows translation to multiple languages at once, and also a browser plugin for translating highlighted strings.