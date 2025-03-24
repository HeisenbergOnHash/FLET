import flet as ft
from css import Main_card_css
from login import login_container


def main(page: ft.Page):
  page.bgcolor = ft.Colors.BLUE_GREY_900
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  page.title = "Testing the Flet of Flutter"
  page.theme_mode = ft.ThemeMode.LIGHT
  page.scroll = ft.ScrollMode.ALWAYS
 
  toggle_bar = ft.Row(controls=[ft.Text("Toggle:", **Main_card_css["toggle_text"]), ft.Switch(**Main_card_css["toggle"])], alignment=ft.MainAxisAlignment.END)
  header_bar = ft.Row(controls=[ft.Text("KasuPay", **Main_card_css["header"])], alignment=ft.MainAxisAlignment.START)
  tag_line_bar = ft.Row(controls=[ft.Text("Your One-Stop Solution for All Your Financial Needs", **Main_card_css["tag_line"])], alignment=ft.MainAxisAlignment.START)

  card = ft.Card(elevation=Main_card_css["card"]["elevation"], 
  content=ft.Container(padding=Main_card_css["card"]["padding"], bgcolor=Main_card_css["card"]["bgcolor"], border_radius=Main_card_css["card"]["border_radius"], 
  content=ft.Column(spacing=Main_card_css["card"]["spacing"], controls=[toggle_bar, header_bar, tag_line_bar])))
  
  # container = ft.Container(content=[card, login_container])
  container = ft.Container(content=ft.Column(
            controls=[card, login_container]),
            alignment=ft.MainAxisAlignment.CENTER)

  page.add(container)


ft.app(target=main, view=ft.AppView.WEB_BROWSER,port=8080)
