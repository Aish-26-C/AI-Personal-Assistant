import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

from backend.prompts import SYSTEM_PROMPT


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()


# =========================================================
# GET GROQ API KEY
# =========================================================

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing from the .env file."
    )


# =========================================================
# CREATE GROQ LLM
# =========================================================

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    api_key=api_key
)


# =========================================================
# CONVERSATION MEMORY
# =========================================================
#
# The system prompt is kept permanently.
# User and AI messages are added during the conversation.
#
# Example:
#
# SystemMessage
#      ↓
# HumanMessage
#      ↓
# AIMessage
#      ↓
# HumanMessage
#      ↓
# AIMessage
#
# This allows the AI to understand previous messages.
# =========================================================

conversation_history = [
    SystemMessage(
        content=SYSTEM_PROMPT
    )
]


# =========================================================
# GET AI RESPONSE
# =========================================================

def get_ai_response(message: str) -> str:
    """
    Send the user's message to the Groq LLM
    together with the conversation history.

    The response is stored in memory so that
    future questions can use previous context.
    """

    # -----------------------------------------------------
    # Add user's message to conversation history
    # -----------------------------------------------------

    conversation_history.append(
        HumanMessage(
            content=message
        )
    )


    # -----------------------------------------------------
    # Send complete conversation to Groq
    # -----------------------------------------------------

    response = llm.invoke(
        conversation_history
    )


    # -----------------------------------------------------
    # Store AI response in conversation history
    # -----------------------------------------------------

    conversation_history.append(
        AIMessage(
            content=response.content
        )
    )


    # -----------------------------------------------------
    # Return AI response
    # -----------------------------------------------------

    return response.content


# =========================================================
# CLEAR CONVERSATION
# =========================================================

def clear_conversation():
    """
    Clear all previous conversation messages
    while keeping the system prompt.
    """

    conversation_history.clear()

    conversation_history.append(
        SystemMessage(
            content=SYSTEM_PROMPT
        )
    )


# =========================================================
# GET CURRENT CONVERSATION HISTORY
# =========================================================

def get_conversation_history():
    """
    Return the current conversation history.

    This function can be useful for debugging,
    testing, or future features.
    """

    return conversation_history


# =========================================================
# TERMINAL CHATBOT
# =========================================================

if __name__ == "__main__":

    print("=" * 60)

    print(
        "             AI PERSONAL ASSISTANT"
    )

    print("=" * 60)

    print(
        "Type 'exit' to stop."
    )

    print(
        "Type 'clear' to clear conversation memory."
    )

    print("=" * 60)

    print()


    # -----------------------------------------------------
    # Continuous conversation
    # -----------------------------------------------------

    while True:

        user_message = input(
            "You: "
        ).strip()


        # -------------------------------------------------
        # Ignore empty messages
        # -------------------------------------------------

        if not user_message:

            print(
                "AI: Please enter a message."
            )

            print()

            continue


        # -------------------------------------------------
        # Exit
        # -------------------------------------------------

        if user_message.lower() == "exit":

            print(
                "AI: Goodbye!"
            )

            break


        # -------------------------------------------------
        # Clear conversation
        # -------------------------------------------------

        if user_message.lower() == "clear":

            clear_conversation()

            print(
                "AI: Conversation memory has been cleared."
            )

            print()

            continue


        # -------------------------------------------------
        # Generate AI response
        # -------------------------------------------------

        try:

            response = get_ai_response(
                user_message
            )

            print(
                "AI:",
                response
            )

            print()


        except Exception as error:

            print(
                "AI: Sorry, something went wrong."
            )

            print(
                "Error:",
                error
            )

            print()