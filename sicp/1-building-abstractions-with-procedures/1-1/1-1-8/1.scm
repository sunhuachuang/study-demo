(define (sqrt x)
  (define (sqrt_iter y)
    (if (good_enough y)
        y
        (sqrt_iter (improve y))))

  (define (good_enough y)
    (< (abs (- (* y y) x)) 0.001))

  (define (improve y)
    (average y (/ x y)))

  (define (average x y) ;;内部形式参数
    (/ (+ x y) 2))

  (define (abs x);;内部形式参数
    (if (< x 0) (- x) x))

  (sqrt_iter 1.0))

(sqrt 2);;1.4142156862745097
