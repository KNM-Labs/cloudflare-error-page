"""
Simple Flask application using cloudflare-error-page package.
Serves customizable Cloudflare-style error pages.
"""

from flask import Flask, request, jsonify
from cloudflare_error_page import render as render_cf_error_page

app = Flask(__name__)

@app.route('/custom', methods=['POST'])
def custom_error():
    """Generate custom error page from JSON payload"""
    params = request.get_json() or {}
    return render_cf_error_page(params)

@app.route('/')
def error_500():
    """500 Internal Server Error"""
    return render_cf_error_page({
        "title": "Oopsie woopsies we've made a fuckie wuckie",
        "error_code": "500",
        "browser_status": {"status": "ok"},
        "cloudflare_status": {"status": "error"},
        "host_status": {"status": "ok", "location": "Your mum gey", "status_text": "Working"},
        "error_source": "host",
        "what_happened": "<p>The web server is being a stupid wittle bum 👉👈 oopsies hehe .</p>",
        "what_can_i_do": "<p>Please try again in a few minutes.</p>",
    })


@app.route('/502')
def error_502():
    """502 Bad Gateway"""
    return render_cf_error_page({
        "title": "Bad gateway",
        "error_code": "502",
        "browser_status": {"status": "ok"},
        "cloudflare_status": {"status": "error", "status_text": "Error"},
        "host_status": {"status": "ok", "location": request.host},
        "error_source": "cloudflare",
        "what_happened": "<p>The web server reported a bad gateway error.</p>",
        "what_can_i_do": "<p>Please try again in a few minutes.</p>",
    })


@app.route('/503')
def error_503():
    """503 Service Unavailable"""
    return render_cf_error_page({
        "title": "Service temporarily unavailable",
        "error_code": "503",
        "browser_status": {"status": "ok"},
        "cloudflare_status": {"status": "ok"},
        "host_status": {"status": "error", "location": request.host, "status_text": "Unavailable"},
        "error_source": "host",
        "what_happened": "<p>The web server is currently unavailable.</p>",
        "what_can_i_do": "<p>Please try again in a few minutes.</p>",
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, debug=True)
