#!/usr/bin/env python3
"""
Main entry point for the email sender script.
"""

import sys
from email_sender import EmailSender
from email_templates import EmailTemplates


def main():
    """Main function to run the email sender."""
    print("=== Email Sender Script ===\n")
    
    # Initialize email sender
    sender = EmailSender()
    
    # Check if sender is configured
    if not sender.is_configured():
        print("❌ Email sender is not configured. Please check config.ini")
        sys.exit(1)
    
    print("✅ Configuration loaded successfully")
    print(f"   SMTP Server: {sender.smtp_server}")
    print(f"   Sender: {sender.sender_email}")
    
    # Show menu
    while True:
        print("\n" + "="*50)
        print("Choose an option:")
        print("1. Send a simple text email")
        print("2. Send an HTML email")
        print("3. Send a templated welcome email")
        print("4. Send a templated notification email")
        print("5. Send email with attachment")
        print("6. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            send_simple_email(sender)
        elif choice == '2':
            send_html_email(sender)
        elif choice == '3':
            send_welcome_email(sender)
        elif choice == '4':
            send_notification_email(sender)
        elif choice == '5':
            send_email_with_attachment(sender)
        elif choice == '6':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


def send_simple_email(sender):
    """Send a simple text email."""
    print("\n--- Send Simple Email ---")
    
    recipient = input("Recipient email (or press Enter for default): ").strip()
    if not recipient:
        recipient = sender.recipient_email
    
    subject = input("Subject (or press Enter for default): ").strip()
    if not subject:
        subject = "Simple Test Email"
    
    print("Enter your message (type 'END' on a new line when finished):")
    lines = []
    while True:
        line = input()
        if line == 'END':
            break
        lines.append(line)
    
    body = '\n'.join(lines)
    
    if not body:
        body = "This is a test email sent from the Python email sender script."
    
    try:
        success = sender.send_email(recipient, subject, body)
        if success:
            print(f"✅ Email sent successfully to {recipient}!")
        else:
            print(f"❌ Failed to send email to {recipient}")
    except Exception as e:
        print(f"❌ Error: {e}")


def send_html_email(sender):
    """Send an HTML email."""
    print("\n--- Send HTML Email ---")
    
    recipient = input("Recipient email (or press Enter for default): ").strip()
    if not recipient:
        recipient = sender.recipient_email
    
    subject = input("Subject (or press Enter for default): ").strip()
    if not subject:
        subject = "HTML Test Email"
    
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; }
            .container { padding: 20px; background-color: #f4f4f4; }
            .header { color: #2c3e50; }
            .content { background-color: white; padding: 20px; border-radius: 5px; }
            .footer { color: #7f8c8d; font-size: 12px; margin-top: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>✨ HTML Email Test</h1>
            </div>
            <div class="content">
                <p>Hello,</p>
                <p>This is an <strong>HTML email</strong> sent from the Python email sender script.</p>
                <p>You can format your emails with:</p>
                <ul>
                    <li><b>Bold text</b></li>
                    <li><i>Italic text</i></li>
                    <li><span style="color: #e74c3c;">Colored text</span></li>
                </ul>
                <p>✅ This email was sent using SMTP!</p>
            </div>
            <div class="footer">
                <p>This is an automated message. Please do not reply.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    try:
        success = sender.send_html_email(recipient, subject, html_content)
        if success:
            print(f"✅ HTML email sent successfully to {recipient}!")
        else:
            print(f"❌ Failed to send HTML email to {recipient}")
    except Exception as e:
        print(f"❌ Error: {e}")


def send_welcome_email(sender):
    """Send a templated welcome email."""
    print("\n--- Send Welcome Email ---")
    
    recipient = input("Recipient email (or press Enter for default): ").strip()
    if not recipient:
        recipient = sender.recipient_email
    
    name = input("Recipient's name: ").strip() or "User"
    
    try:
        templates = EmailTemplates()
        subject, body = templates.welcome_email(name)
        success = sender.send_email(recipient, subject, body)
        
        if success:
            print(f"✅ Welcome email sent successfully to {recipient}!")
        else:
            print(f"❌ Failed to send welcome email to {recipient}")
    except Exception as e:
        print(f"❌ Error: {e}")


def send_notification_email(sender):
    """Send a templated notification email."""
    print("\n--- Send Notification Email ---")
    
    recipient = input("Recipient email (or press Enter for default): ").strip()
    if not recipient:
        recipient = sender.recipient_email
    
    title = input("Notification title: ").strip() or "System Notification"
    message = input("Notification message: ").strip() or "This is a system notification."
    
    try:
        templates = EmailTemplates()
        subject, body = templates.notification_email(title, message)
        success = sender.send_email(recipient, subject, body)
        
        if success:
            print(f"✅ Notification email sent successfully to {recipient}!")
        else:
            print(f"❌ Failed to send notification to {recipient}")
    except Exception as e:
        print(f"❌ Error: {e}")


def send_email_with_attachment(sender):
    """Send an email with an attachment."""
    print("\n--- Send Email with Attachment ---")
    
    recipient = input("Recipient email (or press Enter for default): ").strip()
    if not recipient:
        recipient = sender.recipient_email
    
    subject = input("Subject (or press Enter for default): ").strip()
    if not subject:
        subject = "Email with Attachment"
    
    body = input("Email body: ").strip() or "Please find the attached file."
    
    file_path = input("File path to attach: ").strip()
    
    try:
        success = sender.send_email_with_attachment(
            recipient, subject, body, file_path
        )
        if success:
            print(f"✅ Email with attachment sent successfully to {recipient}!")
        else:
            print(f"❌ Failed to send email with attachment to {recipient}")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
