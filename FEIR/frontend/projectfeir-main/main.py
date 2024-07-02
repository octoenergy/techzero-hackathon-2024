import os

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  """Home Page route."""
  return render_template('index.html')

@app.route("/pages/enterprise")
def enterprise_dashboard():
  return render_template('enterprise_index.html')

@app.route("/pages/sme")
def sme_dashboard():
  return render_template('sme_index.html')

@app.route("/pages/supplier")
def supplier_dashboard():
  return render_template('aupplier_index.html')

@app.route("/pages/help")
def help_pages():
  return "This is some help!"

skeleton_reply = {
  'title': 'This is information that would be displayed on a dashboard'
}

@app.route("/api/enterprise_dashboard")
def enterprise_api():
  skeleton_reply['target_audience'] = "Enterprise"
  return jsonify(skeleton_reply)

@app.route("/api/sme_dashboard")
def sme_api():
  skeleton_reply['target_audience'] = "SME"
  return jsonify(skeleton_reply)

@app.route("/api/supplier_dashboard")
def supplier_api():
  skeleton_reply['target_audience'] = "Supplier"
  return jsonify(skeleton_reply)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))