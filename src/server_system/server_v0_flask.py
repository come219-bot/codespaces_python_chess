from flask import Flask
import uuid
import datetime

class WebServer:
    def __init__(self):
        self.server_id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.status = 'stopped'
        self.app = Flask(__name__)

        @self.app.route('/')
        def index():
            return 'Hello World!'

    def run_server(self, host='127.0.0.1', port=5000):
        self.status = 'running'
        self.app.run(host=host, port=port)

    def stop_server(self):
        self.status = 'stopped'
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug server')
        func()

    def get_server_details(self):
        if self.status == 'running':
            server_ip = self.app.run().host
            server_port = self.app.run().port
        else:
            server_ip = None
            server_port = None
        return {
            'server_id': self.server_id,
            'created_at': self.created_at,
            'status': self.status,
            'server_ip': server_ip,
            'server_port': server_port
        }
