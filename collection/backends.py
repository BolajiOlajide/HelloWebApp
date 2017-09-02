from registration.backends.simple.views import RegistrationView

# my new registration view, subclassing RegistrationView
# from our plugin
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user=None):
        # the named URL that we want to redirect to after
        # successful registration
        user=request.user
        return ('registration_create_resource')