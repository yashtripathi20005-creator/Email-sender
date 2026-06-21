"""
Email sender module using SMTP.
"""

import smtplib
import configparser
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from typing import Optional, List


class EmailSender:
    """Email sender class for sending emails via SMTP."""
    
    def __init__(self, config_file: str = "config.ini"):
        """
        Initialize the EmailSender with configuration.
        
        Args:
            config_file: Path to the configuration file
        """
        self.config_file = config_file
        self.smtp_server = ""
        self.smtp_port = 587
        self.sender_email = ""
        self.sender_password = ""
        self.recipient_email = ""
        self.default_subject = ""
        
        self._load_config()
    
    def _load_config(self) -> None:
        """Load configuration from the config file."""
        config = configparser.ConfigParser()
        
        if not Path(self.config_file).exists():
            print(f"⚠️ Config file '{self.config_file}' not found.")
            print("Creating default config file...")
            self._create_default_config()
            config.read(self.config_file)
        else:
            config.read(self.config_file)
        
        try:
            smtp_config = config['SMTP']
            self.smtp_server = smtp_config.get('smtp_server', '')
            self.smtp_port = smtp_config.getint('smtp_port', 587)
            self.sender_email = smtp_config.get('sender_email', '')
            self.sender_password = smtp_config.get('sender_password', '')
            
            default_config = config['Default']
            self.recipient_email = default_config.get('recipient_email', '')
            self.default_subject = default_config.get('subject', 'Default Subject')
        except (KeyError, ValueError) as e:
            print(f"❌ Error loading configuration: {e}")
    
    def _create_default_config(self) -> None:
        """Create a default configuration file."""
        config = configparser.ConfigParser()
        config['SMTP'] = {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': '587',
            'sender_email': 'your_email@gmail.com',
            'sender_password': 'your_app_password'
        }
        config['Default'] = {
            'subject': 'Default Subject',
            'recipient_email': 'recipient@example.com'
        }
        
        with open(self.config_file, 'w') as f:
            config.write(f)
        
        print(f"✅ Default config file created: {self.config_file}")
        print("Please update it with your email credentials.")
    
    def is_configured(self) -> bool:
        """Check if the email sender is properly configured."""
        return all([
            self.smtp_server,
            self.smtp_port,
            self.sender_email,
            self.sender_password
        ])
    
    def _create_connection(self) -> smtplib.SMTP:
        """
        Create and return an SMTP connection.
        
        Returns:
            SMTP connection object
        """
        try:
            # Create connection
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Enable TLS encryption
            
            # Login to the email server
            server.login(self.sender_email, self.sender_password)
            
            return server
        except smtplib.SMTPAuthenticationError:
            raise Exception("Authentication failed. Please check your email and password.")
        except smtplib.SMTPException as e:
            raise Exception(f"SMTP error: {e}")
        except Exception as e:
            raise Exception(f"Connection error: {e}")
    
    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None
    ) -> bool:
        """
        Send a plain text email.
        
        Args:
            recipient: Recipient email address
            subject: Email subject
            body: Email body (plain text)
            cc: List of CC recipients
            bcc: List of BCC recipients
            
        Returns:
            True if successful, False otherwise
        """
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject or self.default_subject
        msg['From'] = self.sender_email
        msg['To'] = recipient
        
        # Add CC recipients
        if cc:
            msg['Cc'] = ', '.join(cc)
        
        # Add BCC recipients
        if bcc:
            msg['Bcc'] = ', '.join(bcc)
        
        # Attach plain text body
        msg.attach(MIMEText(body, 'plain'))
        
        # Prepare recipients list
        recipients = [recipient]
        if cc:
            recipients.extend(cc)
        if bcc:
            recipients.extend(bcc)
        
        try:
            with self._create_connection() as server:
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return False
    
    def send_html_email(
        self,
        recipient: str,
        subject: str,
        html_content: str,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None
    ) -> bool:
        """
        Send an HTML email.
        
        Args:
            recipient: Recipient email address
            subject: Email subject
            html_content: HTML content of the email
            cc: List of CC recipients
            bcc: List of BCC recipients
            
        Returns:
            True if successful, False otherwise
        """
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject or self.default_subject
        msg['From'] = self.sender_email
        msg['To'] = recipient
        
        if cc:
            msg['Cc'] = ', '.join(cc)
        if bcc:
            msg['Bcc'] = ', '.join(bcc)
        
        # Attach HTML content
        msg.attach(MIMEText(html_content, 'html'))
        
        recipients = [recipient]
        if cc:
            recipients.extend(cc)
        if bcc:
            recipients.extend(bcc)
        
        try:
            with self._create_connection() as server:
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"❌ Failed to send HTML email: {e}")
            return False
    
    def send_email_with_attachment(
        self,
        recipient: str,
        subject: str,
        body: str,
        file_path: str,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None
    ) -> bool:
        """
        Send an email with a file attachment.
        
        Args:
            recipient: Recipient email address
            subject: Email subject
            body: Email body text
            file_path: Path to the file to attach
            cc: List of CC recipients
            bcc: List of BCC recipients
            
        Returns:
            True if successful, False otherwise
        """
        # Check if file exists
        if not Path(file_path).exists():
            print(f"❌ File not found: {file_path}")
            return False
        
        msg = MIMEMultipart()
        msg['Subject'] = subject or self.default_subject
        msg['From'] = self.sender_email
        msg['To'] = recipient
        
        if cc:
            msg['Cc'] = ', '.join(cc)
        if bcc:
            msg['Bcc'] = ', '.join(bcc)
        
        # Attach body text
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach file
        try:
            with open(file_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                
                # Add header with filename
                filename = Path(file_path).name
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{filename}"'
                )
                msg.attach(part)
        except Exception as e:
            print(f"❌ Failed to attach file: {e}")
            return False
        
        recipients = [recipient]
        if cc:
            recipients.extend(cc)
        if bcc:
            recipients.extend(bcc)
        
        try:
            with self._create_connection() as server:
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"❌ Failed to send email with attachment: {e}")
            return False
