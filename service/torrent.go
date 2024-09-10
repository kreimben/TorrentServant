package service

import (
	"github.com/anacrolix/torrent"
)

type TorrentService struct {
	client   *torrent.Client
	torrents map[string]*torrent.Torrent
}

func NewTorrentService() (*TorrentService, error) {
	client, err := torrent.NewClient(nil)
	if err != nil {
		return nil, err
	}
	return &TorrentService{
		client:   client,
		torrents: make(map[string]*torrent.Torrent),
	}, nil
}

func (s *TorrentService) AddTorrent(magnetLink string) error {
	t, err := s.client.AddMagnet(magnetLink)
	if err != nil {
		return err
	}
	s.torrents[t.InfoHash().HexString()] = t
	go s.downloadTorrent(t)
	return nil
}

func (s *TorrentService) GetTorrents() []*torrent.Torrent {
	torrents := make([]*torrent.Torrent, 0, len(s.torrents))
	for _, t := range s.torrents {
		torrents = append(torrents, t)
	}
	return torrents
}

func (s *TorrentService) downloadTorrent(t *torrent.Torrent) {
	<-t.GotInfo()
	t.DownloadAll()
}
