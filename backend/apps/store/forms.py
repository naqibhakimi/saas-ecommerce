from apps.core.forms import BaseForm
from .models import Note


class CreateNoteForm(BaseForm):
    class Meta:
        model = Note
        fields = ("value", "author")


class UpdateNoteForm(BaseForm):
    # [TODO:] how it's work?
    def save(self, commit: bool = ...):
        Note._default_manager.by_author(self.user)
        return super().save(commit)

    class Meta:
        model = Note
        fields = ("id", "value", "author")


class DeleteNoteForm(BaseForm):
    class Meta:
        model = Note
        fields = ("id",)
