from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    s = "Environment Variables\n"
    # for k, v in env.items():
    #     s += str(k) + " = " + str(v) + "\n"

    return [s.encode('utf-8')]
