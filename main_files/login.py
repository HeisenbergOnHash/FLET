
import flet as ft

def on_submit(e):
    response_text.value = "Submitted!"
    e.page.update()

def on_login(e):
    response_text.value = "Logging in..."
    e.page.update()


response_text = ft.Text("", size=16, color=ft.Colors.RED)
phone_input = ft.TextField(label="Enter your phone number", keyboard_type=ft.KeyboardType.NUMBER)
username_field = ft.TextField(label="Username", read_only=True, visible=False)
password_field = ft.TextField(label="Enter your password", password=True, visible=False)
submit_button = ft.ElevatedButton(text="Submit", on_click=on_submit)
login_button = ft.ElevatedButton(text="Login", visible=False, on_click=on_login)

login_container = ft.Container(
    content=ft.Column(
        controls=[
            phone_input,
            username_field,
            password_field,
            submit_button,
            login_button,
            
            response_text,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width= 400,
        height= 400,
    ),
    padding=20,width= 500,
    border_radius=10,
    bgcolor=ft.Colors.BLUE_GREY_100,
    visible=True,
    
)