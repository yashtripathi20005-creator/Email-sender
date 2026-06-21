"""
Email templates for common use cases.
"""

from datetime import datetime
from typing import Tuple


class EmailTemplates:
    """Email templates for various purposes."""
    
    @staticmethod
    def welcome_email(name: str) -> Tuple[str, str]:
        """
        Generate a welcome email template.
        
        Args:
            name: Recipient's name
            
        Returns:
            Tuple of (subject, body)
        """
        subject = f"Welcome to Our Service, {name}!"
        
        body = f"""
Dear {name},

Welcome to our service! We're thrilled to have you on board.

We're committed to providing you with the best experience possible. Here are a few things you can do to get started:

1. Complete your profile
2. Explore our features
3. Connect with other users
4. Check out our documentation

If you have any questions, please don't hesitate to reach out to our support team.

Best regards,
The Team

---
This is an automated message. Please do not reply directly to this email.
"""
        return subject, body
    
    @staticmethod
    def notification_email(title: str, message: str) -> Tuple[str, str]:
        """
        Generate a notification email template.
        
        Args:
            title: Notification title
            message: Notification message
            
        Returns:
            Tuple of (subject, body)
        """
        subject = f"Notification: {title}"
        
        body = f"""
Notification: {title}

Dear User,

{message}

Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

If you have any questions, please contact our support team.

Best regards,
The Team

---
This is an automated notification. Please do not reply directly to this email.
"""
        return subject, body
    
    @staticmethod
    def password_reset_email(name: str, reset_link: str) -> Tuple[str, str]:
        """
        Generate a password reset email template.
        
        Args:
            name: Recipient's name
            reset_link: Password reset link
            
        Returns:
            Tuple of (subject, body)
        """
        subject = "Password Reset Request"
        
        body = f"""
Dear {name},

We received a request to reset your password. To reset your password, please click the link below:

{reset_link}

If you did not request a password reset, please ignore this email or contact our support team.

This link will expire in 24 hours.

Best regards,
The Team

---
This is an automated message. Please do not reply directly to this email.
"""
        return subject, body
    
    @staticmethod
    def order_confirmation_email(
        name: str,
        order_id: str,
        items: list,
        total: float
    ) -> Tuple[str, str]:
        """
        Generate an order confirmation email template.
        
        Args:
            name: Recipient's name
            order_id: Order ID
            items: List of items in the order
            total: Total order amount
            
        Returns:
            Tuple of (subject, body)
        """
        subject = f"Order Confirmation #{order_id}"
        
        items_list = "\n".join([f"  • {item}" for item in items])
        
        body = f"""
Dear {name},

Thank you for your order! Your order has been confirmed.

Order Details:
--------------
Order ID: {order_id}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Items Ordered:
{items_list}

Total Amount: ${total:.2f}
--------------

We'll notify you when your order has been shipped.

If you have any questions about your order, please contact our customer support.

Best regards,
The Team

---
This is an automated confirmation. Please do not reply directly to this email.
"""
        return subject, body
