# Habitica Quest Auto-Accept Script

This Python script automates the process of accepting quests on Habitica. It checks whether there is a quest to accept in your party, and it will automatically accept a new quest.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3 installed on your system.
- Your Habitica API credentials, which include:
  - `x-api-user`: Your Habitica user ID.
  - `x-api-key`: Your Habitica API key.

## Installation and Setup

1. Clone or download this repository to your local machine.

2. Open the script file `autoAcceptQuest.py` in a text editor of your choice.

3. Replace the following placeholders with your Habitica API credentials:

   - `xapiuser`: Your `x-api-user` value.
   - `xapikey`: Your `x-api-key` value.

   ```python
   xapiuser = "YOUR_API_USER_ID"
   xapikey = "YOUR_API_KEY"
   ```

4. Save the changes to the script file.

## Usage

You can run this script manually or set it up as a cron job to repeat automatically at your desired interval (e.g., every hour).

### Manual Execution

To run the script manually, open your terminal and navigate to the directory containing the `auto_accept_quest.py` script. Then, execute the following command:

```bash
python3 autoAcceptQuest.py
```

The script will check for a pending active quest in your Habitica party and it will automatically if there is a pending active quest.

### Setting up a Cron Job (Automatic Execution)

To set up a cron job to run the script automatically every hour, follow these steps:

1. Open your terminal.

2. Edit your crontab file by running the following command:

   ```bash
   crontab -e
   ```

3. Add the following line to your crontab file to run the script every hour:

   ```bash
   0 * * * * /usr/bin/python3 /path/to/auto_accept_quest.py
   ```

   Replace `/path/to/auto_accept_quest.py` with the actual path to your `auto_accept_quest.py` script.

4. Save the crontab file and exit the text editor.

The script will now run automatically every hour as a cron job, checking for and accepting quests in your Habitica party when needed.

## Disclaimer

This script interacts with Habitica's API, and its behavior may change if Habitica updates its API endpoints or authentication methods. Use it responsibly and in accordance with Habitica's terms of service.
