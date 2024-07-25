from flask import Flask, render_template, request, url_for
import joblib 

bow_obj = joblib.load("./models/bag_of_words.lb")
model = joblib.load("./models/bernouliNB.lb")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prediction",methods=["POST","GET"])
def prediction():
    if request.method == "POST":
        message = str(request.form["message"])
        email_message = [message]
        email_converted = bow_obj.transform(email_message).toarray()        
        prediction = model.predict(email_converted)[0]
        label_dict = {"0":"ham","1":"spam"}
        # print(label_dict[str(prediction)])
        return render_template("output.html", output = label_dict[str(prediction)])
    
if __name__ == "__main__":
    app.run(debug=True)
    