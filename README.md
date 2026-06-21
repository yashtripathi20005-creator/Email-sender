# 📧 Email Sender Script (SMTP)

Python script to send emails via SMTP with support for plain text, HTML, templates, and attachments.

## 🚀 Quick Start

1. **Configure** `config.ini` with your SMTP credentials (Gmail users: use [App Password](https://support.google.com/accounts/answer/185833))
2. **Run** `python main.py`
3. **Choose** from the interactive menu

## 📁 Files

- `main.py` - CLI interface
- `email_sender.py` - SMTP logic
- `email_templates.py` - Pre-built templates
- `config.ini` - Your credentials (never commit this!)
- `requirements.txt` - No dependencies (uses standard library only)

## ✨ Features

- Plain text & HTML emails
- File attachments
- Ready-to-use templates (welcome, notifications, password reset, order confirmation)
- CC/BCC support
- Interactive menu

## 🔒 Security

- Never commit `config.ini` to GitHub
- Use environment variables for production
- For Gmail: use App Passwords, not your regular password

## 📝 Example

```python
from email_sender import EmailSender

sender = EmailSender()
sender.send_email(
    recipient="user@example.com",
    subject="Hello",
    body="This is a test email"
)
