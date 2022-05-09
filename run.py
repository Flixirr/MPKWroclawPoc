from app import create_app, register_bp
from app.blueprints.read_from_file import read_from_file
from app.blueprints.route_bp import route_bp
from app.blueprints.closest_bp import closest_bp

app = create_app()
if __name__ == '__main__':
    register_bp(app, read_from_file)
    register_bp(app, route_bp)
    register_bp(app, closest_bp)
    app.debug = True
    app.run(port=8080)