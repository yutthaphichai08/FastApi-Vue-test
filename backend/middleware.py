from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import helper

class AuthenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        
        if request.url.path.startswith("/adminss") :
            try:
                jwt = request.headers['authorization']
                print(jwt)
                helper.verify_access_token()
            except HTTPException as exc:
                return JSONResponse(content={"detail": exc.detail}, status_code=exc.status_code)
            except Exception as exc:
                return JSONResponse(content={"detail": f"Error: {str(exc)}"}, status_code=500)
        response = await call_next(request)
        return response