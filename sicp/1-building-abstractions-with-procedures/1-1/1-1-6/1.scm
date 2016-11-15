(define (cabs x) (cond ((< x 0) (- x)) ((= x 0) 0) ((> x 0) x)))

(define (eabs x) (cond ((< x 0) (- x)) (else x)))

(define (abs x) (if (< x 0) (- x) x))

(abs -5)
(eabs -6)
(cabs -7)

(define (aabs x)
  (if
   (or (= x 0) (> x 0))
   x)
  (- x))

(aabs -8)

;; x < variable < y
(define (between x y m)
  (and (< x m) (> y m)))

(between 2 7 3) ;;#t
(between 2 3 4) ;;#f

(define (neq x y)
  (not (= x y)))

(neq 3 4) ;;#t
(neq 4 4) ;;#f
