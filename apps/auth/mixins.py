from apps.auth.exceptions import EmailAlreadyInUse
from apps.core.mutations import Output
from .forms import SignupForm

class SignupMixin(Output):
    form = SignupForm
    
    @classmethod
    def resolve_mutation(cls, root, info, *args, **kwargs):
        form = cls.form(data = kwargs)
        if form.is_valid():
            user = form.save()
        raise EmailAlreadyInUse()
        return cls(success = True)