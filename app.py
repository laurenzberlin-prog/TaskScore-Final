from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from database import (
    init_db,
    verify_user,
    create_user,
    get_total_points,
    get_user_done_score,
    get_all_tasks,
    insert_task,
    toggle_task_status,
    delete_task,
    get_weekly_points,
    get_done_points,
)

app = Flask(__name__)
app.secret_key = "dev-secret-change-me"  
BUDGET = 100

init_db()


def current_user_id():
    return session.get("user_id")


def login_required():
    return current_user_id() is not None


@app.route("/")
def start():
    if not login_required():
        return redirect(url_for("login"))

    uid = current_user_id()
    return render_template(
        "home.html",
        current_total=get_total_points(uid),
        budget=BUDGET,
        done_score=get_user_done_score(uid),
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        user_id = verify_user(request.form["username"], request.form["password"])
        if user_id:
            session["user_id"] = user_id
            return redirect(url_for("start"))
        error = "Login fehlgeschlagen."

    return render_template("login.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        ok, msg = create_user(request.form["username"], request.form["password"])
        if ok:
            return redirect(url_for("login"))
        error = msg

    return render_template("register.html", error=error)


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))


@app.route("/tasks", methods=["GET", "POST"])
def show_tasks():
    if not login_required():
        return redirect(url_for("login"))

    uid = current_user_id()
    error = None

    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description")
        points = int(request.form.get("points_total") or 0)

        weekdays = request.form.getlist("weekdays")

        if not weekdays:
            error = "Bitte mindestens einen Wochentag auswählen."
        else:
            total = get_total_points(uid)
            needed = points * len(weekdays)

            if total + needed <= BUDGET:
                for day in weekdays:
                    insert_task(title, description, day, points, uid)
                return redirect(url_for("show_tasks"))

            error = f"Wochenbudget überschritten ({total + needed}/{BUDGET})"

    return render_template(
        "tasks.html",
        tasks=get_all_tasks(uid),
        current_total=get_total_points(uid),
        budget=BUDGET,
        error=error,
    )


@app.route("/tasks/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    if not login_required():
        return redirect(url_for("login"))

    toggle_task_status(task_id, current_user_id())
    return redirect(url_for("show_tasks"))


@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task_route(task_id):
    if not login_required():
        return redirect(url_for("login"))

    delete_task(task_id, current_user_id())
    return redirect(url_for("show_tasks"))


@app.route("/plan")
def weekly_plan():
    if not login_required():
        return redirect(url_for("login"))

    return render_template("plan.html", weekly_points=get_weekly_points(current_user_id()))


@app.route("/progress")
def progress():
    if not login_required():
        return redirect(url_for("login"))

    uid = current_user_id()
    return render_template(
        "progress.html",
        total_points=get_total_points(uid),
        done_points=get_done_points(uid),
    )


@app.route("/api/status")
def api_status():
    if not login_required():
        return jsonify({"error": "not logged in"})

    uid = current_user_id()
    tasks = get_all_tasks(uid)

    return jsonify(
        {
            "budget": BUDGET,
            "current_total": get_total_points(uid),
            "done_points": get_done_points(uid),
            "done_score": get_user_done_score(uid),
            "task_count": len(tasks),
        }
    )


if __name__ == "__main__":
    app.run()