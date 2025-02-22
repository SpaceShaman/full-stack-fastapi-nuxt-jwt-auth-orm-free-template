from typing import Protocol

from mail.clients import MailClient


class MailClientInterface(Protocol):
    def send_mail(self, recipients: list[str], subject: str, body: str) -> None: ...


class MailService:
    def __init__(self) -> None:
        self.client: MailClientInterface = MailClient()

    def send_activation_code(self, email: str, activation_url: str) -> None:
        self.client.send_mail(
            [email],
            "Activate your account",
            f"Click the link to activate your account: {activation_url}",
        )
