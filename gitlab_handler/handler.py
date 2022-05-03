from aiogram.utils.markdown import hlink, quote_html

from gitlab_handler.custom_type import ActionType, EventType
from gitlab_handler.schema import EventObjectModel
from gitlab_handler.handler_errors import NotImplementedStatus


class ProcessingEvent:
    def __init__(self, event: EventObjectModel) -> None:
        self._event = event

        self.message = self._event_to_message()

    def _event_to_message(self):
        if self._event.event_type == EventType.note:
            author = self._event.user
            link = hlink("оставил комментарий", self._event.object_attributes.url)
            comment = quote_html(self._event.object_attributes.description)
            message_text = f"{author.name} {link} \n{comment}"
            return message_text

        if self._event.event_type == EventType.merge_request:
            # merge_request logic
            author = self._event.user
            if self._event.object_attributes.action == ActionType.open:
                text = "Создал"
            elif self._event.object_attributes.action == ActionType.approval:
                text = "Аппрувнул"
            elif self._event.object_attributes.action == ActionType.merge:
                text = "Замерджил"
            elif self._event.object_attributes.action == ActionType.close:
                text = "Закрыл"
            else:
                return None
            link = hlink(f"{text} мердж реквест", self._event.object_attributes.url)
            message_text = f"{author.name} {link}"
            return message_text

        if self._event.object_kind == "pipeline":
            if self._event.object_attributes.status == "failed":
                message_text = f"Пайплайн упал с ошибкой. Ветка - {self._event.object_attributes.ref}"
                return message_text

        raise NotImplementedStatus(
            f"{self._event.event_type} is not impleneted for current handler"
        )
