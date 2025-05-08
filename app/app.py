from shiny.express import render, ui, input

ui.input_text("code", "Enter Code")

@render.express
def dynamic_data():
    if input.code() == "Test":

        ui.h1("Valid Code")

        @render.text
        def data():
            return "This is a test"
        
    else:
        ui.h1("Please enter a code")