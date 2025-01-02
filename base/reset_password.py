
# To reset passoword for a superuser.
# Run in interactive shell ie. in terminal below
# call the function as command 
# Before a function call press ctrl+shift+Enter
# Saw in Interactive mode in VS code. 

from django.contrib.auth import get_user_model
print(list(get_user_model().objects.filter(is_superuser=True).values_list('username',flat=True)))
def reset_password(u,password):
    try:
        user=get_user_model().objects.get(username=u)
    except:
        return "User could not be found"
    user.set_password(password)
    user.save()
    return "Password has been changed successfully"
reset_password('Mr.peace','Venky#123$')
    
