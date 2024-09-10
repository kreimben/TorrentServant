package route

import (
	"encoding/json"
	"html/template"
	"net/http"

	pv "github.com/kreimben/TorrentServant/PageVariables"
	"github.com/kreimben/TorrentServant/service"
)

func MainPage(ts *service.TorrentService) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		variables := pv.PageVariables{
			Title:    "Torrent Downloader",
			Message:  "Add and manage your torrents",
			Torrents: ts.GetTorrents(),
		}

		tmpl, err := template.ParseFiles("templates/main.html")
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		tmpl.Execute(w, variables)
	}
}

func AddTorrent(ts *service.TorrentService) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
			return
		}

		var data struct {
			MagnetLink string `json:"magnet_link"`
		}

		if err := json.NewDecoder(r.Body).Decode(&data); err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}

		if err := ts.AddTorrent(data.MagnetLink); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		w.WriteHeader(http.StatusCreated)
	}
}
