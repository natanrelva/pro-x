
from lexer import Lexer
from parser import Parser
from semantic_analyzer import SemanticAnalyzer
from code_generator import CodeGenerator

def main(input_file="data/step_function.json", output_file="data/workflow_graph.html"):
    # Fase 1: Análise Léxica
    lexer = Lexer(input_file)
    tokens = lexer.tokenize()

    # Fase 2: Análise Sintática
    parser = Parser(tokens)
    parsed_data = parser.parse()

    # Fase 3: Análise Semântica
    analyzer = SemanticAnalyzer(parsed_data)
    analyzer.validate()

    # Fase 4: Geração de Código
    generator = CodeGenerator(parsed_data)
    graph_data = generator.generate_graph_data()
    generator.generate_html(graph_data, output_file)

if __name__ == "__main__":
    main()
    