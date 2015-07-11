import web
import time
urls = (
    '/', 'index'
)

class index:
    def GET(self):
    	time.sleep(2)
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()