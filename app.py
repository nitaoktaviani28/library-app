import os
from flask import Flask

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Library Management")
APP_ENV = os.getenv("APP_ENV", "LOCAL")
APP_VERSION = os.getenv("APP_VERSION", "v1")


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                color: #1f2937;
            }}

            .header {{
                background: #1f2937;
                color: white;
                padding: 30px;
                text-align: center;
            }}

            .header h1 {{
                margin: 0 0 10px 0;
            }}

            .container {{
                max-width: 1000px;
                margin: 40px auto;
                padding: 20px;
            }}

            .card {{
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            }}

            .info {{
                display: flex;
                gap: 20px;
                margin: 25px 0;
            }}

            .box {{
                flex: 1;
                background: #f3f4f6;
                padding: 20px;
                border-radius: 10px;
            }}

            .box-title {{
                font-size: 14px;
                color: #6b7280;
                margin-bottom: 8px;
            }}

            .box-value {{
                font-size: 20px;
                font-weight: bold;
            }}

            .version {{
                display: inline-block;
                padding: 8px 15px;
                border-radius: 20px;
                background: #e5e7eb;
                font-weight: bold;
                margin-top: 10px;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 25px;
            }}

            th,
            td {{
                padding: 14px;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }}

            th {{
                background: #f3f4f6;
            }}

            .available {{
                font-weight: bold;
            }}

            .borrowed {{
                font-weight: bold;
            }}

            .footer {{
                text-align: center;
                margin-top: 25px;
                color: #6b7280;
                font-size: 14px;
            }}
        </style>
    </head>

    <body>

        <div class="header">
            <h1>📚 Library Management</h1>
            <p>Kubernetes Demo Application</p>
        </div>

        <div class="container">

            <div class="card">

                <h2>Library Dashboard</h2>

                <div class="info">

                    <div class="box">
                        <div class="box-title">
                            Environment
                        </div>

                        <div class="box-value">
                            {APP_ENV}
                        </div>
                    </div>

                    <div class="box">
                        <div class="box-title">
                            Application Version
                        </div>

                        <div class="box-value">
                            {APP_VERSION}
                        </div>
                    </div>

                    <div class="box">
                        <div class="box-title">
                            Application
                        </div>

                        <div class="box-value">
                            Library App
                        </div>
                    </div>

                </div>

                <h3>Book List</h3>

                <table>

                    <tr>
                        <th>ID</th>
                        <th>Book</th>
                        <th>Author</th>
                        <th>Status</th>
                    </tr>

                    <tr>
                        <td>001</td>
                        <td>Clean Code</td>
                        <td>Robert C. Martin</td>
                        <td class="available">
                            Available
                        </td>
                    </tr>

                    <tr>
                        <td>002</td>
                        <td>The DevOps Handbook</td>
                        <td>Gene Kim</td>
                        <td class="borrowed">
                            Borrowed
                        </td>
                    </tr>

                    <tr>
                        <td>003</td>
                        <td>Kubernetes Up & Running</td>
                        <td>Kelsey Hightower</td>
                        <td class="available">
                            Available
                        </td>
                    </tr>

                    <tr>
                        <td>004</td>
                        <td>Docker Deep Dive</td>
                        <td>Nigel Poulton</td>
                        <td class="available">
                            Available
                        </td>
                    </tr>

                </table>

                <div class="version">
                    Version: {APP_VERSION}
                </div>

                <div class="footer">
                    Running on Kubernetes 🚀
                </div>

            </div>

        </div>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return "OK", 200


@app.route("/version")
def version():
    return {
        "application": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )