
const WebSocket = require('ws');
const socketcan = require('socketcan');

// Create a raw CAN channel, replace 'vcan0' with your actual CAN interface
const channel = socketcan.createRawChannel("vcan0", true);

// Create a WebSocket server
const wss = new WebSocket.Server({ port: 8081 });

// Function to broadcast messages to all connected clients
const broadcast = (data) => {
    wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(data);
        }
    });
};

// Listen for incoming CAN messages
channel.addListener("onMessage", (msg) => {
    // Implement your filtering logic here
    // For example, only forward messages with a specific ID
    //console.log("Received CAN message:", msg);
    if (msg.id === 0x0CF00400 || msg.id === 0x18FEF100) { // Replace 123 with the ID of the messages you're interested in
        // Convert the message to a desired format if necessary
        //console.log("Received CAN message:", msg);
	const dataToSend = JSON.stringify(msg);

        // Broadcast the message to all connected WebSocket clients
        broadcast(dataToSend);
    }
});

// Start listening for messages on the CAN interface
channel.start();

console.log('WebSocket server started on ws://localhost:8081');
console.log('Listening for CAN messages on interface vcan0...');

