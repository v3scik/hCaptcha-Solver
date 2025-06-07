# hCaptcha Solver for Discord.com
> ⚠️ **Project Status Notice**  
> Please note that this solver is **no longer actively maintained** due to detection issues on the Discord platform.
> If we are able to remove detection from the Discord site, rest assured that the hCaptcha Solver will be restored.


This hCaptcha solver works perfectly for Discord endpoints:
- `/register`
- `/invites`

## Solver Specifications
- **Average solving time:** 16 seconds
- **Success rate:** 95%

## API Access
Purchase your API key by joining our Discord server:  
👉 [https://discord.gg/zJJJPjftQG](https://discord.gg/zJJJPjftQG)

## API Documentation

### Base URL
`http://193.111.249.67:20043/`

### Endpoints

#### Health Check
**GET /health**  
Verify API availability.

**Response:**
```json
{
  "status": "ok",
  "message": "Server is running"
}
```

#### Service Status
**GET /api/status**  
Check hCaptcha solver status.

**Response:**
```json
{
  "status": "operational",
  "service": "hCaptcha Solver"
}
```

#### Captcha Solving
**POST /api/solve**  
Submit captcha data for solving.

**Headers:**
```
X-API-Key: <your_api_key>
Content-Type: application/json
```

**Request Body:**
```json
{
  "rqdata": "hCaptcha rqdata",
  "proxy": "username:password@host:port"
}
```

**Parameters:**
- `rqdata` - Required captcha challenge data (obtained from frontend)
- `proxy` - HTTP/HTTPS proxy for the connection

**Successful Response:**
```json
{
  "status": "solved",
  "solution": "<captcha_token>"
}
```

### Error Responses
| Status Code | Error                | Description                                      |
|-------------|----------------------|--------------------------------------------------|
| 401         | Unauthorized         | Missing or invalid API key                       |
| 400         | Bad Request          | Missing required fields (rqdata or proxy)        |
| 500         | Internal Server Error| Error occurred during captcha solving process    |

## Examples
See `examples` for implementation examples.
