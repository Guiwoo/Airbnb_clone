from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """Conversation Model Definition"""

    particpants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.particpants.all():
            usernames.append(user.username)
        return " ,".join(usernames)

    def count_message(self):
        return self.messages.count()

    count_message.short_description = "Number of Message"

    def count_particpants(self):
        return self.particpants.count()

    count_particpants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):

    """Message Modle Definition"""

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says : {self.message}"
