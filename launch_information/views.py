from django.shortcuts import render, HttpResponseRedirect, reverse
from . import functions as f
from .models import RocketLaunchData,LaunchSiteData,Facts,Learn,PreviousLaunchData


def upcoming(request):
    data = RocketLaunchData.objects.all()
    return render(request, 'upcoming.html', {'data':data})


def update_launch_data(request):
    data = f.getLaunchData()
    f.save_launch_data_to_db(data)

    return HttpResponseRedirect(reverse('rocket:index'))


def launch_sites(request):
    data = LaunchSiteData.objects.all()
    return render(request, 'launch_sites.html', {'data':data})


def update_launch_sites_data(request):
    data = f.get_launch_sites_data()
    f.save_sites_data_to_db(data)
    return HttpResponseRedirect(reverse('rocket:index'))





def contacts(request):
    return render(request, 'contacts.html')


def pastlaunch(request):
    pass
    return render(request, 'contacts.html')


def facts(request):
    #data = f.get_facts()

    #f.save_facts_to_db(data)
    facts = Facts.objects.all()

    return render(request, 'facts.html', {'facts':facts})

def learn(request):

    learn = Learn.objects.all()

    return render(request,'learn.html',{'learn':learn})

def previous_launch(request):
    data = f.get_previous_launch_data()
    f.save_previous_launch_data_to_db(data)
    return HttpResponseRedirect(reverse('rocket:index'))

def past_launch(request):

    past =PreviousLaunchData.objects.all()

    return render(request,'past_launch.html',{'past':past})