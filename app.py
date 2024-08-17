import subprocess
import os
from datetime import datetime
from telegram import Bot
import time

# Database configuration
db_user = 'your_username'
db_password = 'your_password'
db_name = 'your_database_name'

# Telegram bot configuration
bot_token = 'your_bot_token'
chat_id = 'your_chat_id'

# Backup directory
backup_dir = '/db/bkp'
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Function to perform the database backup
def backup_database():
    try:
        backup_file = os.path.join(backup_dir, f"db_backup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.sql")
        command = f"mysqldump -u {db_user} -p{db_password} {db_name} > {backup_file}"
        subprocess.run(command, shell=True, check=True)
        print(f"Backup successful: {backup_file}")
        return backup_file
    except Exception as e:
        print(f"Backup failed: {e}")
        return None

# Function to send the backup file via Telegram
def send_backup_via_telegram(file_path):
    try:
        bot = Bot(token=bot_token)
        with open(file_path, 'rb') as document:
            bot.send_document(chat_id=chat_id, document=document)
        print(f"Backup file sent to Telegram: {file_path}")
    except Exception as e:
        print(f"Failed to send backup via Telegram: {e}")

# Infinite loop to run the backup every hour
while True:
    backup_file = backup_database()
    if backup_file:
        send_backup_via_telegram(backup_file)
    
    # Sleep for 1 hour (3600 seconds)
    time.sleep(3600)
