import json

from flask import Flask, jsonify, request

from model.post import Post

posts = []

app = Flask(__name__)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return {'post_id': obj.post_id, 'title': obj.title, 'body': obj.body, 'author': obj.author}
        else:
            return super().default(obj)


@app.route('/posts', methods=['POST'])
def create_post():
    post_json = request.get_json()
    post = Post(post_json['post_id'], post_json['title'], post_json['body'], post_json['author'])

    posts.append(json.loads(json.dumps(post, cls=CustomJSONEncoder)))
    return jsonify({'posts': posts})


@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({'posts': posts})


@app.route('/posts/<int:posts_id>', methods=['GET', 'DELETE', 'PUT'])
def single_post(posts_id):
    for i in range(len(posts)):
        if posts[i]['post_id'] == posts_id:
            if request.method == 'GET':
                return jsonify({'post': posts[i]})
            elif request.method == 'DELETE':
                posts.pop(i)
                return jsonify({'posts': posts})
            elif request.method == 'PUT':
                post_json = request.get_json()
                post = Post(post_json['post_id'], post_json['title'], post_json['body'], post_json['author'])
                title = post_json['title']
                body = post_json['body']
                post.title = title
                post.body = body
                posts[i].update(title=post.title, body=post.body)
                return jsonify(posts[i])


if __name__ == '__main__':
    app.run(debug=True)
