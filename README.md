# hCaptcha solver for Discord.com
Solver works perfectly for **/register** and **/invites**

Informations about solver:
- Average time: 16s
- Successfully: 95%

## How to access the API? 
You can purchase access to your own key on this Discord: https://discord.gg/zJJJPjftQG

## API Requests:
API URL: http://193.111.249.67:20043/
You can find examples in examples.py

**GET /health**
Verify that the API is working properly.
**Response:**
```json
{
  "status": "ok",
  "message": "Server is running"
}
```

## hCaptcha status:
**GET /api/status**
Check that the hCaptcha solver is working properly
**Response:**
```json
{
  "status": "operational",
  "service": "hCaptcha Solver"
}
```

## hCaptcha solving:
**POST /api/solve**
Endpoint to upload captcha data and proxy.

**HEADERS**
X-API-Key: <twój_klucz_api>
Content-Type: application/json

Payload: **JSON**
```json
{
  "rqdata": "hCap rqdata",
  "proxy": "login:password@host:port"
}
```

rqdata - the data required to solve the captcha (received, for example, from the frontend).
proxy - proxy in HTTP(S) format that will be used for the connection.

**Response**:
```json
{
  "status": "solved",
  "solution": "<captcha key>"
}
```

**ERRORS**:
> 401 Unauthorized - missing or invalid API key.
> 400 Bad Request - missing required fields in body (rqdata or proxy).
> 500 Internal Server Error - problem with captcha solution.
