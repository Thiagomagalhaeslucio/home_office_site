# Importa a biblioteca Flask, que é usada para criar o servidor web
from flask import Flask
# Importa o matplotlib para criar gráficos
import matplotlib.pyplot as plt
# Importa bibliotecas para manipular arquivos em memória e converter dados para Base64
import io
import base64

# Cria uma aplicação Flask, que será usada para exibir o site
app = Flask(__name__)

# Função responsável por criar o gráfico com base nos dados
def criar_grafico():
    # Define os períodos de tempo que serão representados no gráfico
    anos = ['Antes da Pandemia', 'Durante a Pandemia', 'Depois da Pandemia']
    # Percentuais de trabalho remoto em cada período
    trabalho_remoto = [5, 70, 30]
    # Percentuais de modelo híbrido em cada período
    modelo_hibrido = [0, 0, 40]

    # Cria o gráfico de barras com uma figura de tamanho 10x6 polegadas
    fig, ax = plt.subplots(figsize=(10, 6))
    # Cria as barras para o trabalho remoto
    ax.bar(anos, trabalho_remoto, label="Trabalho Remoto (%)", color='skyblue')
    # Cria as barras para o modelo híbrido, empilhando-as sobre as barras do trabalho remoto
    ax.bar(anos, modelo_hibrido, label="Modelo Híbrido (%)", bottom=trabalho_remoto, color='orange')

    # Define o título e os rótulos dos eixos do gráfico
    ax.set_title("Mudanças no Modelo de Trabalho (Antes, Durante e Após a Pandemia)", fontsize=14)
    ax.set_xlabel("Período", fontsize=12)
    ax.set_ylabel("Percentual (%)", fontsize=12)
    # Adiciona uma legenda para identificar as cores no gráfico
    ax.legend()
    # Adiciona uma grade horizontal ao gráfico
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    # Salva o gráfico em um buffer de memória no formato PNG
    buf = io.BytesIO()
    plt.tight_layout()  # Ajusta o layout para evitar sobreposição de elementos
    plt.savefig(buf, format="png")  # Salva o gráfico no buffer
    buf.seek(0)  # Move o ponteiro do buffer para o início
    # Converte o gráfico para uma string codificada em Base64 para ser exibido como imagem no navegador
    return base64.b64encode(buf.getvalue()).decode("utf-8")

# Rota principal da aplicação web, que será exibida no navegador ao acessar "/"
@app.route("/")
def home():
    # Gera o gráfico e o converte para o formato Base64
    grafico_base64 = criar_grafico()
    # Retorna o conteúdo HTML da página que será exibida no navegador
    return f"""
    <h1>Trabalho Home Office</h1>
    <h2>Contexto</h2>
    <p>O trabalho home office se tornou relevante principalmente com a pandemia de COVID-19, que forçou muitas empresas a adotarem o trabalho remoto para garantir a continuidade das operações. A transição trouxe desafios, como adaptação tecnológica e equilíbrio entre responsabilidades domésticas e profissionais. Apesar disso, benefícios como flexibilidade e redução de custos foram amplamente percebidos.</p>
    
    <h2>Benefícios</h2>
    <ul>
        <li><strong>Flexibilidade:</strong> 60% dos trabalhadores relataram maior autonomia no home office.</li>
        <li><strong>Redução de custos pessoais:</strong> Economia de até 20% com transporte e alimentação.</li>
        <li><strong>Inclusão:</strong> 25% dos trabalhadores de áreas remotas ou com mobilidade reduzida foram incluídos no mercado.</li>
        <li><strong>Produtividade:</strong> 35% das empresas observaram aumento na eficiência das equipes.</li>
    </ul>
    
    <h2>Malefícios</h2>
    <ul>
        <li><strong>Isolamento social:</strong> Cerca de 40% dos trabalhadores relataram piora na saúde mental.</li>
        <li><strong>Jornadas longas:</strong> 55% relataram aumento na carga horária de trabalho.</li>
        <li><strong>Desigualdade digital:</strong> 30% enfrentaram dificuldades com tecnologia inadequada.</li>
        <li><strong>Gestão de equipes:</strong> 50% dos gestores enfrentaram desafios para supervisionar equipes remotamente.</li>
    </ul>

    <h2>Gráfico - Mudanças no Modelo de Trabalho</h2>
    <!-- Exibe o gráfico gerado dinamicamente -->
    <img src="data:image/png;base64,{grafico_base64}" alt="Gráfico Trabalho Home Office">
    
    <h2>Narrativa</h2>
    <p>O home office transformou o trabalho, impulsionado pela pandemia do século XXI. Antes restrito a freelancers, tornou-se uma solução global. Entre os benefícios, estão a redução do tempo de deslocamento e maior equilíbrio entre vida pessoal e profissional, embora desafios como isolamento social tenham surgido.</p>
    <p>Para as empresas, o modelo remoto exigiu mudanças na liderança, com foco em confiança e resultados. Ele também promoveu contratações globais e equipes diversificadas. Contudo, nem todos se beneficiaram igualmente, evidenciando desigualdades e problemas como o "sempre online".</p>
    <p>O legado do home office é um modelo híbrido que combina flexibilidade e interação presencial, mostrando que o trabalho pode se adaptar às pessoas e não o contrário.</p>
    """

# Inicia o servidor Flask quando o arquivo é executado diretamente
if __name__ == "__main__":
    # Executa o servidor Flask no modo de depuração (útil para desenvolvimento)
    app.run(debug=True)
