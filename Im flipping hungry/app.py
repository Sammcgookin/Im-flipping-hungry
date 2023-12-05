from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        # Redirect to the result page with the query as a parameter
        return redirect(url_for('result', query=query))

    return render_template('index.html')

@app.route('/result/<query>')
def result(query):
    # For demonstration purposes, use a placeholder image URL
    # You can replace this with actual image URLs or an image search API
    image_url = get_image_url_for_query(query)
    return render_template('result.html', query=query, image_url=image_url)

def get_image_url_for_query(query):
    # Replace this function with actual logic to get image URL for the query
    # For now, use placeholder images for some common queries
    placeholders = {
        'steak': 'https://www.howtocook.recipes/wp-content/uploads/2022/11/rare-steak-recipejpg-500x375.jpg',
        'pizza': 'https://www.simplyrecipes.com/thmb/pjYMLcsKHkr8D8tYixmaFNxppPw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__simply_recipes__uploads__2019__09__easy-pepperoni-pizza-lead-3-8f256746d649404baa36a44d271329bc.jpg',
        'burger': 'https://www.safefood.net/getmedia/d81f679f-a5bc-4a16-a592-248d3b1dc803/burger_1.jpg?w=1280&h=720&ext=.jpg&width=1360&resizemode=force',
    }
    return placeholders.get(query, 'https://dudeproducts.com/cdn/shop/articles/gigachad_1068x.jpg?v=1667928905')  # Default placeholder image

if __name__ == '__main__':
    app.run(debug=True)

