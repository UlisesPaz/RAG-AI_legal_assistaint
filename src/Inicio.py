import gradio as gr
from common.rag import respuesta

# Configurar la interfaz con Blocks
with gr.Blocks(css=".small-logo {height: 200px !important; width: auto;}") as iface:
    with gr.Row():
        # Imagen con clase personalizada para tamaño pequeño
        gr.Image("./src/common/logo.jpg", elem_id="logo", interactive=False, show_label=False, type="filepath", elem_classes="small-logo")
        gr.Label("Asistente Legal Virtual")
    gr.ChatInterface(fn=respuesta, 
                     title="Asistente Legal Virtual", 
                     description="Este es un asistente legal experto en responder preguntas de legalidad.")

# Lanzar la interfaz
iface.launch(debug=True)
