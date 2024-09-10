package main

import (
	"context"
	"log"
	"net/http"

	"github.com/kreimben/TorrentServant/route"
	"github.com/kreimben/TorrentServant/service"
	"go.uber.org/fx"
)

func setupServer(torrentService *service.TorrentService) {
	// Router
	http.HandleFunc("/", route.MainPage(torrentService))
	http.HandleFunc("/api/add", route.AddTorrent(torrentService))

	// Server
	log.Println("Starting server on :8000")
	if err := http.ListenAndServe(":8000", nil); err != nil {
		log.Fatal(err)
	}
}

func main() {
	app := fx.New(
		fx.Provide(service.NewTorrentService),
		fx.Invoke(setupServer),
	)

	if err := app.Start(context.Background()); err != nil {
		log.Fatal(err)
	}
}
