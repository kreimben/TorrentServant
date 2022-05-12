import libtorrent as lt


class Torrent:
    def __init__(self):
        self.session = lt.session({'listen_interfaces': '0.0.0.0:6881'})
        print('session: {}'.format(self.session))
        lt
