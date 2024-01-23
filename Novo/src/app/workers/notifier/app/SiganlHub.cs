using System.Text;
using Microsoft.AspNetCore.SignalR;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;
public class SignalrHub : Hub
{
    public SignalrHub() {}
    public async Task NewMessage(string user, string message)
    {
        await Clients.Client(user).SendAsync("messageReceived", user, message);
        Console.WriteLine(user);
    }
}