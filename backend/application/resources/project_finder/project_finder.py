from flask import Blueprint

project_finder = Blueprint("project_finder", __name__)


@project_finder.route("/home")
@project_finder.route("/")
def project_finder_home():
    return "Project Finder home"
