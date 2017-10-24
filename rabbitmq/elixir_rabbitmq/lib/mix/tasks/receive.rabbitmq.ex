defmodule Mix.Tasks.Receive.Rabbitmq do
  use Mix.Task

  @shortdoc "listen receive rabbitmq"

  def wait_for_messages do
    receive do
      {:basic_deliver, payload, _meta} ->
        IO.puts String.valid? payload
        IO.puts " [x] Received #{payload}"
        wait_for_messages()
    end
  end

  def run(_) do
    {:ok, connection} = AMQP.Connection.open
    {:ok, channel} = AMQP.Channel.open(connection)
    AMQP.Queue.declare(channel, "hello")
    AMQP.Basic.consume(channel, "hello", nil, no_ack: true)
    IO.puts " [*] Waiting for messages. To exit press CTRL+C, CTRL+C"

    wait_for_messages()
  end
end
