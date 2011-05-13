"""
Download a current extract of the PivotalTracker database as a CSV

"""
import urllib, urllib2, cookielib

def download(project_id, username, password):

    cj = cookielib.LWPCookieJar()
    urllib2.install_opener(urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)))
    login_form = urllib2.urlopen('https://www.pivotaltracker.com/projects/%s' % project_id).read()
    values = {'credentials[username]' : username,
              'credentials[password]' : password}
    params = urllib.urlencode(values)          
    main_page = urllib2.urlopen('https://www.pivotaltracker.com/signin', params).read()

    values = {'options[include_done_stories]' : 1,
              'options[include_current_backlog_stories]' : 1,
              'options[include_icebox_stories]' : 1}
    params = urllib.urlencode(values)          
    csv = urllib2.urlopen('https://www.pivotaltracker.com/projects/%s/export' % project_id, params)
    return csv
