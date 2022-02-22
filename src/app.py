from flask import Flask, request
from src.exceptions.invalid_direction_exception import InvalidDirectionException
from src.exceptions.invalid_sort_by_exception import InvalidSortByException
from src.exceptions.invalid_tag_exception import InvalidTagException
from src.exceptions.missing_tag_exception import MissingTagException
from src.facades.hatchways import HatchwaysFacade
from src.parsers.blog_post import BlogPostParser
from src.handlers.blog_post import BlogPostHandler

app = Flask(__name__)

blog_post_handler = BlogPostHandler(HatchwaysFacade())


@app.route("/api/ping", methods=["GET"])
def ping():
    return {"success": True}, 200


@app.route("/api/posts", methods=["GET"])
def get_posts():

    args = request.args
    tags = args.get("tags")
    direction = args.get("direction")
    sort_by = args.get("sortBy")

    try:
        tags, sort_by, direction = BlogPostParser.parse(
            tags=tags, sort_by=sort_by, direction=direction
        )
    except MissingTagException as e:
        return e.message, 400
    except InvalidSortByException as e:
        return e.message, 400
    except InvalidDirectionException as e:
        return e.message, 400
    except InvalidTagException as e:
        return e.message, 400

    response = blog_post_handler.handle_blogs(
        tags=tags, sort_by=sort_by, direction=direction
    )

    return response, 200
