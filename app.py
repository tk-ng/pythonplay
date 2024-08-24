from flask import Flask, request

app = Flask(__name__)

POSTS = {
    1: "I like movies!",
    2: "I don't like jackfruit",
    3: "I am watching the Olympics!",
    True: "This is true :-)"
}


@app.route("/")
def home_page():
    html = """
            <html>
                <body>
                    <h1>Home Page!</h1>
                    <p>This is the Home page!</p>
                    <a href="/hello">Go to the hello page</a>
                </body>
            </html>
            """
    return html


@app.route('/hello')
def say_hello():
    html = """
            <html>
                <body>
                    <h1>Hello!</h1>
                    <p>This is the Hello page!</p>
                </body>
            </html>
            """
    return html


@app.route('/goodbye')
def say_goodbye():
    return "<h2>bye bitch</h2>"


@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1> <p>Sorting by: {sort}"


# @app.route('/post', methods=["POST"])
# def post_something():
#     return "You made a post request"

@app.route('/add-comment')
def add_comment_form():
    """Show form for adding a comment"""
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type="text" placeholder="comment" name="comment"/>
        <input type="text" placeholder="username" name="username"/>
        <button>Submit</button>
    </form>
    """


@app.route('/add-comment', methods=["POST"])
def add_comment():
    """Handle adding a comment"""
    ...
    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
    <h1>Saved Your comment</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>
    </ul>
    """


@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"This is the {subreddit} subreddit page"


@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS[id]
    return f"<p>{post}</p>"
