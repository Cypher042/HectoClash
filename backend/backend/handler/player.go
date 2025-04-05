package handler

import (
	"github.com/SyncOrSink/HectoClash/backend/database"
	"github.com/SyncOrSink/HectoClash/backend/models"
	"github.com/gofiber/fiber/v2"
)

func PlayerID(c *fiber.Ctx) error {

	id := c.Params("id")

	user := database.GetUserFromID(id)

	if user == (models.UserDetails{}) {
		return c.Status(fiber.StatusNotFound).JSON(user)
	}

	return c.Status(fiber.StatusOK).JSON(user)
}
