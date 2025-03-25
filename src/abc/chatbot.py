import chainlit as cl

@cl.on_message
async def handleMessage(message: cl.Message):
    cl.Message(
        content=f"Received message: {message.content}",
    ).send()

@cl.on_chat_start
async def start():
    cl.Message(
        content = "Hello I am the abc chatbot"
    )
