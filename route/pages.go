package route

import (
	"net/http"
	"text/template"

	pv "github.com/kreimben/TorrentServant/PageVariables"
)

func MainPage(w http.ResponseWriter, r *http.Request) {
	variables := pv.PageVariables{
		Title:   "Welcome to My Website",
		Message: "Hello, World!",
	}

	tmpl, err := template.ParseFiles("templates/main.html")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	tmpl.Execute(w, variables)
}
