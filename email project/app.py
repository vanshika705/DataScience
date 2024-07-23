from flask import Flask, render_template, request, url_for
# import sqlite3
# import joblib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == "POST":
        # to recieve the data 
        email = (request.form["email"])

    # unseen_data = [[age, gender_type, bmi, children, smoker_type, health_type, region_northeast, region_northwest, region_southeast, region_southwest]]
    
    # prediction = str(random_forest.predict(unseen_data)[0])
    # print(prediction)
    
    # connection = sqlite3.connect("insurance.db")
    # cur = connection.cursor()
    
    # Data = (age, gender, bmi, children, region, smoker, health, prediction)
    # cur.execute(data_insert_query, Data)
    # print("Your data is inserted into database : ",Data)
    # connection.commit()
    # cur.close()
    # connection.close()
    
    
    # return render_template("final.html", output = prediction)
    
if __name__ == "__main__":
    app.run(debug=True)
    

    
