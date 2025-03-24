import flet as ft
 
# Define styles in a dictionary
Main_card_css = {
      "toggle": {
          "value": False,
          "scale": 0.5,
          "active_color": ft.Colors.BLUE,
          "inactive_thumb_color": ft.Colors.GREY_400
      },
      "toggle_text": {
          "size": 1,
          "color": ft.Colors.BLUE_GREY_700
      },
      "header": {
          "size": 45,
          "color": ft.Colors.BLACK,
          "font_family": "Roboto",
          "weight": ft.FontWeight.BOLD,
          "text_align": ft.TextAlign.START
      },
      "tag_line": {
          "size": 15,
          "font_family": "Aerial",
          "text_align": ft.TextAlign.START
      },
      "card": {
          "elevation": 5,
          "padding": 20,
          "bgcolor": ft.Colors.GREEN_50,
          "border_radius": 10,
          "spacing": 5
      }
  }