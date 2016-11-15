(define (factorial n)
  (display n)
  (if (= n 1)
      1
      (* n (factorial (- n 1)))))

(factorial 5) ;;120

(define (factorial2 n)
  (fact-iter 1 1 n))
(define (fact-iter product counter max)
  (if (> counter max)
      product
      (fact-iter (* product counter) (+ counter 1) max)))

(factorial2 6) ;;720
