# Image Analysis Telegram Bot

This project includes a Telegram bot capable of analyzing images sent to it by users. The bot utilizes Azure's Computer Vision API to perform image analysis and provides detailed descriptions of the images, including captions, tags, detected objects, and people.

## Features

- **Image Analysis**: The bot can analyze images to extract various visual features such as captions, tags, objects, and people present in the image.
- **Telegram Integration**: Users can interact with the bot directly through Telegram by sending images for analysis.
- **Multi-language Support**: The bot supports both English and Russian languages for user interaction.

## Files

- **ai_bot.py**: Contains functions related to generating a description of an image based on its visual features.
- **analiz.py**: Implements the image analysis functionality using Azure's Computer Vision API.
- **bot_TG.py**: Defines the Telegram bot and its interaction with users.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain API keys for Azure Computer Vision and Telegram Bot API.
4. Replace placeholders for API keys and other configurations in the respective files (`ai_bot.py`, `analiz.py`, `bot_TG.py`).
5. Run the `bot_TG.py` script to start the Telegram bot.

## Usage

1. Start the bot by sending the `/start` command.
2. Send an image to the bot.
3. The bot will analyze the image and provide a detailed description of its visual content.
4. Users can interact with the bot further by sending more images or using other available commands.