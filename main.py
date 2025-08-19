# Certifique-se de que a biblioteca flask_cors está instalada:
# pip install Flask Flask-Cors

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# A linha abaixo permite pedidos de qualquer origem.
# Por uma questão de segurança, pode substituí-lo pelo seu domínio:
# CORS(app, origins="https://98webmanager.netlify.app")
CORS(app)

# Este é o ponto de acesso que a sua aplicação web irá chamar.
@app.route("/translate", methods=['POST', 'OPTIONS'])
def translate():
    if request.method == 'OPTIONS':
        # Responder ao pedido OPTIONS para satisfazer o CORS.
        # Isto é necessário para que o navegador saiba que pode prosseguir.
        return jsonify({'message': 'CORS preflight request successful'}), 200
    
    # Processar o pedido POST de tradução.
    # Exemplo:
    try:
        data = request.json
        text = data.get('text', '')
        source_lang = data.get('source', '')
        target_lang = data.get('target', '')

        # Aqui é onde faria a chamada real para o LibreTranslate
        # ou outro motor de tradução. Por agora, vamos retornar uma resposta de exemplo.
        translated_text = f"Texto traduzido para {target_lang}: {text}"
        
        return jsonify({
            'translatedText': translated_text,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # O Render usa a variável de ambiente PORT.
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
