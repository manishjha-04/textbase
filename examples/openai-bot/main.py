from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = API_KEY.env

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with a recipe suggestor and diet manager.

To get a recipe suggestion based on available ingredients, you can provide the ingredients you have or ask for a specific dish. For example, you can say "I have chicken, tomatoes, and onions. What recipe can I make?" or "Can you suggest a pasta recipe?"

To create a diet plan for gym lovers, you can specify dietary preferences, calorie requirements, and meal frequency. For example, you can say "I want a high-protein diet plan with 2000 calories per day and 5 meals." The AI will provide a personalized diet plan for you.

Feel free to start the conversation with any question or topic related to recipe suggestion or diet management, and let's get started!
"""



@bot()
def on_message(message_history: List[Message], state: dict = None):
    if len(message_history) == 0:
        # Send an initial message from the bot when the conversation starts
        initial_message = Message("Bot", "Hello ,Welcome to the recipe suggestor and diet manager! I can help you with recipe suggestions based on available ingredients you have or specific dishes you want to make so to fullfill yout midnight cravings. Or you can also ask me to create a personalized diet plan for you or for gym rats. Feel free to ask any questions or let me know how I can assist you")
        message_history.append(initial_message)

        # Add a message describing what the chatbot can do
        intro_message = Message("Bot", "Welcome to the recipe suggestor and diet manager! I can help you with recipe suggestions based on available ingredients or specific dishes. You can also ask me to create a personalized diet plan for gym lovers. Feel free to ask any questions or let me know how I can assist you.")
        message_history.append(intro_message)

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }
