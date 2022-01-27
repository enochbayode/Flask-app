from flask import Blueprint
# from .blueprint.blueprint import blueprint
from flask import current_app as app


# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='template',
    static_folder='static'
)

@home_bp.route('/', methods=['GET'])
def home():
    """Homepage."""
    products = fetch_products(app)
    return render_template(
        'home.html',
        title='Flask Blueprint Demo',
        subtitle='Demonstration of Flask blueprints in action.',
        template='home-template',
        products=products
    )