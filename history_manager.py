from collections import defaultdict
from gigachat.models import Chat, Messages, MessagesRole
from config import TEMPERATURE, MAX_TOKENS, SYSTEM_ROLE_CONTENT
from typing import Dict


def create_user_history():
    return Chat(
        messages=[Messages(role=MessagesRole.SYSTEM, content=SYSTEM_ROLE_CONTENT)],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )


user_histories: Dict[int, Chat] = defaultdict(create_user_history)
