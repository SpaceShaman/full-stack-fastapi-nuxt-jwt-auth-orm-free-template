from contextlib import contextmanager
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

import settings

from .exceptions import SMTPEnvError


class MailClient:
    def send_mail(self, recipients: list[str], subject: str, body: str) -> None:
        message = self._generate_message(recipients, subject, body)
        with _smtp_connection() as smtp:
            smtp.sendmail(settings.SMTP_USER, recipients, message)

    def _generate_message(self, recipients: list[str], subject: str, body: str) -> str:
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = settings.SMTP_USER
        message["To"] = ", ".join(recipients)
        return message.as_string()


@contextmanager
def _smtp_connection():
    if (
        settings.SMTP_HOST is None
        or settings.SMTP_PORT is None
        or settings.SMTP_USER is None
        or settings.SMTP_PASSWORD is None
    ):
        raise SMTPEnvError("SMTP environment variables not set")
    with SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as smtp:
        smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        yield smtp
