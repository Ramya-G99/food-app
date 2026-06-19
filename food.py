from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Ramya Food App</h1>
    <h2>Menu</h2>
    <ul>
        <li>Pizza - ₹150</li>
        <li>Burger - ₹100</li>
        <li>Sandwich - ₹80</li>
        <li>French Fries - ₹70</li>
        <li>Cold Drink - ₹40</li>
    </ul>
    """

if __name__ == "__main__":
    app.run()