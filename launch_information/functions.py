import requests, bs4, pprint
from .models import RocketLaunchData,LaunchSiteData, Facts,PreviousLaunchData

def getLaunchData():
    url = 'https://spaceflightnow.com/launch-schedule/'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content, 'html.parser')

    data = {'dates': [],
            'names': [],
            'times': [],
            'sites': [],
            'country': [],
            'descriptions': []
            }
    selection = soup.select('span.launchdate')
    for s in selection:
        data['dates'].append(s.text.strip())


    selection = soup.select('span.mission')
    for s in selection:
        data['names'].append(s.text.strip())


    selection = soup.select('div.missiondata')
    for s in selection:
        data['times'].append(s.text.strip().split('\n')[0].replace('Launch time:','').strip())
        data['sites'].append(s.text.strip().split('\n')[1].replace('Launch site:','').strip())
        data['country'].append(s.text.strip().split('\n')[1].replace('Launch site:','').strip().split(',')[-1].strip())


    selection = soup.select('div.missdescrip')
    for s in selection:
        data['descriptions'].append(s.text.strip())

    data_list = []

    for i in range(len(data['dates'])):
        d = {}
        d['date'] = data['dates'][i]
        d['name'] = data['names'][i]
        d['time'] = data['times'][i]
        d['site'] = data['sites'][i]
        d['country'] = data['country'][i]
        d['des'] = data['descriptions'][i]
        data_list.append(d)

    return data_list

def save_launch_data_to_db(data):
    for d in data:
        entries = RocketLaunchData.objects.filter(name=d['name'])
        if entries.exists():
            entry = entries.first()
            entry.date = d['date']
            entry.time = d['time']
            entry.country = d['country']
            entry.site = d['site']
            entry.des = d['des']
            entry.save()
        else:
            entry = RocketLaunchData(
            name = d['name'],
            date = d['date'],
            time = d['time'],
            country = d['country'],
            site = d['site'],
            des = d['des']
            )
            entry.save()

def get_launch_sites_data():
    res = requests.get('https://en.wikipedia.org/wiki/List_of_rocket_launch_sites')
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    tables = soup.select('table.wikitable')

    alist= []

    for table in tables:
        slist = []
        trs = table.select('tr')
        for tr in trs:
            sdict = {}
            if trs.index(tr) != 0:
                tds = tr.select('td')
                sdict['country'] = tds[0].text.strip()
                sdict['location'] = tds[1].text.strip()
                sdict['coordinates'] = tds[2].text.strip()
                sdict['operational_date'] = tds[3].text.strip()
                try:
                    sdict['no_of_rockets_launched'] = tds[4].text.strip()
                except:
                    sdict['no_of_rockets_launched'] = None
                try:
                    sdict['heavies_rocket_launched'] = tds[5].text.strip()
                except:
                    sdict['heavies_rocket_launched'] = None
                try:
                    sdict['highest_altitude_achieved'] = tds[6].text.strip()
                except:
                    sdict['highest_altitude_achieved'] = None
                slist.append(sdict)
        alist.extend(slist)
    return alist

def save_sites_data_to_db(data):
    for d in data:
        entries = LaunchSiteData.objects.filter(coordinates=d['coordinates'])
        if entries.exists():
            entry = entries.first()
            entry.country = d['country']
            entry.location = d['location']
            entry.no_of_rockets_launched = d['no_of_rockets_launched']
            entry.heavies_rocket_launched = d['heavies_rocket_launched']
            entry.highest_altitude_achieved = d['highest_altitude_achieved']
            entry.operational_date = d['operational_date']
            entry.save()
        else:
            entry = LaunchSiteData(
            country = d['country'],
            location = d['location'],
            no_of_rockets_launched = d['no_of_rockets_launched'],
            heavies_rocket_launched = d['heavies_rocket_launched'],
            highest_altitude_achieved = d['highest_altitude_achieved'],
            operational_date = d['operational_date'],
            coordinates = d['coordinates']
            )
            entry.save()


def save_facts_to_db(data):
    # for fact in facts:
    #     try:
    #         f = Facts(text=fact)
    #         f.save()
    #     except:
    #         pass
    for d in data:
        try:
            e = Facts(
                title=d['title'],
                text=d['text'],
                img=d['img']
            )
            e.save()
        except Exception as e:
            print(e)
            pass


def get_facts():
    res = requests.get('https://www.factinate.com/things/24-mind-exploding-facts-rocket-science/')
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    alist = []
    div = soup.select('.infinite_holder')
    h2s = div[0].select('h2')
    ps = div[0].select('p')
    imgs = div[0].select('img')
    ps.pop(-1)
    ps.pop(13)
    ps.pop(10)
    ps.pop(0)
    imgs2 = []
    for i in range(len(imgs)):
        if i % 2 != 0:
            imgs2.append(imgs[i])
    for i in range(len(ps)):
        data = {}
        data['title'] = h2s[i].text
        data['text'] = ps[i].text
        data['img'] = imgs2[i].get('src')
        alist.append(data)

    return alist


def get_previous_launch_data():
    res = requests.get('https://www.rocketlaunch.live/?includePast=1')
    soup = bs4.BeautifulSoup(res.content, 'html.parser')
    div = soup.select('div.launchloop')[0]
    rows = div.select('div.row')
    alist = []

    for row in rows:
        data = {}
        try:
            data['date'] = row.select('div.launch_date')[0].text.strip()
            data['time'] = row.select('div.rlt_time')[0].text.strip()
            data['vehicle'] = row.select('div.rlt-vehicle')[0].text.strip()
            data['agency'] = row.select('div.rlt-provider')[0].text.strip()
            data['location'] = row.select('div.rlt-location')[0].text.strip().replace('\t', '').replace('\n', ' ')
            data['name'] = row.select('div.mission_name')[0].text.strip()
            alist.append(data)
        except:
            pass

    return alist


def save_previous_launch_data_to_db(data):
    for d in data:
        try:
            e = PreviousLaunchData(
                name=d['name'],
                date=d['date'],
                time=d['time'],
                vehicle=d['vehicle'],
                agency=d['agency'],
                location=d['location']
            )
            e.save()
        except:
            pass