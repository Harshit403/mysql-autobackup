# 🛡️ Automated MySQL Backup & Telegram Bot 📦

This repository contains a Python script that automates the process of backing up a MySQL database every hour and sends the backup file to a specified Telegram chat using a bot. This script is designed to run continuously and handle local databases hosted on the same server.

## 🚀 Features

- 💾 **Automated Hourly Backups**: Backup your MySQL database every hour.
- 📤 **Send Backups via Telegram**: Automatically send the backup file to your Telegram chat.
- 🔁 **Runs Continuously**: Script runs indefinitely with a 1-hour sleep between backups.
- 🔐 **Local Database Handling**: Works seamlessly with databases hosted on `localhost`.

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Harshit-shrivastav/mysql-autobackup.git
cd mysql-autobackup
```

### 2. Install Required Dependencies

Make sure you have Python 3 installed. Then, install the necessary libraries:

```bash
pip install python-telegram-bot
```

### 3. Configure the Script

Edit the `app.py` script to include your database and Telegram bot details:

```python
# Database configuration
db_user = 'your_username'
db_password = 'your_password'
db_name = 'your_database_name'

# Telegram bot configuration
bot_token = 'your_bot_token'
chat_id = 'your_chat_id'

# Backup directory
backup_dir = '/path/to/backup'
```

- 🔑 **db_user**: Your MySQL database username.
- 🔑 **db_password**: Your MySQL database password.
- 💾 **db_name**: The name of the database you want to back up.
- 🤖 **bot_token**: Your Telegram bot token (obtain from BotFather).
- 🆔 **chat_id**: Your Telegram chat ID where backups will be sent.
- 📁 **backup_dir**: Directory where backups will be stored.

### 4. Run the Script

Run the script manually to start the backup process. The script will continue running, creating backups every hour.

```bash
python3 app.py
```

To run the script in the background:

```bash
nohup python3 app.py > app.log 2>&1 &
```

### 5. Stop the Script

If you need to stop the script, find its Process ID (PID) and terminate it:

```bash
ps aux | grep app.py
kill <PID>
```

## 💡 How It Works

### 📝 SQL Backup Command

The script uses the following `mysqldump` command to create a backup of your database:

```bash
mysqldump -u your_username -p'your_password' your_database_name > db_backup.sql
```

- **What it does**: Creates a dump of your MySQL database and saves it to a specified file.
- **Output**: The SQL dump is saved to the specified file, nothing is returned in the terminal.

### 🕒 Continuous Backup Process

- The script runs in an infinite loop (`while True:`) and sleeps for 1 hour (`time.sleep(3600)`) between backups.
- After creating a backup, the script sends the file to your specified Telegram chat.

## 🔒 Security Considerations

- **Environment Variables**: Store sensitive information (like passwords and tokens) in environment variables rather than hard-coding them into the script.
- **File Permissions**: Ensure that backup files and the script have appropriate permissions to prevent unauthorized access.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### 📬 Feedback & Contributions

Feel free to submit issues or pull requests if you find any bugs or have improvements!

---

### 📦 Repository Structure

```plaintext
.
├── backup_bot.py          # Main Python script for automated backups
├── README.md              # This file
└── LICENSE                # License file
```
