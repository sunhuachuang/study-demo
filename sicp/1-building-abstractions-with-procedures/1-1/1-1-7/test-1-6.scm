(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))

;;这种方法会递归一直下去 因为是应用序　所以ｃｏｎｄ都会求值
(define (sqrt_iter guess x)
  (new-if (good_enough guess x)
          guess
          (sqrt_iter (improve guess x)
                     x)))
;;(define (sqrt_iter y x)
;;  (if (good_enough y x)
;;      y
;;      (sqrt_iter (improve y x) x)))

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

;;(sqrt 2);;1.4142156862745097

(new-if #t (display "good") (display "bad"))
