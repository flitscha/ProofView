import asyncio
import json
import subprocess
import os

class LeanSession:
    def __init__(self, lean_file_path, project_root=None):
        self.lean_file_path = lean_file_path
        self.project_root = project_root
        self.uri = f"file://{lean_file_path}"
        self.proc = None


    async def start(self):
        self.proc = await asyncio.create_subprocess_exec(
            'lean', '--server',
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.project_root
        )
        await self._initialize()
        await self._open_file()


    async def _send(self, msg):
        raw = json.dumps(msg)
        header = f"Content-Length: {len(raw)}\r\n\r\n"
        self.proc.stdin.write(header.encode('utf-8') + raw.encode('utf-8'))
        await self.proc.stdin.drain()


    async def _recv_response(self, expected_id):
        while True:
            header = await self.proc.stdout.readline()
            if not header:
                return None
            length = int(header.decode().strip().split(": ")[1])
            await self.proc.stdout.readline()
            body = await self.proc.stdout.read(length)
            response = json.loads(body)
            if response.get("id") == expected_id:
                return response


    async def _initialize(self):
        await self._send({
            "jsonrpc": "2.0",
            "id": 0,
            "method": "initialize",
            "params": {
                "processId": None,
                "rootUri": None,
                "capabilities": {},
            }
        })
        await self._send({
            "jsonrpc": "2.0",
            "method": "initialized",
            "params": {}
        })


    async def _open_file(self):
        with open(self.lean_file_path, 'r') as f:
            text = f.read()

        await self._send({
            "jsonrpc": "2.0",
            "method": "textDocument/didOpen",
            "params": {
                "textDocument": {
                    "uri": self.uri,
                    "languageId": "lean",
                    "version": 1,
                    "text": text
                }
            }
        })


    async def get_goal_at_position(self, line, character, request_id=1):
        await self._send({
            "jsonrpc": "2.0",
            "id": request_id,
            "method": "$/lean/plainGoal",
            "params": {
                "textDocument": {"uri": self.uri},
                "position": {"line": line - 1, "character": character - 1}
            }
        })
        response = await self._recv_response(request_id)

        if response is None:
            return "No response from Lean server."

        result = response.get("result")
        if result is None:
            return "no goals"

        return result.get("rendered", "No goal found.")
