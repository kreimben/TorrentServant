package main

import (
	"context"
	"log"
	"net/http"

	"github.com/kreimben/TorrentServant/route"
	"go.uber.org/fx"
)

func setupServer() {
	// Router
	http.HandleFunc("/", route.MainPage)

	// Server
	log.Println("Starting server on :8000")
	if err := http.ListenAndServe(":8000", nil); err != nil {
		log.Fatal(err)
	}
}

func main() {
	app := fx.New(
		fx.Invoke(setupServer),
	)

	if err := app.Start(context.Background()); err != nil {
		log.Fatal(err)
	}
}
