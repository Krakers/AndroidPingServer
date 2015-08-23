import web
urls = (
    '/', 'index'
)


class index:
    def GET(self):
        return "Hello, world!"

    def POST(self):
        data = web.data()
        print data
        return data

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
