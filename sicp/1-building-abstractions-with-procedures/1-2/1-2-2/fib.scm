;; Fibonacci numbers

;; recursive
(define (fib n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 1))
                 (fib (- n 2))))))

;;(fib 6) ;;8

(define (fib-iter a b step n)
  (define next-a (+ a b))
  (define next-b a)
  (define next-step (+ step 1))
  (if (> next-step n) next-a
      (fib-iter next-a next-b next-step n)))

(define (fib2 n)
  (fib-iter 0 1 1 n))

(fib2 6)

;;iteration
(define (fib3 n)
  (fib-iter3 1 0 n))

(define (fib-iter3 a b count)
  (if (= count 0)
      b
      (fib-iter3 (+ a b) a (- count 1))))

(fib3 6)
