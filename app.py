import plotly.express as px
from shiny.express import input, render, ui
from shinywidgets import render_plotly

tips = px.data.tips()

with ui.sidebar():
    ui.input_selectize("var", "Select variable", choices=["total_bill", "tip"])

ui.nav_spacer()

with ui.nav_panel("Plot"):
    @render_plotly
    def plot():
        p = px.histogram(tips, x=input.var())
        p.update_layout(height=225)
        return p

with ui.nav_panel("Table"):
    @render.data_frame
    def table():
        return tips[[input.var()]]