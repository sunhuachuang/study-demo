(define (add_two_bigger x y z)
  (if (and (> x z) (> y z)) (+ x y))
  (if (and (> x y) (> z y)) (+ x z))
  (if (and (> y x) (> z x)) (+ y z)))

(add_two_bigger 1 2 3)
