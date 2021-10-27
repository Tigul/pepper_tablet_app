from flask import Flask, render_template, request
from std_msgs.msg import String
import rospy

app = Flask(__name__)
node = rospy.init_node('pepper_app')
pub = rospy.Publisher('/assistant', String, queue_size=10)

@app.route("/")
def start():
    return render_template("index_new.html")

@app.route("/<product>", methods=['POST'])
def send_product(product):
    req = dict(request.form)
    req['product'] = product
    print(req)
    msg = str(req).replace("'", '"')
    print(msg)
    pub.publish(String(msg))
    return render_template("index_new.html")
