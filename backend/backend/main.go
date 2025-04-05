package main

import (
	"log"

	"github.com/SyncOrSink/HectoClash/backend/database"
	"github.com/SyncOrSink/HectoClash/backend/handler"
	"github.com/SyncOrSink/HectoClash/backend/routes"
	"github.com/gofiber/fiber/v2"
)

func main() {
	log.Println("Connecting to DB.")
	disconnect := database.Connect()
	defer disconnect()
	handler.Connect()
	log.Println("Connected to DB.")
	log.Println("Starting Server...")
	database.CreateLeaderBoardIndex()
	log.Println("LeaderBoard")
	app := fiber.New(fiber.Config{
		StrictRouting: true,
		AppName: "HectoClash",
		EnablePrintRoutes: true,
	})
	routes.SetupRoutes(app)
	app.Listen(":8000")
}
