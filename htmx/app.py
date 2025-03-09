from flask import Flask, request, render_template_string

app = Flask(__name__)

# Lista para armazenar os itens
items = []

# Rota principal
@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>lista de itens </title>
            <script src="https://unpkg.com/htmx.org"></script>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-gray-100 p-8">
            <div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md">
                <h1 class="text-2xl font-bold mb-4">Lista de Itens</h1>
                <ul id="item-list" class="mb-4">
                    {% for item in items %}
                        <li class="py-2 border-b border-gray-200">{{ item }}</li>
                    {% endfor %}
                </ul>
                <div class="flex gap-2">
                    <input
                        type="text"
                        id="new-item"
                        name="new-item"
                        placeholder="Adicionar item"
                        class="flex-1 p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                    <button
                        hx-post="/add-item"
                        hx-target="#item-list"
                        hx-swap="innerHTML"
                        hx-include="#new-item"
                        class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                        Adicionar
                    </button>
                </div>
            </div>
        </body>
        </html>
    ''', items=items)

# Rota para adicionar itens
@app.route('/add-item', methods=['POST'])
def add_item():
    new_item = request.form.get('new-item')
    if new_item and new_item.strip():
        items.append(new_item.strip())
    return render_template_string('''
        {% for item in items %}
            <li class="py-2 border-b border-gray-200">{{ item }}</li>
        {% endfor %}
    ''', items=items)

if __name__ == '__main__':
    app.run(debug=True)