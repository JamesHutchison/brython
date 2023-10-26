import sanic
from sanic import Sanic

app = Sanic("BrythonBug")

app.static("/static", "./static", name="static_files")


@app.get("/")
async def hello_world(request):
    return await sanic.file("bug.html")


if __name__ == "__main__":
    app.run()
