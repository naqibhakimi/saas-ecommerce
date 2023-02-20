from apps.core.querysets import BaseQuerySet


class NoteQuerSet(BaseQuerySet):
    def by_author(self, author):
        return self.filter(author=author)
