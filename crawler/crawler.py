from time import ctime

from flask import Blueprint, request

from crawler.crawler_service import get_word_occurrence
from crawler.custom_exceptions import UrlNotFoundException, UrlNotProvidedException

blueprint = Blueprint('crawler', __name__, url_prefix="/")

up_time = ctime()


@blueprint.route("/health", methods=["GET"])
def health():
    return {
        "status": "UP",
        "message": f"alive since {up_time}"
    }


@blueprint.route("/count-words", methods=["GET"])
def count_words():
    try:
        url = request.args.get("url")
        if url is None or url == "":
            return {"error": "Url must be provided"}, 400
        return get_word_occurrence(url)
    except UrlNotFoundException as ex:
        return {"error": ex.message}, 404
    except UrlNotProvidedException as ex:
        return {"error": ex.message}, 400
