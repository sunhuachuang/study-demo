<?php
echo 'this is pdo</br>';

try{
    // Create a new connection.
    // You'll probably want to replace hostname with localhost in the first parameter.
    // Note how we declare the charset to be utf8mb4.  This alerts the connection that we'll be passing UTF-8 data.  This may not be required depending on your configuration, but it'll save you headaches down the road if you're trying to store Unicode strings in your database.  See "Gotchas".
    // The PDO options we pass do the following:
    // \PDO::ATTR_ERRMODE enables exceptions for errors.  This is optional but can be handy.
    // \PDO::ATTR_PERSISTENT disables persistent connections, which can cause concurrency issues in certain cases.  See "Gotchas".
    $link = new PDO('mysql:host=localhost;dbname=test', 'root', 'sun');

    $handle = $link->prepare('select * from user where id = 2');

    // PHP bug: if you don't specify PDO::PARAM_INT, PDO may enclose the argument in quotes.  This can mess up some MySQL queries that don't expect integers to be quoted.
    // See: https://bugs.php.net/bug.php?id=44639
    // If you're not sure whether the value you're passing is an integer, use the is_int() function.
//    $handle->bindValue(1, 2, PDO::PARAM_INT);
//    $handle->bindValue(2, 'lisi');

    $handle->execute();

    $result = $handle->fetch(PDO::FETCH_OBJ);
    print_r($result);
    // Using the fetchAll() method might be too resource-heavy if you're selecting a truly massive amount of rows.
    // If that's the case, you can use the fetch() method and loop through each result row one by one.
    // You can also return arrays and other things instead of objects.  See the PDO documentation for details.
    // $result = $handle->fetchAll(PDO::FETCH_OBJ);

    // foreach($result as $row){
    //     print($row->Username);
    // }

    $link = null;
    echo '</br>this is end';

} catch(\PDOException $ex) {
    print($ex->getMessage());
}