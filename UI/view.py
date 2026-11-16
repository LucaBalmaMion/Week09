from pydoc import text

import flet as ft

class View:
    def __init__(self, page):
        self.page = page
        self.page.title = 'Cineclub - ricorsione'
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controller = None
        self.dd_serate = None
        self.risultati = None

    def set_controller(self, controller):
        self.controller = controller

    def load_interface(self):
        self.dd_serate = ft.Dropdown(
            label='Numero di serate', width=210
        )
        self.dd_serate.options.append(ft.DropdownOption(key = 6,text = 'Sei'))
        self.dd_serate.options.append(ft.DropdownOption(key = 9, text ='Nove'))
        self.dd_serate.options.append(ft.DropdownOption(key = 12, text = 'Dodici'))


        self.risultati = ft.ListView(expand=1, spacing=8, padding=16)
        self.page.add(
            ft.Text('Programma del cineclub', size=24, color='blue'),
            ft.Row([
                self.dd_serate,
                ft.Button(content = 'Statistiche per genere', on_click=self.controller.handle_statistiche),
                ft.Button('Programma ottimo', on_click=self.controller.handle_programma),
            ], alignment=ft.MainAxisAlignment.CENTER),
            self.risultati,
        )

    def mostra(self, righe):
        self.risultati.controls.clear()
        for riga in righe:
            self.risultati.controls.append(ft.Text(str(riga)))
        self.page.update()

    def avviso(self, messaggio):
        self.page.show_dialog(ft.AlertDialog(title=ft.Text(messaggio)))
