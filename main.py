import requests as requests
from flask import Flask, render_template, request
from contact import Contact

contact = Contact()
app = Flask(__name__)

data = requests.get(url="https://api.npoint.io/9eb91a7a0613d6fcd4a7").json()

@app.route('/')
def home_page():
    return render_template("index.html", posts=data)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact', methods=['POST', 'GET'])
def contact_page():
    if request.method == "POST":
        # data = request.form
        email_data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "number": request.form["phone"],
            "message": request.form["message"]
        }

        contact.send_email(email_data)
        return render_template("contact.html", message="Successfully sent your message!")

    return render_template("contact.html", message="Contact me")

@app.route('/post/<int:id>')
def post_page(id):
    post = [post for post in data if post["id"] == id]
    return render_template("post.html", post=post[0])


if __name__ == "__main__":
    app.run()
