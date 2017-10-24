defmodule ElixirRabbitmqTest do
  use ExUnit.Case
  doctest ElixirRabbitmq

  test "greets the world" do
    assert ElixirRabbitmq.hello() == " [x] Sent 'Hello World!'"
  end
end
