import kong_pdk.pdk.kong as kong

Schema = (
    {"message": {"type": "string"}},
)

version = '0.1.0'
priority = 0

class Plugin(object):
    def access(self, kong: kong.kong):
        host, err = kong.request.get_header("host")
        if err:
            pass  # error handling
        # if run with --no-lua-style
        # try:
        #     host = kong.request.get_header("host")
        # except Exception as ex:
        #     pass  # error handling
        message = "hello"
        if 'message' in self.config:
            message = self.config['message']
        kong.response.set_header("x-hello-from-python", "Python says %s to %s" % (message, host))
        kong.response.set_header("x-python-pid", str(os.getpid()))

if __name__ == "__main__":
    from kong_pdk.cli import start_dedicated_server
    start_dedicated_server("py-hello", Plugin, version, priority)