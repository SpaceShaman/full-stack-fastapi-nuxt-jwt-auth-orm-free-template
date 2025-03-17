from pathlib import Path
from typing import Protocol

from core.settings import BASE_URL
from jinja2 import Template
from mail.client import MailClient


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
        with open(Path(__file__).parent / "templates/activation_email.html") as file:
            template = Template(file.read())
        activation_url = f"{BASE_URL}/activate/{activation_code}"
        return template.render(activation_url=activation_url)
