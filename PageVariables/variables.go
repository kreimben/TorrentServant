package PageVariables

import "github.com/anacrolix/torrent"

type PageVariables struct {
	Title    string
	Message  string
	Torrents []*torrent.Torrent
}
