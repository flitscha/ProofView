import asyncio
import json
import subprocess


async def start_lean_server(lean_file_path):
    proc = await asyncio.create_subprocess_exec(
        'lean', '--server',
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    async def send(msg):
        raw = json.dumps(msg)
        header = f"Content-Length: {len(raw)}\r\n\r\n"
        proc.stdin.write(header.encode('utf-8') + raw.encode('utf-8'))
        await proc.stdin.drain()

    async def recv_response(expected_id):
        while True:
            header = await proc.stdout.readline()
            if not header:
                return None
            length = int(header.decode().strip().split(": ")[1])
            await proc.stdout.readline()
            body = await proc.stdout.read(length)
            response = json.loads(body)

            # is this the response we are looking for?
            if response.get("id") == expected_id:
                return response

    # send initial message to start the server
    await send({
        "jsonrpc": "2.0",
        "id": 0,
        "method": "initialize",
        "params": {
            "processId": None,
            "rootUri": None,
            "capabilities": {},
        }
    })

    await send({
        "jsonrpc": "2.0",
        "method": "initialized",
        "params": {}
    })

    # open the Lean file
    with open(lean_file_path, 'r') as f:
        text = f.read()

    await send({
        "jsonrpc": "2.0",
        "method": "textDocument/didOpen",
        "params": {
            "textDocument": {
                "uri": f"file://{lean_file_path}",
                "languageId": "lean",
                "version": 1,
                "text": text
            }
        }
    })

    # now we send a request to get the gaol at a specific position
    line = 8
    character = 1

    await send({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "$/lean/plainGoal",
        "params": {
            "textDocument": {
                "uri": f"file://{lean_file_path}"
            },
            "position": {
                "line": line - 1,
                "character": character - 1
            }
        }
    })

    response = await recv_response(1)
    print("goal at line:", line, "column:", character)
    print("answer:", json.dumps(response, indent=2))
 