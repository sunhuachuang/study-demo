(define (square x) (* x x))
(square 5);25

(define (sum_of_square x y) (+ (square x) (square y)))

(sum_of_square 2 3);13

(define (f a) (+ (+ (square a) 1)
                 (+ (square a) 2)))

(f 3);21
