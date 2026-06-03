from graph.workflow import app

graph = app.get_graph()

png = graph.draw_mermaid_png()

with open(
    "workflow.png",
    "wb"
) as f:
    f.write(png)