import flet as ft
from flet import TextField, Row, Column, ElevatedButton, Container,ControlEvent, Page, ThemeMode, MainAxisAlignment

toggle_style: dict={
    "icon": ft.icons.DARK_MODE_ROUNDED,
    "icon_size": 18}
class Controls(ft.SafeArea):
    def __init__(self) ->None:
        super().__init__()
        self.textfield: TextField=TextField(hint_text="0", multiline=False,text_align=ft.TextAlign.RIGHT, expand=True ,border=ft.InputBorder.OUTLINE, width=430)
        self.toggle: ft.IconButton=ft.IconButton(**toggle_style, on_click=self.switch)
        self.content:Container= Container(bgcolor=ft.colors.BLACK12,border_radius=ft.border_radius.all(20),padding=10,content=Column(controls=[
             Row(controls=[ft.Text(value="STANDARD", color=ft.colors.GREEN_800, style=ft.TextThemeStyle.TITLE_LARGE), self.toggle], alignment="spaceBetween"),
            Row(controls=[self.textfield]),
            Row(controls=[
             ElevatedButton(text="AC", width=100, on_click=self.solution, height=50, data="AC"),
             ElevatedButton(text="±", width=100, height=50, data="±", on_click=self.solution),
             ElevatedButton(text="%", width=100, height=50, data="%", on_click=self.solution),
             ElevatedButton(text="⌫", width=100, height=50, data="⌫", on_click=self.solution)]),
            Row(controls=[
             ElevatedButton(text="7", width=100, on_click=self.solution, height=50, data="7"),
             ElevatedButton(text="8", width=100, height=50, data="8", on_click=self.solution),
             ElevatedButton(text="9", width=100, height=50, data="9", on_click=self.solution),
             ElevatedButton(text="/", width=100, height=50, data="/", on_click=self.solution)]),
            Row(controls=[
             ElevatedButton(text="6", width=100, on_click=self.solution, height=50, data="6"),
             ElevatedButton(text="5", width=100, height=50, data="5", on_click=self.solution),
             ElevatedButton(text="4", width=100, height=50, data="4", on_click=self.solution),
             ElevatedButton(text="*", width=100, height=50, data="*", on_click=self.solution)]),
            Row(controls=[
             ElevatedButton(text="3", width=100, on_click=self.solution, height=50, data="3"),
             ElevatedButton(text="2", width=100, height=50, data="2", on_click=self.solution),
             ElevatedButton(text="1", width=100, height=50, data="1", on_click=self.solution),
             ElevatedButton(text="+", width=100, height=50, data="+", on_click=self.solution)]),
            Row(controls=[
             ElevatedButton(text="0", width=100, on_click=self.solution, height=50, data="0"),
             ElevatedButton(text="00", width=100, height=50, data="00", on_click=self.solution),
             ElevatedButton(text="000", width=100, height=50, data="000", on_click=self.solution),
             ElevatedButton(text="-", width=100, height=50, data="-", on_click=self.solution)]),
            Row(controls=[
             ElevatedButton(text=".", width=100, on_click=self.solution, height=50, data="."),
             ElevatedButton(text="x^2", width=100, height=50, data="x^2", on_click=self.solution),
             ElevatedButton(text="√x", width=100, height=50, data="√x", on_click=self.solution),
             ElevatedButton(text="=", width=100, height=50, data="=", on_click=self.solution,bgcolor=ft.colors.GREEN_800 )
             ])
            ],
            alignment=MainAxisAlignment.CENTER)) 

    
    
    def solution(self,e) -> None:
        if e.control.text== "AC":
            self.textfield.value=""
            self.update()
        elif e.control.text=="=":
            try:
                if "√" in self.textfield.value:
                    self.textfield.value=str(round(float(str.strip(self.textfield.value, "√"))**0.5,7))
                else:
                    self.textfield.value=str(eval(self.textfield.value))
            except:  # noqa: E722
                self.textfield.value="Error"
            self.update()
        elif e.control.text=="±":
            if float(self.textfield.value) > 0:
                self.textfield.value="-" + self.textfield.value
            else:
                self.textfield.value=abs(float(self.textfield.value))
        elif e.control.text=="√x":
            self.textfield.value="√" + self.textfield.value
            self.update()
        elif e.control.text=="x^2":
            self.textfield.value=str(float(self.textfield.value)**2)
        elif e.control.text=="⌫":
            self.textfield.value=self.textfield.value[:-1]
        elif e.control.text=="%":
            self.textfield.value=str(float(self.textfield.value)/100)
        else:
            self.textfield.value+=e.control.text
        self.update()
    
    
    def switch(self, e:ControlEvent):
        if self.page.theme_mode==ThemeMode.DARK:
            self.page.theme_mode=ThemeMode.LIGHT
            self.toggle.icon=ft.icons.LIGHT_MODE_ROUNDED
            self.page.update()
        else:
            self.page.theme_mode=ThemeMode.DARK
            self.toggle.icon=ft.icons.DARK_MODE_ROUNDED
            self.page.update()


def main(page: Page) ->None:
    page.title="Calculator App"
    page.theme_mode=ThemeMode.DARK
    page.window_resizable=False
    page.window_width=490
    page.window_height=550
    page.add(Controls())



if __name__=="__main__":
    ft.app(target=main)
