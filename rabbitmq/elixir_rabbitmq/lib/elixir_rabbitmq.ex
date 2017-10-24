defmodule ElixirRabbitmq do
  @moduledoc """
  Documentation for ElixirRabbitmq.
  """

  @doc """
  Hello world.

  ## Examples

      iex> ElixirRabbitmq.hello
      :world

  """
  def hello do
    {:ok, connection} = AMQP.Connection.open
    {:ok, channel} = AMQP.Channel.open(connection)
    AMQP.Basic.publish(channel, "", "hello2", "Hello World!")
    IO.puts " [x] Sent 'Hello World!'"
  end
end
