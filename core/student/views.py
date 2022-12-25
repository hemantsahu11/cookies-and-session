from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Home Page')


def set_cookie(request):
    response = render(request, "student/setcookie.html")
    # response = HttpResponse('cookie set')    # we just have to set cookie via response object
    response.set_cookie('name', 'hemant', max_age=120)   # cookie will last for 120 seconds
    return response


def get_cookie(request):
    name = request.COOKIES.get('name', "not found")
    return render(request, "student/getcookie.html", {'cookie': name})


def del_cookie(request):
    response = render(request, "student/deletecookie.html")
    response.delete_cookie('framework')
    return response


def set_signed_cookie(request):
    response = HttpResponse("setting signed cookies ")
    response.set_signed_cookie('framework', 'django', salt='fr')
    return response


def get_signed_cookie(request):
    framework = request.get_signed_cookie('framework', default="some framework", salt='fr')
    return HttpResponse(framework)


def delete_signed_cookie(request):    # deletion will be same as normal cookie
    pass


"""      session begins from here     """


def set_session(request):
    request.session['name'] = 'Hemant'
    # request.session.set_expiry(600)  # exprity time will set to 600 seconds
    # request.session.set_expiry(0)    # if set to 0 then session will expire when browser will be closed....
    request.session['branch'] = 'computer science'
    return render(request, "student/setsession.html")     # in session we do not need to return response


def get_session(request):            #by default session remains for 2 weeks inside database even after closing browser they are different from cookies
    name = request.session.get('name', "session not found")
    branch = request.session.get('branch', "session not found")
    return render(request, "student/getsession.html", {'name': name, 'branch': branch})

        # session has most of dictionary methods like setdefault , get , items, keys, values , flush()


def delete_session(request):
    # if 'name' in request.session:    # for removing a specific key
    #     del request.session['name']
    request.session.flush()    # deleting whole session all keys and values from sessions table also
    # request.session.clear_expired()   # this will delete the expire sessions from the database and clear the database
    return render(request, "student/deletesession.html")


def run_methods(request):
    return HttpResponse(request.session.get_session_cookie_age())   # age of the session in seconds
    # return HttpResponse(request.session.get_expiry_age())         # time left for session to be expired in seconds
    # return HttpResponse(request.session.get_expiry_date())        # expiry date of session in date format
    # return HttpResponse(request.session.get_expire_at_browser_close())  # session will be deleted on closing browser or not


""" setting cookies using session framework of django
    It has some predefined method for setting and getting cookies so we do not need to do it explicitly """


def set_test_cookie(request):
    request.session.set_test_cookie()
    return render(request, "student/setcookie.html")


def get_test_cookie(request):
    print(request.session.test_cookie_worked())
    return render(request, "student/getcookie.html")


def delete_test_cookie(request):
    request.session.delete_test_cookie
    return render(request, "student/deletesession.html")