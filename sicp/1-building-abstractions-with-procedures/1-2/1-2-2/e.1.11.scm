;; f(n): n<3 => fn = n
;;       n>3 => fn = f(n-1) + 2f(n-2) + 3f(f-3)

;; recursive

(define (f-recu n)
  (if (< n 3)
      n
      (+ (f (- n 1))
         (* 2 (f (- n 2)))
         (* 3 (f (- n 3))))))

(display (f-recu 10))

;; iteration
(define (f-iter n)
  (f-iter-act 2 1 0 n))

(define (f-iter-act a b c count)
  (if (< count 3)
      a
      (f-iter-act (+ a (* 2 b) (* 3 c)) a b (- count 1))))

(f-iter 10)
