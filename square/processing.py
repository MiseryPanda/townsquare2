
from django.contrib.auth.models import User
from square.models import Volunteer, Event, EventLocation
from square.utils import gen_password


def process_volunteer(first, last, uname=None, pw=None):

    v = Volunteer()

    if not uname:
        # if a username is not provided, make one from 
        # first name, last name, and sign up date
        uname = '{0}{1}:{2}' % \
            (first, last, v.signup_date.strftime('%m-%d-%y'))

    if not pw:
        # if a password is not provided, generate a random one 
        pw = gen_password(length=8)

    # associate a django user object with this volunteer
    u = User.objects.create_user(
        first_name=first, 
        last_name=last, 
        password=pw, 
        username=uname)

    u.save()
    v.save()

    return v

    
def process_event(event_type, event_location, date, start_time, end_time, 
                    notes, is_volunteer_time):
    
    e = Event(
        event_type=event_type,
        event_location=event_location,
        date=date,
        start=start_time,
        end=end_time,
        notes=notes,
        is_volunteer_time=is_volunteer_time)
    
    e.save()
    
    return e
