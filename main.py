import flet as ft
from database_func import TABELLE_VALIDE, get_tabella_dati


def main(page: ft.Page):
    # Configurazione della pagina
    page.title = "ARCHEO TEST"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window.width = 1100
    page.window.height = 750

    # Stato dell'applicazione
    tabella_corrente = None

    # Elementi dell'interfaccia
    titolo_principale = ft.Text(
        "ARCHEO TEST",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    titolo_tabella = ft.Text(
        "Seleziona una tabella per visualizzare i dati",
        size=20,
        weight=ft.FontWeight.W_600,
    )

    txt_ricerca = ft.TextField(
        label="Cerca nei dati",
        hint_text="Digita una parola, data o numero...",
        expand=True,
        dense=True,
        on_submit=lambda e: esegui_filtro(e),
    )

    btn_filtro = ft.Button(
        "FILTRO",
        icon=ft.Icons.SEARCH,
        on_click=lambda e: esegui_filtro(e),
    )

    btn_azzera = ft.Button(
        "AZZERA FILTRO",
        icon=ft.Icons.CLEAR,
        on_click=lambda e: azzera_filtro(e),
    )

    riga_filtri = ft.Row(
        controls=[txt_ricerca, btn_filtro, btn_azzera],
        visible=False,
    )

    # Contenitore della tabella dati
    tabella_container = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, expand=True)

    def carica_dati(nome_tabella: str, filtro: str = ""):
        """Esegue la query e aggiorna il controllo DataTable."""
        try:
            colonne, righe = get_tabella_dati(nome_tabella, filtro)

            if not colonne:
                tabella_container.controls = [
                    ft.Text("Nessuna colonna o tabella vuota.")
                ]
                page.update()
                return

            # Costruzione dinamica delle colonne
            data_columns = [
                ft.DataColumn(
                    ft.Text(col.upper(), weight=ft.FontWeight.BOLD),
                )
                for col in colonne
            ]

            # Costruzione dinamica delle righe
            data_rows = []
            for riga in righe:
                celle = [
                    ft.DataCell(
                        ft.Text(str(valore) if valore is not None else "-")
                    )
                    for valore in riga
                ]
                data_rows.append(ft.DataRow(cells=celle))

            if not data_rows:
                tabella_container.controls = [
                    ft.Text(
                        "Nessun record trovato per i criteri specificati.",
                        italic=True,
                        size=15,
                    )
                ]
            else:
                dt = ft.DataTable(
                    columns=data_columns,
                    rows=data_rows,
                    border=ft.Border.all(1, ft.Colors.GREY_300),
                    vertical_lines=ft.BorderSide(1, ft.Colors.GREY_200),
                    heading_row_color=ft.Colors.GREY_100,
                    divider_thickness=1,
                )
                # Contenitore orizzontale scorrevole per tabelle larghe
                tabella_container.controls = [
                    ft.Row(controls=[dt], scroll=ft.ScrollMode.ADAPTIVE)
                ]

        except Exception as err:
            tabella_container.controls = [
                ft.Text(
                    f"Errore connessione/query: {err}",
                    color=ft.Colors.RED_600,
                    weight=ft.FontWeight.BOLD,
                )
            ]

        page.update()

    def seleziona_tabella(nome: str):
        nonlocal tabella_corrente
        tabella_corrente = nome
        txt_ricerca.value = ""
        riga_filtri.visible = True
        titolo_tabella.value = f"Visualizzazione Dati Tabella: {nome}"
        carica_dati(nome)

    def esegui_filtro(e):
        if tabella_corrente:
            carica_dati(tabella_corrente, txt_ricerca.value)

    def azzera_filtro(e):
        if tabella_corrente:
            txt_ricerca.value = ""
            carica_dati(tabella_corrente, "")

    # Creazione dei pulsanti delle tabelle
    riga1_nomi = ["sito", "cantiere", "quadrante", "archeologo", "missione"]
    riga2_nomi = ["unita_stratigrafica", "media"]

    pulsanti_riga1 = [
        ft.Button(
            t.upper(),
            on_click=lambda e, t_name=t: seleziona_tabella(t_name),
        )
        for t in riga1_nomi
    ]

    pulsanti_riga2 = [
        ft.Button(
            t.upper().replace("_", " "),
            on_click=lambda e, t_name=t: seleziona_tabella(t_name),
        )
        for t in riga2_nomi
    ]

    # Layout complessivo
    page.add(
        ft.Container(
            content=titolo_principale,
            alignment=ft.Alignment(0, 0),
            padding=ft.Padding(0, 0, 0, 10),
        ),
        ft.Row(controls=pulsanti_riga1, wrap=True, spacing=10),
        ft.Row(controls=pulsanti_riga2, wrap=True, spacing=10),
        ft.Divider(height=25, thickness=1.5),
        titolo_tabella,
        ft.Container(height=10),
        riga_filtri,
        ft.Container(height=15),
        tabella_container,
    )


if __name__ == "__main__":
    ft.run(main)