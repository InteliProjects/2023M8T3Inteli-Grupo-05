using System.Text;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.SignalR;
using Microsoft.Extensions.ObjectPool;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddSignalR();


// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddSingleton<SignalrHub>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
    app.UseCors(x => x
            .AllowAnyMethod()
            .AllowAnyHeader()
            .SetIsOriginAllowed(origin => true) // allow any origin
            .AllowCredentials());
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.MapHub<SignalrHub>("/hub");

app.Use(async (context, next) =>
{
    var hubContext = context.RequestServices
                        .GetRequiredService<IHubContext<SignalrHub>>();
    Console.WriteLine(hubContext);

    var factory = new ConnectionFactory { HostName = "localhost" };
    var connection = factory.CreateConnection();
    using var channel = connection.CreateModel();
    channel.QueueDeclare("notify");
    Console.WriteLine(connection);
    Console.WriteLine("teste");
    var consumer = new EventingBasicConsumer(channel);
    consumer.Received += async (model, eventArgs) =>
    {
        var body = eventArgs.Body.ToArray();
        var message = Encoding.UTF8.GetString(body);


        Console.WriteLine(message);
        await hubContext.Clients.Client(message).SendAsync("messageReceived", message, message);
        // await teste.Clients.Client(message).SendAsync("messageReceived", message, message);

    };

    channel.BasicConsume(queue: "notify", autoAck: true, consumer: consumer);

    if (next != null)
    {
        await next.Invoke();
    }
});

app.Run();
