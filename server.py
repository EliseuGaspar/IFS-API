from src.app import app
from src.routes.routes import *

if __name__ == '__main__':
	app.run(
		debug=True,
		port=1111
	)

