(define (sqrt_iter y x)
  (if (good_enough y x)
      y
      (sqrt_iter (improve y x) x)))

(define (good_enough y x)
  (< (abs (- (* y y) x)) 0.001))

(define (improve y x)
  (average y (/ x y)))

(define (average x y)
  (/ (+ x y) 2))

(define (abs x)
  (if (< x 0) (- x) x))

(define (sqrt x)
  (sqrt_iter 1.0 x))

(sqrt 2);;1.4142156862745097
(sqrt 3);;1.7321428571428572
