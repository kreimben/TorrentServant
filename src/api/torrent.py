import libtorrent as lt


def ready():
    session = lt.session({'listen_interfaces': '0.0.0.0:6881'})
