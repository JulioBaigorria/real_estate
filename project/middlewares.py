from fastapi import Request, logger
from starlette.middleware.base import BaseHTTPMiddleware
import time


class ServerTiming(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        try:
            response = await call_next(request)
        except Exception as e:
            logger.logger.exception("HTTP Middleware. Response Error.")
        else:
            process_time = time.time() - start_time
            server_timing = "app;dur=%.2f, db;dur=%.2f"
            response.headers["Server-Timing"] = server_timing % (process_time, 0)
            return response
