defmodule Mix.Tasks.Send.Rabbitmq do
  use Mix.Task

  @shortdoc "test send to rabbitmq"

  def run(name) do
    {:ok, connection} = AMQP.Connection.open
    {:ok, channel} = AMQP.Channel.open(connection)
    AMQP.Basic.publish(channel, "", "hello", "Hello #{name}!")
    AMQP.Connection.close(connection)
    IO.puts " [x] Sent 'Hello World!'"
  end
end
