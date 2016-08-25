<?php

/*
 * php5.5+ use bcrypt-hash
 * don't need to slat, hash had been done.
 * php 5.3- use phpass
 */

$password = 'thisMyPassword';

$hashPassword = password_hash($password, PASSWORD_DEFAULT);

echo $hashPassword;//会变化的散列值

password_verify($password, $hashPassword);//true

if (password_verify('aaaa', $hashPassword)) {
    echo 'true';
} else {
    echo 'false';
}
