# from .models import Person 
# from leadmanagement.messages.errors import (PERMISSION_DENIED, INVITATION_EXPIRED)
# from rest_framework.exceptions import ValidationError
# from ..utill.utills import (generate_random_string, now)


# class PersonService:  
#     def _send_invitation_mail(user:Person ,invitation_token):
#         subject = 'Thank you for registering to our site'
#         message = 'message'
#         email_from = settings.EMAIL_HOST_USER
#         recived_data = request.data
#         recipient_list = [recived_data]
#         send_mail(subject, message, email_from, recipient_list)
#         return HttpResponse('Sent')

#     def invite_user(self, user: Person):
#         self.validate_user_before_registration(user)
#         invitation_token = generate_random_string(40)
#         is_sent = self._send_invitation_mail(user, invitation_token)


#     def validate_user_before_registration(self, user: Person):
#         if user.is_active:
#             raise ValidationError({"Status": [PERMISSION_DENIED]})
#         if user.invitation_expires_at < now():
#             raise ValidationError({"invitation_expires_at": [INVITATION_EXPIRED]})

#     def register_user(self, user: Person):
#         user.is_active = True
#         user.invitation_token = None
#         user.invitation_expires_at = None
#         user.save()