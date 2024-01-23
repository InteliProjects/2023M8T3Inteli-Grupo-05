import * as signalR from "@microsoft/signalr";
const URL = "http://localhost:5002/hub"; //or whatever your backend port is
class Connector {
    private connection: signalR.HubConnection;
    public events: (onMessageReceived: (username: string, message: string) => void) => void;
    static instance: Connector;
    constructor() {
        this.connection = new signalR.HubConnectionBuilder()
            .withUrl(URL)
            .withAutomaticReconnect()
            .build();
        this.connection.start().catch((err: any) => document.write(err));
        this.events = (onMessageReceived) => {
            this.connection.on("messageReceived", (username: any, message: any) => {
                onMessageReceived(username, message);
            });
        };
    }
    public newMessage = (messages: string) => {
        this.connection.send("newMessage", this.connection.connectionId, messages).then((x: any) => console.log("sent"))
        console.log(this.connection.connectionId)
    }
    public static getInstance(): Connector {
        if (!Connector.instance)
            Connector.instance = new Connector();
        return Connector.instance;
    }
}
export default Connector.getInstance;