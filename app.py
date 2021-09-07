from flask import Flask, render_template
from std_msgs.msg import String
import rospy

app = Flask(__name__)
node = rospy.init_node('pepper_app')
pub = rospy.Publisher('/assistant', String, queue_size=10)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/<product>", methods=['GET', 'POST'])
def send_product(product):
    pub.publish(String(product))
    return render_template("index.html")
