import datetime
from enum import Enum, auto
import libtorrent as lt
import os


class __StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class _CurrentStatus(__StrEnum):
    queued = auto()
    checking = auto()
    downloading_metadata = auto()
    downloading = auto()
    finished = auto()
    seeding = auto()
    allocating = auto()
    checking_fastresume = auto()


# This class is only for concrete session's status.
# You can still get information from its' status object which is actually unknown for general use.
class _SessionInformation:
    def __init__(self, status):
        self.progress = status.progress()
        self.download_rate = status.download_rate()
        self.upload_rate = status.upload_rate()
        self.num_peers = status.num_peers()
        self.current_status = _CurrentStatus(status.state)

    def get_information(self) -> dict[str, str]:
        result = dict()
        result['progress'] = self.progress
        result['download_rate'] = self.download_rate
        result['upload_rate'] = self.upload_rate
        result['num_peers'] = self.num_peers
        result['current_status'] = self.current_status
        return result


class Torrenting:
    __torrent_handle: lt.torrent_handle

    def __init__(self):
        self.session = lt.session()
        self.session.listen_on(6681, 6691)

        self.params = {
            'save_path': self.__get_cwd(),
            # 0 => All pieces will be written to their final position,
            # all files will be allocated in full when the torrent is first started.
            # This mode minimizes fragmentation but could be a costly operation.
            # 1 => All pieces will be written to the place where they belong and sparse files will be used.
            # This is the recommended, and default mode.
            'storage_mode': lt.storage_mode_t(1),
            'paused': False,
            'auto_managed': True,
            'duplicate_is_error': True
        }

        print('params: {}'.format(self.params))
        print('session: {}'.format(self.session))

    def set_magnet_url(self, magnet_url: str):
        # TODO: Load torrent session from magnet url.
        self.__torrent_handle = lt.add_magnet_uri(self.session, magnet_url, self.params)

    def set_torrent_file(self, location: str):
        # TODO: Load torrent session from torrent file. (*.torrent)
        self.params['ti'] = lt.torrent_info(list(location.keys())[0])
        lt.add_torrent(self.params)

    def start(self):
        self.session.start_dht()

    def check_metadata(self) -> bool:
        results = False
        try:
            results = self.__torrent_handle.has_metadata()
        except Exception as e:
            self.__exception_print(e)
        return results

    def get_information(self) -> str:
        return self.__torrent_handle.get_torrent_info()

    def get_session_information(self) -> _SessionInformation:
        return _SessionInformation(self.__torrent_handle.start())

    def get_status(self):
        self.__torrent_handle.status().state

    def __get_cwd(self) -> str:
        current = os.getcwd()
        return current + '/Downloads'

    def __exception_print(self, message):
        print('{}'.format(datetime.datetime.now()))
        print('There is exception: {}'.format(message))
