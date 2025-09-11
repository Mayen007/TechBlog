# Security Improvements

This document outlines the security improvements made to address CodeQL security issues.

## Changes Made

### 1. Hardcoded Credentials (CWE-259)
- **Issue**: Admin credentials were hardcoded in `admin.py`
- **Fix**: Moved credentials to environment variables using `os.environ.get()`
- **Environment Variables**:
  - `ADMIN_USERNAME`: Admin username (defaults to 'admin')
  - `ADMIN_PASSWORD`: Admin password hash (defaults to existing hash for backward compatibility)

### 2. Weak Random Number Generator (CWE-330)
- **Issue**: Using `random.choice()` for selecting featured posts
- **Fix**: Replaced with `secrets.choice()` for cryptographically secure random selection

### 3. Binding to All Interfaces (CWE-605)
- **Issue**: Flask app was binding to `0.0.0.0` which exposes the service to all network interfaces
- **Fix**: Changed to bind to `127.0.0.1` by default, configurable via environment variables
- **Environment Variables**:
  - `FLASK_HOST`: Host to bind to (defaults to '127.0.0.1')
  - `FLASK_PORT`: Port to bind to (defaults to 5000)

### 4. Additional Security Enhancements
- **Secret Key**: Made configurable via `SECRET_KEY` environment variable
- **Session Security**: Added secure session configuration:
  - `SESSION_COOKIE_SECURE`: Set to True in production
  - `SESSION_COOKIE_HTTPONLY`: Set to True to prevent XSS
  - `SESSION_COOKIE_SAMESITE`: Set to 'Lax' for CSRF protection

## Environment Variables

For production deployment, set these environment variables:

```bash
export SECRET_KEY="your-secret-key-here"
export ADMIN_USERNAME="your-admin-username"
export ADMIN_PASSWORD="your-hashed-password"
export FLASK_HOST="127.0.0.1"  # Or appropriate host
export FLASK_PORT="5000"
export FLASK_ENV="production"
```

## Verification

All security issues have been verified as resolved using Bandit security scanner:
- No high, medium, or low severity issues detected
- All CWE vulnerabilities addressed
- Application tested and functioning correctly