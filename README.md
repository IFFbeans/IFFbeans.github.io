# IFFbeans.github.io
# Kids Story AI App

This is a *Python project* that runs a Flask server to generate *kid-friendly stories* using OpenAI GPT models. Kids can type in story ideas and get a fun, short story back.

## Features
- Accepts story ideas via a POST request.
- Generates fun, short, kid-friendly stories.
- Returns the story as JSON.

## Folder Structure

## Setup

1. *Install Dependencies*  

2. *Add OpenAI API Key*  
3. ⁠- In Replit, add it as a secret with key OPENAI_API_KEY.

3. *Run the Server*  
4. ⁠- The Flask server will start and give a public URL like:
  
  https://your-repl-name.your-username.repl.co
  

## API Endpoint

- *POST* /generate-story  
- *Request JSON body*:
```json
{
 "prompt": "A friendly dragon who loves cupcakes"
}
{
  "story": "Once upon a time, there was a friendly dragon named..."
