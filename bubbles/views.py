# Create your views here.

#General import
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.utils import simplejson
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
#from django.template import defaultfilters
#from django.core.files import locks

#Models import
#from core.models import PersonType, PersonRank, Person, CompanyType, Company

#Python import
from datetime import datetime, date, timedelta
import os
import shutil

# -----------------------------------------------------------
# Write JSON response to template views
# -----------------------------------------------------------
def json_response(content):
    response = HttpResponse(mimetype="text/plain")

    # Prevent ajax cache in IE8
    response["Cache-Control"] = "max-age=0,no-cache,no-store"

    response.write(simplejson.dumps(content))

    return response

# -----------------------------------------------------------
# Write Text response to template views
# -----------------------------------------------------------
def text_response(content):
    response = HttpResponse(mimetype="text/plain")

    # Prevent ajax cache in IE8
    response["Cache-Control"] = "max-age=0,no-cache,no-store"

    response.write(content)

    return response

# -----------------------------------------------------------
# Load Services page
# -----------------------------------------------------------
from core.models import Post
def bubbles(request):

    test = "test"

    print "salut"

    posts = Post.objects
    posts = posts.filter(is_published=True)
    #return render_to_response('company/company.html',
    return render_to_response('bubbles/post_list.html',
                              {
                                'test': test,
                                'post_list': posts,
                              },
                              context_instance=RequestContext(request))

