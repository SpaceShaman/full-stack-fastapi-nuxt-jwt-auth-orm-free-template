from contextlib import contextmanager
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

from core.settings import SMTP_HOST, SMTP_PASSWORD, SMTP_PORT, SMTP_USER

from .exceptions import SMTPEnvError


class MailClient:
    def send_mail(self, recipients: list[str], subject: str, body: str) -> None:
        message = self._generate_message(recipients, subject, body)
        with _create_smtp_connection() as smtp:
            smtp.sendmail(SMTP_USER, recipients, message)

    def _generate_message(self, recipients: list[str], subject: str, body: str) -> str:
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = SMTP_USER
        message["To"] = ", ".join(recipients)
        return message.as_string()


@contextmanager
def _create_smtp_connection():
    if (
        SMTP_HOST is None
        or SMTP_PORT is None
        or SMTP_USER is None
        or SMTP_PASSWORD is None
    ):
        raise SMTPEnvError("SMTP environment variables not set")
    with SMTP_SSL(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        yield smtp
