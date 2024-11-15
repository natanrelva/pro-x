
import json

class CodeGenerator:
    def __init__(self, validated_data):
        self.workflow = validated_data

    def generate_graph_data(self):
        """Convert the workflow to D3.js compatible nodes and links."""
        nodes = []
        links = []

        for state_name, state_data in self.workflow["States"].items():
            nodes.append({"id": state_name, "type": state_data["Type"]})

            if "Next" in state_data:
                links.append({"source": state_name, "target": state_data["Next"]})

            if "Choices" in state_data:
                for choice in state_data["Choices"]:
                    links.append({
                        "source": state_name,
                        "target": choice["Next"],
                        "label": choice.get("Condition", "")
                    })

            if "Default" in state_data:
                links.append({"source": state_name, "target": state_data["Default"], "label": "Default"})

        return {"nodes": nodes, "links": links}

    def generate_html(self, graph_data, output_file="data/workflow_graph.html"):
        """Generates the HTML file with embedded D3.js."""
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <script src="https://d3js.org/d3.v7.min.js"></script>
            <style> circle {{ fill: steelblue; }} line {{ stroke: #999; }}</style>
        </head>
        <body>
            <svg width="800" height="600"></svg>
            <script>
                const data = {json.dumps(graph_data)};
                const svg = d3.select("svg"), width = +svg.attr("width"), height = +svg.attr("height");
                const simulation = d3.forceSimulation(data.nodes).force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
                    .force("charge", d3.forceManyBody()).force("center", d3.forceCenter(width / 2, height / 2));

                const link = svg.append("g").selectAll("line").data(data.links).enter().append("line");
                const node = svg.append("g").selectAll("circle").data(data.nodes).enter().append("circle").attr("r", 10)
                    .call(d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended));

                simulation.on("tick", () => {{
                    link.attr("x1", d => d.source.x).attr("y1", d => d.source.y)
                        .attr("x2", d => d.target.x).attr("y2", d => d.target.y);
                    node.attr("cx", d => d.x).attr("cy", d => d.y);
                }});

                function dragstarted(event, d) {{ if (!event.active) simulation.alphaTarget(0.3).restart(); d.fx = d.x; d.fy = d.y; }}
                function dragged(event, d) {{ d.fx = event.x; d.fy = event.y; }}
                function dragended(event, d) {{ if (!event.active) simulation.alphaTarget(0); d.fx = null; d.fy = null; }}
            </script>
        </body>
        </html>
        """
        with open(output_file, "w") as f:
            f.write(html_template)
    