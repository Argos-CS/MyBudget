import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

# ========= Layout ========= #
layout = dbc.Col([
    html.H1("Financeiro", className="text-primary"),
    html.P("by Info Servive 24h", className="text-info"),
    html.Hr(),

    # Seção PERFIL -----------------------
    dbc.Button(id='botao_avatar',
               children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
                         ],
               style={'background-color': 'transparent', 'border-color': 'transparent'}),

    # Seção NOVO -----------------------
    dbc.Row([
        dbc.Col([
            dbc.Button(color='success', id='open-novo-receita',
                       children=['+ Receita']),
        ], width=6),
        dbc.Col([
            dbc.Button(color='danger', id='open-novo-despesa',
                       children=['- Despesa']),
        ], width=6)
    ]),

    # Modal Receita
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar receita')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-receita"),
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor: "),
                    dbc.Input(placeholder="100.00", id="valor-receita", value="")
                ], width=6)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date_receitas',
                                         min_date_allowed=date(2020, 1, 1),
                                         max_date_allowed=date(2030, 12, 31),
                                         date=datetime.today(),
                                         display_format='DD/MM/YYYY',  # Formato desejado da data
                                         style={"width": "100%"}
                                         ),
                ], width=4),

                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[],
                        value=[],
                        id='switch-input-receita',
                        switch=True
                    )
                ], width=4),

                dbc.Col([
                    html.Label('Categoria da receita'),
                    dbc.Select(id='select_receita', options=[], value=[])
                ], width=4)
            ], style={'margin-top': '25px'}),





            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color': 'green'}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-receita", value=""),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-receita", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend('Excluir categorias', style={'color': 'red'}),
                                dbc.Checklist(
                                    id='checklist-selected-style-receita',
                                    options=[],
                                    value=[],
                                    label_checked_style={'color': 'red'},
                                    input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange'},
                                ),
                                dbc.Button('Remover', color='warning', id='remove-category-receita', style={'margin-top': '20px'}),
                            ], width=6)
                        ])
                    ], title='Adicionar/Remover Categorias')
                ], flush=True, start_collapsed=True, id='accordion-receita'),
            
                html.Div(id='id_teste_receita', style={'padding-top': '20px'}),
                dbc.ModalFooter([
                    dbc.Button("Adicionar Receita", id="salvar_receita", color="sucess"),
                    dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click"),
                ])
            ], style={'margin-top': '25px'})
        ])
    ], style={"background-color": "rgba(17, 140, 70, 0.05)"},
    id="modal-novo-receita",
    size="lg",
    is_open=False,
    centered=True,
    backdrop=True),

    # Modal Despesa
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar despesa')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(placeholder="Ex.: Água, Luz, Telefone, Internet ...", id="txt-despesa"),
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor: "),
                    dbc.Input(placeholder="100.00", id="valor-despesa", value="")
                ], width=6)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date_despesas',
                                         min_date_allowed=date(2020, 1, 1),
                                         max_date_allowed=date(2030, 12, 31),
                                         date=datetime.today(),
                                         display_format='DD/MM/YYYY',  # Formato desejado da data
                                         style={"width": "100%"}
                                         ),
                ], width=4),

                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[],
                        value=[],
                        id='switch-input-despesa',
                        switch=True
                    )
                ], width=4),

                dbc.Col([
                    html.Label('Categoria da despesa'),
                    dbc.Select(id='select_despesa', options=[], value=[])
                ], width=4)
            ], style={'margin-top': '25px'}),





            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color': 'green'}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-depesa", value=""),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-despesa", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend('Excluir categorias', style={'color': 'red'}),
                                dbc.Checklist(
                                    id='checklist-selected-style-despesa',
                                    options=[],
                                    value=[],
                                    label_checked_style={'color': 'red'},
                                    input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange'},
                                ),
                                dbc.Button('Remover', color='warning', id='remove-category-despesa', style={'margin-top': '20px'}),
                            ], width=6)
                        ])
                    ], title='Adicionar/Remover Categorias')
                ], flush=True, start_collapsed=True, id='accordion-despesa'),
            
                html.Div(id='id_teste_despesa', style={'padding-top': '20px'}),
                dbc.ModalFooter([
                    dbc.Button("Adicionar Despesa", id="salvar_despesa", color="sucess"),
                    dbc.Popover(dbc.PopoverBody("Despessa Salva"), target="salvar_despesa", placement="left", trigger="click"),
                ])
            ], style={'margin-top': '25px'})
        ])
    ], style={"background-color": "rgba(17, 140, 70, 0.05)"},
    id="modal-novo-despesa",
    size="lg",
    is_open=False,
    centered=True,
    backdrop=True),
  

    # Modal Receita
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar receita')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-receita"),
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor: "),
                    dbc.Input(placeholder="100.00", id="valor-receita", value="")
                ], width=6)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date_receitas',
                                         min_date_allowed=date(2020, 1, 1),
                                         max_date_allowed=date(2030, 12, 31),
                                         date=datetime.today(),
                                         display_format='DD/MM/YYYY',  # Formato desejado da data
                                         style={"width": "100%"}
                                         ),
                ], width=4),

                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[],
                        value=[],
                        id='switch-input-receita',
                        switch=True
                    )
                ], width=4),

                dbc.Col([
                    html.Label('Categoria da receita'),
                    dbc.Select(id='select_receita', options=[], value=[])
                ], width=4)
            ], style={'margin-top': '25px'}),





            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color': 'green'}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-receita", value=""),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-receita", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend('Excluir categorias', style={'color': 'red'}),
                                dbc.Checklist(
                                    id='checklist-selected-style-receita',
                                    options=[],
                                    value=[],
                                    label_checked_style={'color': 'red'},
                                    input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange'},
                                ),
                                dbc.Button('Remover', color='warning', id='remove-category-receita', style={'margin-top': '20px'}),
                            ], width=6)
                        ])
                    ], title='Adicionar/Remover Categorias')
                ], flush=True, start_collapsed=True, id='accordion-receita'),
            
                html.Div(id='id_teste_receita', style={'padding-top': '20px'}),
                dbc.ModalFooter([
                    dbc.Button("Adicionar Receita", id="salvar_receita", color="sucess"),
                    dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click"),
                ])
            ], style={'margin-top': '25px'})
        ])
    ], style={"background-color": "rgba(17, 140, 70, 0.05)"},
    id="modal-novo-receita",
    size="lg",
    is_open=False,
    centered=True,
    backdrop=True),

    # Modal Despesa
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar despesa')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(placeholder="Ex.: aluguel, luz, compras...", id="txt-despesa"),
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor: "),
                    dbc.Input(placeholder="100.00", id="valor-despesa", value="")
                ], width=6)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date_despesas',
                                         min_date_allowed=date(2020, 1, 1),
                                         max_date_allowed=date(2030, 12, 31),
                                         date=datetime.today(),
                                         style={"width": "100%"}
                                         ),
                ], width=4),

                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[],
                        value=[],
                        id='switch-input-despesa',
                        switch=True
                    )
                ], width=4),

                dbc.Col([
                    html.Label('Categoria da despesa'),
                    dbc.Select(id='select_despesa', options=[], value=[])
                ], width=4)
            ], style={'margin-top': '25px'}),

            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={'color': 'green'}),
                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-despesa", value=""),
                                html.Br(),
                                dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(id="category-div-add-despesa", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend('Excluir categorias', style={'color': 'red'}),
                                dbc.Checklist(
                                    id='checklist-selected-style-despesa',
                                    options=[],
                                    value=[],
                                    label_checked_style={'color': 'red'}, input_checked_style={'backgroundColor': 'blue', 'borderColor': 'orange'},
                                ),
                                dbc.Button('Remover', color='warning', id='remove-category-despesa', style={'margin-top': '20px'}),
                            ], width=6)
                        ])
                    ], title='Adicionar/Remover Categorias')
                ], flush=True, start_collapsed=True, id='accordion-despesa'),
            
                html.Div(id='id_teste_despesa', style={'padding-top': '20px'})
            ])
        ]),
    ], id='modal-despesa', is_open=False),

    # Seção NAV -----------------------
    html.Hr(),
    dbc.Nav(
        [
            dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
            dbc.NavLink("Extratos", href="/extratos", active="exact"),
        ], vertical=True, pills=True, id='nav-buttons', style={"margin-bottom": "50px"})
])

# ========= Callbacks ========= #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal_receita(n1, is_open):
    if n1:
        return not is_open
    return is_open

# Pop-up despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal_despesa(n1, is_open):
    if n1:
        return not is_open
    return is_open