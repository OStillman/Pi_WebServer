var hostname = "192.168.68.116";
var port = 1884;

// Create a client instance
var client = new Paho.MQTT.Client(hostname, Number(port), "clientId");

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({
    onSuccess: onConnect
});


// called when the client connects
function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("onConnect");
    header.notices = "No Notices"
    presence_owen.init()
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
        console.log("onConnectionLost:" + responseObject.errorMessage);
        header.notices = "Lost connection to MQTT Server!";
    }
}

// called when a message arrives
function onMessageArrived(message) {
    //console.log("Message arrived: topic=" + message.destinationName + ", message=" + message.payloadString);
    if (message.destinationName ==  "presence/owen"){
        presence_owen.statusUpdate(message.payloadString);
    }
}

let presence_owen = {
    init: function(){
        console.info("Subscribing to Owen's status...");
        client.subscribe("presence/owen");
        console.info("Subscribed to Owen")
    },
    statusUpdate: function(status){
        console.info("Owen's status has been updated");
        console.log(`Owen is ${status}`);
        presence_detection.owen_status = status
    }
};