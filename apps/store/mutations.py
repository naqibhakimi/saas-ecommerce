import graphene
from apps.core.mutations import RelayMutationMixin, DynamicInputMixin
from .mixins import UpdateAddressMixin
from .forms import CreateNoteForm, UpdateNoteForm, DeleteNoteForm
from graphene_django.forms.mutation import DjangoModelFormMutation
from .types import NoteNode
class CreateNote(DjangoModelFormMutation):
    class Meta:
        form_class = CreateNoteForm

class UpdateNote(DjangoModelFormMutation):
    class Meta:
        form_class = UpdateNoteForm


class DeleteNote(DjangoModelFormMutation):
    class Meta:
        form_class = DeleteNoteForm

class UpdateAddress(
        UpdateAddressMixin,
        RelayMutationMixin,
        DynamicInputMixin,
        graphene.ClientIDMutation):
    pass


class SalesChannel(
    RelayMutationMixin,
    DynamicInputMixin,
    UpdateAddressMixin,
    graphene.ClientIDMutation
):
    pass


class Mutation:
    create_note = CreateNote.Field()
    update_note = UpdateNote.Field()
    delete_note = DeleteNote.Field()
