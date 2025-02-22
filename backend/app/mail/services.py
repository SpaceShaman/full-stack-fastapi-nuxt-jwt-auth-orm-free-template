from typing import Protocol

from core.settings import BASE_URL
from mail.clients import MailClient


class MailClientInterface(Protocol):
    def send_mail(self, recipients: list[str], subject: str, body: str) -> None: ...


class MailService:
    def __init__(self) -> None:
        self.client: MailClientInterface = MailClient()

    def send_activation_code(self, email: str, activation_code: str) -> None:
        self.client.send_mail(
            [email],
            "Activate your account",
            self._create_activation_email_body(activation_code),
        )

    def _create_activation_email_body(self, activation_code: str) -> str:
        activation_url = f"{BASE_URL}/activate/{activation_code}"
        return f"Click the link to activate your account: {activation_url}"
