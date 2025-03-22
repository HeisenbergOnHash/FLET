import flet as ft
import requests

class LoginPage(ft.Column):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success
        self.heading = ft.Text("KasuPay", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.response_text = ft.Text("", size=16, color=ft.Colors.RED)
        self.phone_input = ft.TextField(label="Enter your phone number", keyboard_type=ft.KeyboardType.NUMBER)
        self.username_field = ft.TextField(label="Username", read_only=True, visible=False)
        self.password_field = ft.TextField(label="Enter your password", password=True, visible=False)
        self.submit_button = ft.ElevatedButton(text="Submit", on_click=self.on_submit)
        self.login_button = ft.ElevatedButton(text="Login", visible=False, on_click=self.on_login)
        self.toggle_switch = ft.Switch(on_change=self.on_toggle_change, scale=0.2)
        self.is_manager_mode = False

        # Toggle switch in a row aligned to the top-right
        self.toggle_row = ft.Row(
            controls=[self.toggle_switch],
            alignment=ft.MainAxisAlignment.END
        )

        self.controls = [
            self.toggle_row,  # Add the toggle row at the top
            self.heading, self.phone_input, self.submit_button, self.response_text,
            self.username_field, self.password_field, self.login_button
        ]
        self.alignment = ft.MainAxisAlignment.CENTER
        self.spacing = 20
        self.padding = 20
        self.bgcolor = "#ffffff"
        self.border_radius = 10
        self.width = 400
        self.border = ft.border.all(2, ft.Colors.BLACK)
        self.animate = ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT)

    def on_toggle_change(self, e):
        self.is_manager_mode = self.toggle_switch.value
        self.update()

    def on_submit(self, e):
        phone_number = self.phone_input.value
        mode = "manager" if self.is_manager_mode else "client"
        response = requests.get(f"https://base.finovaapay.com/login/{mode}?phone_number={phone_number}")
        if response.status_code == 200:
            username = response.json().get('message', {}).get('admin_username' if mode == "manager" else 'username', 'Unknown')
            self.username_field.value = username
            self.username_field.visible = True
            self.password_field.visible = True
            self.login_button.visible = True
            self.response_text.value = ""
            self.submit_button.visible = self.phone_input.visible = False
        else:
            self.response_text.value = f"API call failed! Status : {response.text}"
            self.response_text.color = ft.Colors.RED  
        self.update()

    def on_login(self, e):
        username = self.username_field.value
        password = self.password_field.value
        mode = "manager" if self.is_manager_mode else "client"
        response = requests.post(f"https://base.finovaapay.com/login/{mode}", json={"username": username, "password": password})
        if response.status_code == 200:
            self.on_login_success(mode=mode)
        else:
            self.response_text.value = f"Login failed! {response.text}."
            self.response_text.color = ft.Colors.RED  
        self.update()

class ClientDashboard(ft.Column):
    def __init__(self, on_logout):
        super().__init__()
        self.on_logout = on_logout
        
        self.navbar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="DASHBOARD"),
                ft.NavigationBarDestination(icon=ft.icons.HISTORY, label="HISTORY"),
                ft.NavigationBarDestination(icon=ft.icons.PAYMENT, label="PAYIN"),
                ft.NavigationBarDestination(icon=ft.icons.SEND, label="BULK PAYOUT"),
                ft.NavigationBarDestination(icon=ft.icons.LOGOUT, label="LOGOUT"),
            ],
            on_change=self.on_navbar_change)
        self.response_text = ft.Text("", size=16, color=ft.Colors.BLUE, visible=False)
        self.controls = [self.navbar,self.response_text]

    def on_navbar_change(self, e):
        if e.control.selected_index == 4:
            self.on_logout()
        else:  
            self.show_message(f"Function called for index {e.control.selected_index}") 
    
    def show_message(self, message):
        self.response_text.value = message 
        self.response_text.visible = True  
        self.update()  

class ManagerDashboard(ft.Column):
    def __init__(self, on_logout):
        super().__init__()
        self.on_logout = on_logout
        
        self.navbar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="DASHBOARD"),
                ft.NavigationBarDestination(icon=ft.icons.HISTORY, label="USERS"),
                ft.NavigationBarDestination(icon=ft.icons.PAYMENT, label="PAYIN REQUESTS"),
                ft.NavigationBarDestination(icon=ft.icons.SEND, label="MANAGE PAYIN"),
                ft.NavigationBarDestination(icon=ft.icons.LOGOUT, label="LOGOUT"),
            ],
            on_change=self.on_navbar_change)
        self.response_text = ft.Text("", size=16, color=ft.Colors.BLUE, visible=False)
        self.controls = [self.navbar,self.response_text]

    def on_navbar_change(self, e):
        if e.control.selected_index == 4:
            self.on_logout()
        else:  
            self.show_message(f"Function called for index {e.control.selected_index}") 
    
    def show_message(self, message):
        self.response_text.value = message 
        self.response_text.visible = True  
        self.update()  

class DashboardPage(ft.Column):
    def __init__(self, on_logout, mode):
        super().__init__()
        self.on_logout = on_logout
        self.mode = mode
        self.dashboard = ClientDashboard(on_logout=self.on_logout) if mode == "client" else ManagerDashboard(on_logout=self.on_logout)
        self.controls = [self.dashboard]

def main(page: ft.Page):
    page.title = "KasuPay"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.GREEN_50  

    def show_dashboard(mode):
        page.views.clear()
        dashboard_page = DashboardPage(on_logout=show_login, mode=mode)
        page.views.append(ft.View("/", [dashboard_page]))
        page.update()
        page.go("/")

    def show_login():
        page.views.clear()
        login_page = LoginPage(on_login_success=show_dashboard)
        page.views.append(ft.View("/", [ft.Container(
            content=login_page, alignment=ft.alignment.center, expand=True, padding=20, margin=20,
            bgcolor=ft.Colors.WHITE, border_radius=10, shadow=ft.BoxShadow(spread_radius=1, blur_radius=15,
            color=ft.Colors.BLACK26, offset=ft.Offset(0, 0))
        )]))
        page.update()
        page.go("/")

    show_login()
    
ft.app(target=main, view=None, port=5001)
