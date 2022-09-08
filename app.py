from flask import Flask, render_template, request
from std_msgs.msg import String
from pepper_behaviour_srvs.srv import Visualize
import rospy

app = Flask(__name__)
node = rospy.init_node('pepper_app')
pub = rospy.Publisher('/assistant', String, queue_size=10)
vis_service = rospy.ServiceProxy('/visualize_shelf', Visualize)

@app.route("/")
def start():
    return render_template("index_grid.html")

@app.route("/<product>", methods=['POST'])
def send_product(product):
    req = dict(request.form)
    req['product'] = product
    #print(req)
    msg = str(req).replace("'", '"')
    print(msg)
    #pub.publish(String(msg))
    vis_service(msg)
    return render_template("vis_img.html")
