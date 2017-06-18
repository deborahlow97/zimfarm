from datetime import datetime
from flask.json import JSONEncoder
from database.task import Task


class ZimfarmDispatcherJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Task):
            json = {
                'id': o.id,
                'name': o.name,
                'status': o.status,
                'time': {
                    'created': self.encode_datetime(o.created_time),
                    'started': self.encode_datetime(o.started_time),
                    'finished': self.encode_datetime(o.finished_time)
                },
                'command': o.command,
                'return_code': o.return_code,
                'result': {
                    'stdout': o.stdout,
                    'stderr': o.stderr,
                    'error': o.error
                },
            }
            return json
        else:
            JSONEncoder.default(self, o)

    def encode_datetime(self, d: datetime):
        return d.isoformat() + 'Z' if isinstance(d, datetime) else None
