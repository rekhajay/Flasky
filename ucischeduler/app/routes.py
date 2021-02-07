from app import schedulerapp
from flask import render_template

@schedulerapp.route("/")
def homepage():
    return render_template("index.html", title="HOME PAGE IS RELOADING")

@schedulerapp.route("/makerequest")
def makerequest():

WEBSOC_BASE_URL = "https://www.reg.uci.edu/perl/WebSoc/"


def get_websoc_request(req_args=None, full_request=False):
    headers = {"User-Agent": "Mozilla/5.0"}
    params = dict()
    if req_args:
        params["YearTerm"] = req_args.get("YearTerm")
        params["Breadth"] = req_args.get("Breadth")
        params["Dept"] = req_args.get("Dept")
        params["CourseCodes"] = req_args.get("CourseCodes")
        params["CourseNum"] = req_args.get("CourseNum")
        params["Division"] = req_args.get("Division")
        params["InstrName"] = req_args.get("InstrName")
        params["CourseTitle"] = req_args.get("CourseTitle")
        params["ClassType"] = req_args.get("ClassType")
        params["Units"] = req_args.get("Units")
        params["Days"] = req_args.get("Days")
        params["StartTime"] = req_args.get("StartTime")
        params["EndTime"] = req_args.get("EndTime")
        params["FullCourses"] = req_args.get("FullCourses")
        params["Submit"] = "XML"
    if full_request:
        params["ShowFinals"] = "on"
        params["ShowComments"] = "on"

     requests.get(WEBSOC_BASE_URL, params=params, headers=headers).content


    return render_template("index.html", title="Docs  pagedsd")

@schedulerapp.route("/link1")
def link1():
    return render_template("index.html", title="Link1  page")

@schedulerapp.route("/link2")
def link2():
    return render_template("index.html", title="Link2 page")

