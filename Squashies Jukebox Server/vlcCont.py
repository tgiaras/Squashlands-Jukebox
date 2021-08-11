import xmltodict, json, requests, subprocess, os
from xml.dom import minidom

class VLC:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8080
        self.password = 'test'
        self.authentication = requests.auth.HTTPBasicAuth('', self.password)

        self.start()

    def cwd(self):
    	print(os.getcwd())

    def start(self):
        subprocess.Popen([
            'C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe',
            #'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe',
            '-I',
            'qt',
            '--extraintf',
            'http',
            '--http-host',
            '%s' % (self.host),
            '--http-port',
            '%s' % (self.port),
            '--http-password',
            '%s' % (self.password)
        ])
    
    def playlist(self,queue):
        response = requests.get('http://localhost:8080/requests/playlist.xml', auth=self.authentication)
        #print(json.dumps(xmltodict.parse(response.text), indent=4))
       
        response = xmltodict.parse(response.text)
        if queue == True:
            try:
                response = response["node"]["node"][0]["leaf"]
            except KeyError:
                return "empty"
        else:
            response = response["node"]["node"][1]["leaf"]

        return response

    def add(self, file):
        params = {'command': 'in_enqueue', 'input': file}
        response = requests.get('http://localhost:8080/requests/playlist.xml',
            params=params, auth=self.authentication)
        # print(json.dumps(xmltodict.parse(response.text), indent=4))

    def addPlaying(self, file):
        params = {'command': 'in_play', 'input': file}
        response = requests.get('http://localhost:8080/requests/playlist.xml',
            params=params, auth=self.authentication)
        # print(json.dumps(xmltodict.parse(response.text), indent=4))

    def remove(self,id):
        params = {'command': 'pl_delete', 'id': id}
        response = requests.get('http://localhost:8080/requests/playlist.xml',
            params=params, auth=self.authentication)

    def fullscreen(self):
        params = {'command': 'fullscreen'}
        response = requests.get('http://localhost:8080/requests/playlist.xml',
            params=params, auth=self.authentication)
        # print(json.dumps(xmltodict.parse(response.text), indent=4))

    def play(self):
        params = {'command': 'pl_play'}
        response = requests.get('http://localhost:8080/requests/playlist.xml',
            params=params, auth=self.authentication)
        # print(json.dumps(xmltodict.parse(response.text), indent=4))

    def pause(self):
        params = {'command': 'pl_pause'}
        response = requests.get('http://localhost:8080/requests/playlist.xml',
            params=params, auth=self.authentication)
        # print(json.dumps(xmltodict.parse(response.text), indent=4))

    def next(self):

        params = {'command': 'pl_next'}
        response = requests.get('http://localhost:8080/requests/playlist.xml',
            params=params, auth=self.authentication)
        # print(json.dumps(xmltodict.parse(response.text), indent=4))

    def previous(self):
        params = {'command': 'pl_previous'}
        response = requests.get('http://localhost:8080/requests/playlist.xml',
            params=params, auth=self.authentication)
        # print(json.dumps(xmltodict.parse(response.text), indent=4))

    